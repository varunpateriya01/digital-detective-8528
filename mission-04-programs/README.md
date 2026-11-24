# Mission 4 — How programs run

## 1. Mission title
Mission 4 — How programs run

## 2. Task / objective
Create and run a small Python program, then compare compilation and interpretation.

## 3. Work completed
I saved a one-line program in `hello.py` and ran it from Terminal with Python 3. It printed `Hello from Python`. I compared how compilers and interpreters translate or execute source code.

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates source code into another form before the program runs. | Executes instructions at runtime; many interpreters also translate to an intermediate form first. |
| Typical output | Object code or an executable program. | Results produced while the interpreter runs the program. |
| One example | A C compiler such as `clang`. | The Python interpreter. |
| One advantage | The translated program can run efficiently without translating the source each time. | It is convenient to run and inspect code during development. |

A compiler translates a program before normal execution, often producing object code or an executable. An interpreter handles program instructions while the program runs. The distinction is useful, but real language implementations can combine both approaches. Python, for example, commonly compiles source to bytecode and then runs that bytecode in its virtual machine.

## 4. Commands / tools used
- Python 3 — ran `mission-04-programs/hello.py`.
- `python3 mission-04-programs/hello.py` — displayed `Hello from Python`.

## 5. My understanding
Both approaches turn a program into actions the computer can perform. A compiler does more translation ahead of execution, while an interpreter is involved as the program runs. The names describe common approaches; modern language runtimes can combine them.

## 6. Difficulties faced
No major difficulties.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- `hello.py` — the working Python program.
- Terminal output: `Hello from Python`.

## 9. Commit details
Commit message: `Compare compilers and interpreters`. The completed mission was pushed to the public GitHub repository.
