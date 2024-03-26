# Geometry Dash Save Manager
A python program that automates backing your CCGameManager and CCLocalLevels up for you in a neat gdsave (zip) file.

Dependencies:
PyQt5 - For the GUI. Not required for the cmd version.

## Setup
Assuming you have python3 already, create a virual environment in your current directory:

```
python3 -m venv venv
```
Activate the virtual environment:
```
- On Mac or Linux:
source venv/bin/activate
- On Windows:
call venv\scripts\activate.bat
```
And install the library (if you do not currently have PyQt5).
```
pip install PyQt5
```
After that, the appication is set up you should be ready to activate the application.
```
/bin/python3 (whatever directory you cloned the repository in)/gd-save-manager/gdsm_gui.py
```
