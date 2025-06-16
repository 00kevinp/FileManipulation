######################################
# Kevin Pickelman                    #
# CMSC 498 -- Programming Project 1  #
# Dr. Girard                         #
# 01/24/2025                         #
######################################

import fileEntry
import fileEditing

# The main driver function for the application, allows the user to decide what
# they'd like to do with the file. Firstly, y for yes, n for no, if the user
# wants to make any changes to the file. If yes, the user can choose to add a new
# entry(enter number 1), edit an existing entry(enter number 2),
# or exit the application(enter number 3).
def driver():
    changes = input("Do you want to make any changes to the file? (y/n)\n")
    while changes.lower() == "y":
        choice = input("New Entry or Edit Existing Entry?\nnew -> 1\nedit -> 2\nexit -> 3\n")
        if choice == "1":
            color, zip, state = fileEntry.getEntryInfo()
            fileEntry.writeToFile(color, zip, state)
        elif choice == "2":
            entryNumber, toEdit, newValue = fileEditing.entryEditInfo()
            fileEditing.editEntries(entryNumber, toEdit, newValue)
        elif choice == "3":
            break
        else:
            print("Invalid entry. Please try again.")
    print("Goodbye!")

def main():
    driver()


if __name__ == "__main__":
    main()