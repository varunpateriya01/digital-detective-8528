# Mission 1 — Know your computer

## 1. Mission title
Mission 1 — Know your computer

## 2. Task / objective
Explain the input, processing, output and storage stages in a computer activity. Identify hardware, software and other computer systems.

## 3. Work completed
I used Terminal to create a short text file, displayed it, and checked its size. The file contains 87 bytes. I traced the activity with the IPOS model and listed examples of hardware, software and everyday computer systems.

### IPOS example: creating and reading a text note

| Stage | What happened | Component involved |
|---|---|---|
| Input | I supplied the sentence as text to a file-writing command. | Keyboard/input stream and Terminal |
| Processing | The shell and operating system passed the text to the file system and wrote its bytes. | CPU, memory and operating system |
| Output | `cat` displayed the saved sentence in Terminal. | Terminal window and display |
| Storage | The text remained in `activity-note.txt` after the command finished. | Internal storage drive |

### Hardware and software examples

| Item | Type | Software category | Purpose |
|---|---|---|---|
| Keyboard | Hardware | — | Sends text and commands into the computer. |
| Display | Hardware | — | Shows text and program output. |
| CPU | Hardware | — | Executes instructions and processes data. |
| SSD | Hardware | — | Keeps files when power is off. |
| macOS | Software | Operating system | Manages hardware, files, memory and applications. |
| Safari | Software | Application | Opens websites and web applications. |
| TextEdit | Software | Application | Creates and edits text documents. |
| Disk Utility | Software | Utility | Checks and manages storage volumes. |

### Computer systems in everyday life

| System | Main purpose | One input | One output |
|---|---|---|---|
| ATM | Provides banking services | Card and PIN | Cash or transaction message |
| Traffic signal controller | Controls traffic flow | Vehicle or pedestrian sensor | Traffic light changes |
| Ticket machine | Sells travel or event tickets | Destination or seat selection | Ticket or receipt |

## 4. Commands / tools used
- Terminal shell — created the text file inside the assignment repository.
- `cat mission-01-computer-basics/activity-note.txt` — displayed the saved sentence.
- `wc -c < mission-01-computer-basics/activity-note.txt` — counted the file's bytes and returned `87`.

## 5. My understanding
IPOS is a useful way to describe what happens to information. Input supplies data, the processor and operating system handle it, output presents a result, and storage keeps information for later. In this example, the sentence was still in the file after the Terminal command ended, so it had been stored rather than only displayed temporarily.

## 6. Difficulties faced
No major difficulties.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- `activity-note.txt` — the saved sentence used in the IPOS example.
- `README.md` — completed tables and explanation.

## 9. Commit details
Commit message: `Complete computer basics and IPOS mission`. The completed mission was pushed to the public GitHub repository.
