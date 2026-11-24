# Mission 3 — Understand the operating system

## 1. Mission title
Mission 3 — Understand the operating system

## 2. Task / objective
Inspect operating-system details, account context, storage, running processes, paths and file permissions, then explain the OS responsibilities.

## 3. Work completed
I checked the operating system and storage from Terminal, redacted the active account name, and opened Activity Monitor to inspect running processes. Terminal did not allow the process-list command in this environment, so I used Activity Monitor instead. I compared the permission string on a practice file and wrote a privacy-safe summary.

| Information explored | What it tells me | Observation (privacy-safe) |
|---|---|---|
| Operating system | Which OS and release are running. | macOS 27.2.1. |
| Current account | Which local account owns this session. | Checked; the account name was redacted. |
| Storage | Space used and available on the project volume. | 460 GiB total; 92 GiB used; 344 GiB available (22% used) at the time checked. |
| System activity | Programs and background tasks currently running. | Activity Monitor showed application and system processes, including Finder and a Chrome helper. PIDs were not recorded. |

A process is a program that is currently executing. Activity Monitor displayed a PID column; each process has an identifier the operating system can use to distinguish it. Finder is an example of an application process, and a Chrome helper is an example of a supporting process.

### Paths and permissions

An absolute path starts at the filesystem root and identifies one location independently of the current directory. In this public report, the home-directory portion is redacted: `/Users/[redacted]/Documents/Codex/2026-11-24/ne/outputs/digital-detective-8528/mission-03-operating-system/README.md`. A relative path is interpreted from the current directory; from the repository root, `mission-03-operating-system/README.md` points to this file.

The practice file's permission string was `-rw-r--r--`. The owner can read and write it, but it is not executable. Group members and other users have read permission only. I did not change any permissions.

### Operating-system responsibilities

| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Starts programs and shares CPU time among active tasks. | Giving time to a browser and a text editor. |
| Memory management | Tracks RAM use and assigns memory to programs. | Keeping a document open while a browser runs. |
| Device management | Coordinates hardware through drivers and system services. | Sending a page to a printer. |
| File management | Organizes files and folders and handles saving and retrieval. | Saving a note in the mission folder. |
| User interface / shell | Provides ways for people and programs to control the computer. | Finder windows or Terminal commands. |
| Security and permissions | Controls accounts and which actions they may perform on files. | Allowing the owner to edit a file while others can only read it. |

## 4. Commands / tools used
- `sw_vers -productName` and `sw_vers -productVersion` — reported macOS and its version.
- `id -un` — checked the active account; the name was redacted and not saved.
- `df -h .` — reported storage totals; the filesystem and mount details were omitted.
- `ps -axo comm` — attempted to list processes in Terminal; macOS returned “operation not permitted.”
- Activity Monitor — inspected the process table and its PID column.
- `stat -f '%Sp' .../notes.txt` — returned `-rw-r--r--`.

## 5. My understanding
The operating system connects applications to the hardware and manages shared resources such as CPU time, memory, storage and devices. A process is one running instance of a program, and the PID helps the OS keep track of it. Paths locate files, while permissions describe which users may read, change or run them. System details can be useful for troubleshooting, but account names, process identifiers and filesystem details should be removed from public evidence.

## 6. Difficulties faced
The process-list command in Terminal was blocked with “operation not permitted.” The raw storage and account commands can also include details that should not be published.

## 7. How I resolved them
I opened Activity Monitor to view running processes, then recorded only application examples and noted that a PID column was present. I redacted the account name and omitted filesystem identifiers and mount paths from the evidence.

## 8. Evidence / files
- `system-observations.md` — privacy-safe OS, storage, process and permission observations.
- `../mission-02-terminal/terminal-practice/practice/notes.txt` — file used to inspect permissions.

## 9. Commit details
Commit message: `Document operating system and file management`. The completed mission was pushed to the public GitHub repository.
