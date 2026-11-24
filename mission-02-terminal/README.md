# Mission 2 — Become comfortable with the Terminal

## 1. Mission title
Mission 2 — Become comfortable with the Terminal

## 2. Task / objective
Practise basic command-line navigation and safe file changes, explain flags and pipes, and inspect a package manager without installing or uninstalling anything.

## 3. Work completed
I practised these commands inside `mission-02-terminal/terminal-practice/practice`: `pwd`, `ls`, `ls -lah`, `cd`, `mkdir`, `touch`, `cp`, `mv`, and `cat`. I created a blank file, wrote two lines to a note, made a backup copy, renamed a copied file, and read the original back. Both lines remained after I appended the second one. I also used `ls -lh | head -n 5` to send a directory listing through a pipe and show only its first five lines.

The `-a` flag revealed `.hidden-demo`, which a normal listing did not show. The `-h` flag displayed sizes in readable units such as bytes.

Homebrew was installed. `brew --version` returned `Homebrew 7.0.7`; `brew list --formula` displayed the installed formula names. I did not install or remove any packages.

## 4. Commands / tools used

| Command | Purpose | Observation |
|---|---|---|
| `pwd` | Print the current directory. | Showed the mission practice location; I recorded only the repository-relative path. |
| `ls` | List visible names. | Listed `practice` from the terminal-practice folder. |
| `ls -lah` | Show details, hidden names and human-readable sizes. | Included `.hidden-demo`, permissions, file sizes and timestamps. |
| `cd ..` / `cd terminal-practice` | Change directories. | Moving to the parent changed the location from the practice folder to the Mission 2 folder. |
| `mkdir practice` | Create a directory. | Created the isolated file-practice area. |
| `touch empty.txt` | Create an empty file. | The listing showed a zero-byte file. |
| `cp notes.txt notes-backup.txt` | Copy a file. | The source and backup both remained. |
| `mv copied.txt moved-and-renamed.txt` | Move or rename a file. | The renamed copy appeared under its new name. |
| `cat notes.txt` | Display file contents. | Both saved lines were printed. |
| `>` and `>>` | Write or append redirected output. | `>` made the first line; `>>` added the second without erasing it. |
| `ls -lh \| head -n 5` | Pipe a listing to another command. | `ls` supplied lines; `head` kept the first five. |
| `brew --version` | Display Homebrew's version. | Returned version 7.0.7. |
| `brew list --formula` | List installed formula packages. | Displayed the package names managed by Homebrew. |

## 5. My understanding
The current-directory command tells me where relative paths will be interpreted. A directory listing helps me confirm which files are present before changing anything. Redirection with `>` replaces a file's contents, while `>>` adds text at the end. Copying leaves the original in place; moving transfers it or changes its name. A pipe connects one command's output to another command's input. A package manager keeps software installation and version information in one place; it can make software easier to maintain, but I only inspected it for this task.

## 6. Difficulties faced
After using `cd ..` from the mission folder, I initially tried to enter `terminal-practice` as if I were still in the mission folder. The command failed because the repository root did not contain a folder by that name.

## 7. How I resolved them
I checked the directory with `pwd`, returned to `mission-02-terminal`, and then entered `terminal-practice`. The practice files were kept inside the repository and moved into the correct mission folder before committing.

## 8. Evidence / files
- `terminal-practice/practice/notes.txt` — two lines demonstrating append behavior.
- `terminal-practice/practice/notes-backup.txt` — copied backup.
- `terminal-practice/practice/moved-and-renamed.txt` — renamed copy.
- `terminal-practice/practice/empty.txt` — zero-byte file.
- `terminal-practice/practice/.hidden-demo` — hidden-file example.

## 9. Commit details
Commit message: `Complete Terminal and file management mission`. The completed mission was pushed to the public GitHub repository.
