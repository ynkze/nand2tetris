# usage: `python3 assembler.py asm-files/Rect.asm` would produce a `Rect.hack` file

import argparse
import re

parser = argparse.ArgumentParser(description='Translate assembly .asm file into binary .hack file')
parser.add_argument("filename", help=".asm file to convert")
args = parser.parse_args()

hackfile = (re.search(r'[^/\\]+(?=\.)', args.filename)).group() + ".hack"

jump_dict = {
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

dest_dict = {
    "0": "000",
    "M": "001",
    "D": "010",
    "DM": "011",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "ADM": "111"
}

comp_dict = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "A": "110000",
    "!D": "001101",
    "!A": "110001",
    "-D": "001111",
    "-A": "110011",
    "D+1": "011111",
    "A+1": "110111",
    "D-1": "001110",
    "A-1": "110010",
    "D+A": "000010",
    "D-A": "010011",
    "A-D": "000111",
    "D&A": "000000",
    "D|A": "010101"
}

symbol_table = {
    "SP": "0",
    "LCL": "1",
    "ARG": "2",
    "THIS": "3",
    "THAT": "4",
    "R0": "0",
    "R1": "1",
    "R2": "2",
    "R3": "3",
    "R4": "4",
    "R5": "5",
    "R6": "6",
    "R7": "7",
    "R8": "8",
    "R9": "9",
    "R10": "10",
    "R11": "11",
    "R12": "12",
    "R13": "13",
    "R14": "14",
    "R15": "15",
    "SCREEN": "16384",
    "KBD": "24576"
}


# first pass to initialize symbols reference
with open(args.filename, 'r') as infile:
    count = 0
    for line in infile:
        start_line = line.replace(" ", "")[0]

        if start_line == "(": # label symbols
            label = line.strip()[1:-1]
            if label not in symbol_table:
                symbol_table[label] = str(count)

        if start_line == "/" or start_line.isspace() or start_line == "(":
            continue

        count += 1

# second pass to decode the instructions
with open(args.filename, 'r') as infile, open(hackfile, 'w') as outfile:
    variable_value = 16
    for line in infile:
        start_line = line.replace(" ", "")[0]

        if start_line == "/" or start_line.isspace() or start_line == "(": # skip comments, labels, whitespace
            continue
        elif start_line == "@": # translate a-instruction
            variable = line.strip()[1:]

            if not variable.isnumeric(): # resolve pre-defined symbol or variable
                if variable not in symbol_table:
                    symbol_table[variable] = variable_value
                    variable_value += 1
                variable = symbol_table[variable]

            address = int(variable)
            outstring = bin(address)[2:].zfill(16) + "\n"
            outfile.write(outstring)
        else: # translate c-instruction
            start, a, comp, dest, jump = "111", "0", "101010", "000" , "000"
            if ";" in line:
                parts = re.split(r'\s*;\s*', line)
                jump = jump_dict[parts[1].strip()]
                if "=" not in parts[0]:
                    comp = comp_dict[parts[0].strip()]
            
            if "=" in line:
                parts = re.split(r'\s*=\s*', line)
                dest = dest_dict[parts[0].strip()]
                # since A and M register binary instruction are quite similar, we set variable "a" depending on if its M
                if "M" in parts[1]:
                    a = "1"
                    parts[1] = parts[1].replace("M", "A")
                comp = comp_dict[parts[1].strip()]

            outfile.write(start + a + comp + dest + jump + "\n")

    print("Assembly finished")
