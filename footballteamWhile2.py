football_team = []

#TO-OO: append 11 players with for loop, ask user for player's name
for i in range(11):
    name = input("Add a player to the football team: ")
    football_team.append(name)
print(football_team)    

repeat = "Y"
while repeat =="Y"
    edit = int(input("Which player do you want to change "))
    football_team[edit-1] = input("Enter a new player: ")
    
    delete = int(input("Which player do you want to delete"))
    del football_team[delete-1]

    repeat = input("Do you want to adit more?(Y/N")
    print(football_team)
    