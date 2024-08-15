## Installation
```bash
git clone https://github.com/Etyamor/goit-pycore-final.git
python -m venv .venv
```
Windows (cmd)
```bash
.\.venv\Scripts\activate.bat
```
Windows (PowerShell)
```bash
.\.venv\Scripts\Activate.ps1
```
Macos/Linux
```bash
source .venv/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
## Usage
```bash
python main.py
```
## Commands
| Command                                           | Description                           |
|---------------------------------------------------|---------------------------------------|
| `add-contact name address phone email birthday`   | Add contact                           |
| `add-note title description tags`                 | Add note                              |
| `show-contacts`                                   | Show all contacts                     |
| `show-notes`                                      | Show all notes                        |
| `delete-contact name`                             | Delete contact by name                |
| `delete-note title`                               | Delete note by title                  |
| `edit-note title newtitle newdescription newtags` | Edit note                             |
| `find-note title`                                 | Find note by title                    |
| `find-note-by-tag tag`                            | Find note by tag                      |
| `add-tag title tag`                               | Add tag to note                       |
| `delete-tag title tag`                            | Delete tag from note                  |
| `get-contacts-upcoming-birthdays days`            | Get contacts with birthdays in n days |
| `close`, `exit`                                   | Close application                     |
| `help`                                            | Get list of commands                  |
