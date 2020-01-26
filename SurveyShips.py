#Michael Guarino
#StratumFive Coding Challenge

#Open input file
rf = open("SampleInput.txt", "r")

#Grabs first line to create the grid
x, y = rf.readline().split(" ")
grid = [['0' for col in range(int(x))] for row in range(int(y))]

#Puts all ship positions and commands into list, removes line spacing
ships = rf.readlines()
for i in range(len(ships)-1):
    ships[i] = ships[i].strip()

while ships:
    #Removing blank lines from list
    if ships[0] == '':
        ships.pop(0)
    #Assumes ship position is first followed by ship instructions
    curShip = ships.pop(0).split(" ")
    curShip[0] = int(curShip[0])
    curShip[1] = int(curShip[1])
    curCommands = ships.pop(0)




wf = open("Output.txt", "w")

