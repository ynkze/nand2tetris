# Nand2Tetris

Code for [Nand2Tetris](https://www.nand2tetris.org/) course to build a mini computer from scratch, called the Hack computer.
Project 1-6 is for the hardware while Project 7-12 is for the software.

## Project 1: Elementary Gates

Made elementary gates starting with a given NAND gate, mostly using truth table to convert to boolean function then reducing the expression to existing available parts.

## Project 2: ALU

Made arithmetic parts then made ALU (which will be part of the CPU), ALU can compute what operation to do e.g. addition and/or negation based on the op-code.

## Project 3: Memory

Made memory parts like registers and RAMs (which CPU will use to store and retrieve instructions), using the sequential logic of D-flip flops.

## Project 4: Machine Language

Hands-on with Hack computer assembly language to do implement multiplication (since the instruction sets only contain addition/subtraction, multiplication is not implemeneted on the hardware level) and interfacing keyboard presses to display on screen.

## Project 5: Computer Architecture

Made memory and CPU and then putting them together to make the underlying computer hardware, the difficulty was following the given CPU architecture and deciding which control bits to which gates using the Hack instruction set:
![image](https://github.com/user-attachments/assets/d90bf3fa-3689-4d77-a844-84365587ac08)
<img width="699" alt="Screenshot 2024-08-26 at 11 07 23 PM" src="https://github.com/user-attachments/assets/7da81a1b-8ca0-46e2-a3bc-d6194466a707">

The overall computer architecture to create:
![image](https://github.com/user-attachments/assets/239b5863-1a1b-4adc-9e40-01f7ea0b9f8e)

## Project 6: Assembler

Created a simple assembler Python script that translates Hack assembly language into binary code.
