import os
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QLabel

# variables needed for the backup/import process 
saves_list = os.listdir("./backups/") 
default_save_location = os.path.expanduser("~/AppData/Local/GeometryDash/")
save_location = ""
save_choice = ""
app = QApplication([])

# pyqt
def mwindow():
    window = QWidget()
    vlayout = QVBoxLayout()
    hlayout = QHBoxLayout()
    listWidget = QListWidget()
    backupbutton = QPushButton('Backup Local Save')
    window.setLayout(vlayout)

    vlayout.addWidget(QLabel('Welcome to the Geometry Dash Save File Backup Manager!'))

    for value in saves_list:
        listWidget.addItem(value)
    vlayout.addWidget(listWidget)

    vlayout.addLayout(hlayout)

    hlayout.addWidget(backupbutton)
    hlayout.addWidget(QPushButton('Import Backup to Game'))

    window.show()

mwindow()
"""
while True:
    print("What would you like to do?")
    print("- Backup local save (1)")
    print("- Import backup to game (2)")
    print("- Exit (0)")
    print("?: ", end='')
    menu_choice = input("")

    if menu_choice == "1":

        # 1. Detection of save location
        if os.path.exists(default_save_location):
            print('Local save is detected.')
            save_location = default_save_location
        else:
            while True:
                print('Local save is not detected. Where is your save located?')
                custom_save_location = input("")
                print("Is this path correct?" + "'" + str(custom_save_location) + "'" + "(y/n)")
                save_confirmation = input("")
                if save_confirmation == "y":
                    print("Confirmed.")
                    save_location = custom_save_location
                    break
                if save_confirmation == "n":
                    print("Okay. Feel free to change the directory.")
                else:
                    continue
        
        # 2. Give user option to rename 
        print("What would you like to name the save backup?")
        print("Name: ", end='')
        backup_name = input("")


        # 3. Create a folder called rawsaves in cache
        os.mkdir("./cache/rawsaves/") 

        # 4. Copy the save files in the rawsaves folder
        shutil.copy(save_location + "CCGameManager.dat", "./cache/rawsaves/")
        shutil.copy(save_location + "CCGameManager2.dat", "./cache/rawsaves/")
        shutil.copy(save_location + "CCLocalLevels.dat", "./cache/rawsaves/")
        shutil.copy(save_location + "CCLocalLevels2.dat", "./cache/rawsaves/")

        # 5. Zip the rawsaves folder
        shutil.make_archive('./cache/rawsaves', 'zip', './cache/rawsaves')

        # 6. Rename the rawsaves.zip folder into backup_name.
        os.rename("./cache/rawsaves.zip", "./backups/" + backup_name + ".gdsave")

        # 7. Remove the rawsaves folder
        shutil.rmtree("./cache/rawsaves")

        # 8. Check if the file has successfully been created. If true, confirm.
        if os.path.exists( "./backups/" + backup_name + ".gdsave"):
            print("Save has successfully been backed up!")
        else:
            print("Backup failed to create!")


        time.sleep(3)

        
    
    elif menu_choice == "2":

        print("Note: Make sure that you have backed up your current save already, as this WILL overwrite whatever save the game is using right now.")
        print("Proceed? (y/n)")
        proceed_choice = input("")

        if proceed_choice == "y":


            # 1. Detection of save location
            if os.path.exists(default_save_location):
                print('Local save is detected.')
                save_location = default_save_location
            else:
                while True:
                    print('Local save is not detected. Where is your save located?')
                    custom_save_location = input("")
                    print("Is this path correct?" + "'" + str(custom_save_location) + "'" + "(y/n)")
                    save_confirmation = input("")
                    if save_confirmation == "y":
                        print("Confirmed.")
                        save_location = custom_save_location
                        break
                    if save_confirmation == "n":
                        print("Okay. Feel free to change the directory.")
                    else:
                        continue
            
            # 2. User chooses a save file in ./backups/

            while True:
    
                print("What save would you like to import?")
                for value in saves_list:
                    print("- '" + value + "'")
                print("")
            
                save_choice = input("")

                # 3. Grab the file with save_choice. Loop the code if the save does not exist
                if os.path.exists("./backups/" + save_choice + ".gdsave"):
                    print("yay you have the save")
                    break
                else:
                    print("Save does not exist. Try again.")
                    time.sleep(1)
                    continue

            # 3. Copy the file in cache, and rename the file extension part of the backup from gdsave to zip
            shutil.copy("./backups/" + save_choice + ".gdsave", "./cache/")
            os.rename("./cache/" + save_choice + ".gdsave", "./cache/import.zip")

            # 4. Unzip the .zip in ./cache/
            os.mkdir("./cache/import") 
            shutil.unpack_archive("./cache/import.zip", './cache/import', 'zip')  

            # 5. Remove the old save contents from the Geometry Dash save_location
            if os.path.exists(save_location + "CCGameManager.dat") and os.path.exists(save_location + "CCLocalLevels.dat"):
                os.remove(save_location + "CCGameManager.dat")
                os.remove(save_location + "CCLocalLevels.dat")
            else:
                print("The files do not exist. Continuing.")
                time.sleep(2)
            
            # 6. Copy the unzipped save contents into the Geometry Dash save_location

            shutil.copy("./cache/import/CCGameManager.dat", save_location)
            shutil.copy("./cache/import/CCLocalLevels.dat", save_location)
            
            # 7. Remove all the contents in ./cache/

            shutil.rmtree("./cache/import")
            os.remove("./cache/import.zip")

            # 8. Check if the file has successfully been created. If true, confirm.
            if os.path.exists(save_location + "CCGameManager.dat") and os.path.exists(save_location + "CCLocalLevels.dat"):
                print("Save has successfully been imported!")
            else:
                print("Backup failed to import!")

            time.sleep(3)
    elif menu_choice == "0":
        break
"""
