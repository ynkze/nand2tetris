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

with open(args.filename, 'r') as infile, open(hackfile, 'w') as outfile:
    for line in infile:
        start_line = line.replace(" ", "")[0]

        if start_line == "/" or start_line.isspace(): # skip comments and whitespace
            continue
        elif start_line == "@": # translate a-instruction
            address = int(line[1:])
            outstring = bin(address)[2:].zfill(16) + "\n"
            outfile.write(outstring)
        else: # translate c-instruction
            start, a, comp, dest, jump = "111", "0", "101010", "000" , "000"
            if ";" in line:
                parts = re.split(r'\s*;\s*', line)
                jump = jump_dict[parts[1].strip()]
                line = parts[0]
                if "=" not in line:
                    comp = comp_dict[parts[0]]
            
            if "=" in line:
                parts = re.split(r'\s*=\s*', line)
                dest = dest_dict[parts[0].strip()]
                if "M" in parts[1]:
                    a = "1"
                    parts[1] = parts[1].replace("M", "A")
                comp = comp_dict[parts[1].strip()]

            outfile.write(start + a + comp + dest + jump + "\n")

    print("Assembly finished")
