######################################
# Kevin Pickelman                    #
# CMSC 498 -- Programming Project 1  #
# Dr. Girard                         #
# 01/24/2025                         #
######################################


# Gathers the entry information from the user and returns it
def getEntryInfo():
    color = input("Enter a color: ")
    zip = input("Enter a zip code: ")
    state = input("Enter a state: ")
    return color, zip, state


# Writes the entry information to the file
def writeToFile(color, zip, state):
    with open('fun.dat', 'a+') as funFile:
        funFile.seek(0) # got this line from Copilot, it better work, UPDATE: it works and what it does is ensures that we begin reading from the beginning of the file
        lines = [line for line in funFile.readlines() if line.strip()]
        entryNumber = len(lines) + 1 if lines else 1 # if there are no lines in the file, the entry number is 1, otherwise it is the length of the lines + 1
        if zip.isdigit() and len(state) == 2 and state.isalpha():
            color = color[:8].ljust(8, ' ')
            #            ^^^^^^ Copilot taught me this handy ljust method
            state = state.upper()
            zip = zip[:5].ljust(5, '0')# if zip is less than 5, fill with zeros after the numbers entered
            infoList = { # dictionary is used for easy access to later edit information, also ensures that the info maintains its order
                "color" : color,
                "zip" : zip,
                "state" : state
            }
            funFile.write(f"{entryNumber}: {infoList['color']},{infoList['zip']},{infoList['state']}\n")
        #     write to the fun.dat file (funFile)
        else:
            print("Invalid input. Please try again.")

