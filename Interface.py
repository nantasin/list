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
    print("B: Print thr team list")
    print("X Exit the program")
    choice = input("Exter yoer choice: ")
    if choice == "A":
    name = input("Enter a name: ")
    teamlist.append(name) 
print(teamlist)