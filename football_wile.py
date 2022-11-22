football_team = []
repeat = "Y"
while repeat == "Y":
    name = input("Enter the player's name: ")
    football_team.append(name)
    repeat = input("do you want to ente anothr namr(Y/N): ")
print(football_team)