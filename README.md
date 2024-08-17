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
| `add-tag title tag`                               | Add tag to note                       |
| `delete-contact name`                             | Delete contact by name                |
| `delete-note title`                               | Delete note by title                  |
| `delete-tag title tag`                            | Delete tag from note                  |
| `edit-contact name fieldname field`               | Edit contact                          |
| `edit-note title newtitle newdescription newtags` | Edit note                             |
| `find-contacts parameter`                         | Find contacts by any parameter        |
| `find-note title`                                 | Find note by title                    |
| `find-note-by-tag tag`                            | Find note by tag                      |
| `show-contacts`                                   | Show all contacts                     |
| `show-contacts-upcoming-birthdays days`           | Get contacts with birthdays in n days |
| `show-notes`                                      | Show all notes                        |
| `show-notes-by-tags`                              | Show notes sorted by tags             |
| `close`, `exit`                                   | Close application                     |
| `help`                                            | Get list of commands                  |
## FAQ
### How to add contact if name or address containing more than 1 word?
Use quotes to add contact with name or address containing more than 1 word. Example:

`add-contact "John Doe" "New York" 1234567890 email@gmail.com 01.01.2000`

### What is the data format for birthday?
Use format `DD.MM.YYYY`. Example:

`add-contact "John Doe" "New York" 1234567890 email@gmail.com 01.01.2000`

### How to add note if I have more than 1 tag?
Use quotes and separate tags by comma. Example:
`add-note "My note" "Very important noe" "tag1,tag2"`