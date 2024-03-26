import os
import shutil
import sys
import time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QLabel, QLineEdit,QGroupBox

# variables needed for the backup/import process 
saves_list = os.listdir("./backups/") 
default_save_location = os.path.expanduser("~/AppData/Local/GeometryDah/")
default_save_location_linux = os.path.expanduser("~/.local/share/Steam/steamapps/compatdata/322170/pfx/drive_c/users/steamuser/AppData/Local/GeometryDash/")
save_location = ""
save_choice = ""

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.hlayout = QHBoxLayout()
        self.vlayout = QVBoxLayout()
        savegroupbox = QVBoxLayout()
        self.setLayout(self.vlayout)
        self.setFixedWidth(420)

        groupbox = QGroupBox("Saves:")
        groupbox.setLayout(savegroupbox)

        self.welcome = QLabel(self)
        self.welcome.setText("Welcome to the Geometry Dash Save File Manager! \n\nA program that automates backing your CCGameManager and CCLocalLevels up for you in a neat gdsave (zip) file.")
        self.welcome.setWordWrap(True)

        self.madeby = QLabel(self)
        self.madeby.setText("made by sushiwt, 2024     Geometry Dash belongs to RobTop")
        self.madeby.setAlignment(QtCore.Qt.AlignCenter)

        self.b1 = QPushButton(self)
        self.b1.setText("Backup Local Save")
        self.b1.clicked.connect(self.backupbtn)

        self.b2 = QPushButton(self)
        self.b2.setText("Import Backup to Game")
        self.b2.clicked.connect(self.importbtn)

        self.listWidget = QListWidget()
        for value in saves_list:
            self.listWidget.addItem(value.replace(".gdsave", "", 1))

        self.vlayout.addWidget(self.welcome)

        self.vlayout.addWidget(groupbox)
        savegroupbox.addWidget(self.listWidget)

        self.vlayout.addLayout(self.hlayout)
        self.hlayout.addWidget(self.b1)
        self.hlayout.addWidget(self.b2)
        self.vlayout.addWidget(self.madeby)

        self.center()
        self.show()

    def backupbtn(self):
        self.bkupwin = BackupWindow()
        self.bkupwin.show()
    
    def importbtn(self):
        self.iprtwin = ImportWindow()
        self.iprtwin.show()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

class BackupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        altlayout = QHBoxLayout()
        self.setLayout(layout)
        self.setFixedWidth(360)
        self.savedetectlabel = QLabel(self)
        self.savedetectlabel.setWordWrap(True)

        if os.path.exists(default_save_location):
            self.savedetectlabel.setText("Local save (Windows) is detected. \n" + default_save_location + "\nYou don't have to input your custom path.")
        elif os.path.exists(default_save_location_linux):
            self.savedetectlabel.setText("Local save (Linux) is detected. \n" + default_save_location_linux + "\nYou don't have to input your custom path.")
        else:
            self.savedetectlabel.setText("Local save is not detected. \nWhat path are your saves in?")
            self.customsavepath = QLineEdit(self)
            layout.addWidget(self.customsavepath)

        self.namelabel = QLabel("What would you like to name the save backup?")
        self.savname = QLineEdit(self)

        self.confirmbtn = QPushButton(self)
        self.confirmbtn.setText("Confirm")
        self.confirmbtn.clicked.connect(self.backupsave)
        
        layout.addWidget(self.savedetectlabel)
        layout.addWidget(self.namelabel)

        layout.addLayout(altlayout)
        altlayout.addWidget(self.savname)
        altlayout.addWidget(self.confirmbtn)

        self.center()

    def backupsave(self):
        if os.path.exists(default_save_location):
            save_location = default_save_location
        elif os.path.exists(default_save_location_linux):
            save_location = default_save_location_linux
        else:
            save_location = self.customsavepath.text()

        os.mkdir("./cache/rawsaves/") 

        shutil.copy(save_location + "CCGameManager.dat", "./cache/rawsaves/")
        shutil.copy(save_location + "CCGameManager2.dat", "./cache/rawsaves/")
        shutil.copy(save_location + "CCLocalLevels.dat", "./cache/rawsaves/")
        shutil.copy(save_location + "CCLocalLevels2.dat", "./cache/rawsaves/")

        shutil.make_archive('./cache/rawsaves', 'zip', './cache/rawsaves')

        os.rename("./cache/rawsaves.zip", "./backups/" + self.savname.text() + ".gdsave")

        shutil.rmtree("./cache/rawsaves")

        if os.path.exists( "./backups/" + self.savname.text() + ".gdsave"):
            print("Save has successfully been backed up!") 
            self.m = SuccessWindow()
            self.m.show()
        else:
            print("Backup failed to create!")
            time.sleep(3)
            os.execl(sys.executable, sys.executable, *sys.argv) 

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

class ImportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        altlayout = QHBoxLayout()
        self.setFixedWidth(320)
        self.setLayout(layout)
        self.savedetectlabel = QLabel(self)
        self.savedetectlabel.setWordWrap(True)

        if os.path.exists(default_save_location):
            self.savedetectlabel.setText("Local save (Windows) is detected. \n" + default_save_location + "\nYou don't have to input your custom path.")
        elif os.path.exists(default_save_location_linux):
            self.savedetectlabel.setText("Local save (Linux) is detected. \n" + default_save_location_linux + "\nYou don't have to input your custom path.")
        else:
            self.savedetectlabel.setText("Local save is not detected. \nWhat path are your saves in?")
            self.customsavepath = QLineEdit(self)
            layout.addWidget(self.customsavepath)

        self.namelabel = QLabel("Note: Make sure that you have backed up your current save already, as this WILL overwrite whatever save the game is using right now. (but just in case, this program will leave out the CCGameManager2 and CCLocalLevels2 dat files.) \n\nWhat save would you like to import?")
        self.namelabel.setWordWrap(True)
        self.savname = QLineEdit(self)

        self.confirmbtn = QPushButton(self)
        self.confirmbtn.setText("Confirm")
        self.confirmbtn.clicked.connect(self.backupsave)

        self.listWidget = QListWidget()
        for value in saves_list:
            self.listWidget.addItem(value.replace(".gdsave", "", 1))
        
        layout.addWidget(self.savedetectlabel)
        layout.addWidget(self.namelabel)
        layout.addWidget(self.listWidget)

        layout.addLayout(altlayout)
        altlayout.addWidget(self.savname)
        altlayout.addWidget(self.confirmbtn)

        self.center()

    def backupsave(self):
        if os.path.exists("./backups/" + self.savname.text() + ".gdsave"):
            if os.path.exists(default_save_location):
                save_location = default_save_location
            elif os.path.exists(default_save_location_linux):
                save_location = default_save_location_linux
            else:
                save_location = self.customsavepath.text()

            shutil.copy("./backups/" + self.savname.text() + ".gdsave", "./cache/")
            os.rename("./cache/" + self.savname.text() + ".gdsave", "./cache/import.zip")

            os.mkdir("./cache/import") 
            shutil.unpack_archive("./cache/import.zip", './cache/import', 'zip')  

            if os.path.exists(save_location + "CCGameManager.dat") and os.path.exists(save_location + "CCLocalLevels.dat"):
                os.remove(save_location + "CCGameManager.dat")
                os.remove(save_location + "CCLocalLevels.dat")
            else:
                print("The files do not exist. Continuing.")
                time.sleep(2)

            shutil.copy("./cache/import/CCGameManager.dat", save_location)
            shutil.copy("./cache/import/CCLocalLevels.dat", save_location)

            shutil.rmtree("./cache/import")
            os.remove("./cache/import.zip")

            if os.path.exists( "./backups/" + self.savname.text() + ".gdsave"):
                self.m = SuccessWindow()
                self.m.show()
            else:
                print("Backup failed to create!")
                time.sleep(3)
                os.execl(sys.executable, sys.executable, *sys.argv) 
        else:
            self.fileExists = FileExistsWindow()
            self.fileExists.show()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

class SuccessWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.namelabel = QLabel("The task was a success! \nPress the Confirm button to restart the application.")
        layout.addWidget(self.namelabel)

        self.confirmbtn = QPushButton(self)
        self.confirmbtn.setText("Confirm")
        self.confirmbtn.clicked.connect(self.restartpr)
        layout.addWidget(self.confirmbtn)

        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def restartpr(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

class FileExistsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.namelabel = QLabel("Save does not exist.")
        layout.addWidget(self.namelabel)

        self.confirmbtn = QPushButton(self)
        self.confirmbtn.setText("Close")
        self.confirmbtn.clicked.connect(lambda:self.close())
        layout.addWidget(self.confirmbtn)

        self.center()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

# pyqt
def mwindow():
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())

mwindow()