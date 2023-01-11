#program interface sgoudl have all of these:
#1, Tall the user what the program is and what is can do
#2, Tall the user make choices or select option
#2, Let the user information -you shoulc include a helpful message
#4, Display result ror answer
#5, Let the user close the program

teamlist = []
choice = ' '
while choice != 'x':
    print("TEAM MANAGER")
    print("===============")
    print("This program will help you manage your team")
    print("\n")
    print("A: Append a value")
    print("B: Print thr list")
    print("C: Print an Element")
    print("D: Delete an Element")
    print("E: Edit an Elemet")
    print("F: Sort the list")
    print("X Exit the program")
    choice = input("Exter yoer choice: ")
    if choice == "A":
        name = input("Enter a name: ")
        teamlist.append(name) 
    if choice == "8":
        print(teamlist)
    if choice =="C":
        i = input("Which list item do you want to print")
        i = int(i)
        print(teamlist[i])
    if choice == "D":
        delete = int(xinput("Which item do oyu want to detele?;1 "))
        del teamlist[delete]
    if choice == "E":
        edit = int(input("which item do you want to edit?; "))
        teamlist[edit-1] = input("Enter a new item")
    if choice == "F":
        teamlist.sort()
        print(teamlist)
    if choice == "X":
        print("Exiting thr program")    