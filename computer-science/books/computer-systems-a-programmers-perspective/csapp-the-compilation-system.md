CSAPP The compilation System
===

```c
// hello.c
 #include <stdio.h>

 int main()
{
    printf("hello, world\n");
}
```

The hello program begins life as a high-level C program because it can be read
and understood by human beings in that form. However, in order to run hello.c on
the system, the individual C statements must be translated by other programs
into a sequence of low-level machine-language instructions. These instructions
are then packaged in a form called an executable object program and stored as a
binary disk file. Object programs are also referred to as executable object
files.

On a Unix system, the translation from source file to object file is performed
by a compiler driver.

```bash
gcc -o hello hello.c
```

![The Compilation System](./assets/The_Compilation_System.png)

4 stages
---

- preprocessor
- compiler
- assembler
- linker

All 4 collectively form the Compilation System.

Preprocessing phase
---
The preprocessor (cpp) modifies the original C program according to directives
that begin with the # character. For example, the #include <stdio.h> command in
line 1 of hello.c tells the preprocessor to read the contents of the system
header file stdio.h and insert it directly into the program text. The result is
another C program, typically with the .i suffix.

Compilation phase
---
The compiler (cc1) translates the text file hello.i into the text file hello.s,
which contains an assembly-language program. Each statement in an
assembly-language program exactly describes one low-level machine-language
instruction in a standard text form. Assembly language is useful because it
provides a common output language for different compilers for different
high-level languages. For example, C compilers and Fortran compilers both
generate output files in the same assembly language.

Assembly phase
---
Next, the assembler (as) translates hello.s into machine-language instructions,
packages them in a form known as a relocatable object program, and stores the
result in the object file hello.o. The hello.o file is a binary file whose bytes
encode machine language instructions rather than characters. If we were to view
hello.o with a text editor, it would appear to be gibberish.

Linking phase
---
Notice that our hello program calls the printf function, which is part of the
standard C library provided by every C compiler. The printf function resides in
a separate precompiled object file called printf.o, which must somehow be merged
with our hello.o program. The linker (ld) handles this merging. The result is
the hello file, which is an executable object file (or simply executable) that
is ready to be loaded into memory and executed by the system.
