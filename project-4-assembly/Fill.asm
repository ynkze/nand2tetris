// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.

(LOOP)
@KBD
D=M
@BLACK
D;JGT
@WHITE
D;JEQ

(BLACK)
@8192
D=A

(BLACK2)
@SCREEN
A=D+A
M=-1
D=D-1
@BLACK2
D;JGE

@LOOP
0;JMP

(WHITE)
@8192
D=A

(WHITE2)
@SCREEN
A=D+A
M=0
D=D-1
@WHITE2
D;JGE

@LOOP
0;JMP
