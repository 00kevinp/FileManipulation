######################################
# Kevin Pickelman                    #
# CMSC 498 -- Programming Project 1  #
# Dr. Girard                         #
# 01/24/2025                         #
######################################



# Cornerstone of editng entries in the file, gets the entry number and the component to edit,
# also shows the user the entry they wish to edit before proceeding.
# If this was a larger scaled project, obviously more features such as a "go back" option would be added
# once the user sees the entry they wish to edit.
def entryEditInfo():
    newValue = ""
    entryNumber = int(input("Enter the entry number you want to edit: "))
    # try/except block to handle invalid entry numbers
    try:
        with open('fun.dat', 'r') as funFile:
            lines = [line for line in funFile.readlines() if line.strip()]
            entryIndex = entryNumber - 1
            entry = lines[entryIndex].strip().split(': ')[1].split(',')
            print(f"Entry to be edited: {entry}")
    except IndexError:
        print("Invalid entry number. Please try again.")
        return None, None, None
    toEdit = input("Enter the component you want to edit: COLOR, ZIP, STATE\n").upper()
    if toEdit not in ["COLOR", "ZIP", "STATE"]:
        print("Invalid entry. Please try again.")
        return None, None, None
    newValue = input(f"Enter the new value for {toEdit}: ")
    return entryNumber, toEdit, newValue


# Main driver function for actually making the edits to the file.
# Takes the entry number, the component to edit, and the new value for that component
# and decides where to overwrite that new data to.
# Pretty weak error handling here, just bare bones.
def editEntries(entryNumber, toEdit, newValue):
    if entryNumber is None or toEdit is None or newValue is None:
        return
    with open('fun.dat', 'r') as funFile:
        funFile.seek(0)
        lines = [line for line in funFile.readlines() if line.strip()]
        numLines = len(lines)
        if numLines < entryNumber or entryNumber < 1:
            print("Invalid entry number. Please try again.")
            # **important** in case the user enters an invalid entry number

        entryIndex = entryNumber - 1
        entry = lines[entryIndex].strip().split(': ')[1].split(',')
        if toEdit == "COLOR":
            entry[0] = newValue[:8].ljust(8, ' ')
        elif toEdit == "ZIP":
            entry[1] = newValue[:5].ljust(5, '0')
        elif toEdit == "STATE":
            newValue = newValue.upper()
            entry[2] = newValue[:2].ljust(2, ' ')
        else:
            print("Invalid entry. Please try again.")
            return

        lines[entryIndex] = f"{entryNumber}: {','.join(entry)}\n"

        # writing the new data to the file
        with open('fun.dat', 'w') as funFile:
            funFile.writelines(lines)
            funFile.truncate()





