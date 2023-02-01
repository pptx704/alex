# Alex
A simple application for auto check-ins and check-outs on a Notion database.

# Usage
1. Clone the repository.
2. Install required libraries. Better if virtual environment is activated.
```
pip install -r requirements.txt
```
3. Have a `logo.png` file as icon. If there is no such file, a square will be drawn.
4. Copy `secrets_example.json` file to `secrets.py` and modify it with correct **database id** and Notion integration token.
5. Run `app.pyw`. The program considers its starting time as check-in time.


There are 4 options in the toolbar menu-
* **Quit without saving** - This will terminate the app without checking out on Notion.
* **Check In/Out** - Self explanatory
* **Reset** - Replaces the check-in time with the current time.
* **Quit** - Quits the application. Checks out if user is checked in.

# Todo
- [ ] Pop-up for getting the work title when checking out
- [ ] Add option for putting work summary