#Michael Guarino
#StratumFive Coding Challenge

#Open input file
rf = open("SampleInput.txt", "r")

#Grabs first line to create the grid
x, y = rf.readline().split(" ")
grid = [['0' for col in range(int(x)+1)] for row in range(int(y)+1)]

#Puts all ship positions and commands into list, removes line spacing
ships = rf.readlines()
for i in range(len(ships)-1):
    ships[i] = ships[i].strip()

N=0
E=1
S=2
W=3

while ships:
    #Removing blank lines from list
    if ships[0] == '':
        ships.pop(0)
    #Assumes ship position is first followed by ship instructions
    curShip = ships.pop(0).split(" ")
    curX = int(curShip[0])
    curY = int(curShip[1])
    shipDir = curShip[2]
    #Making direction values integers to make changing direction a bit simpler
    if shipDir is 'N':
        shipDir = N
    elif shipDir is 'E':
        shipDir = E
    elif shipDir is 'S':
        shipDir = S
    elif shipDir is 'W':
        shipDir = W
       
    curCommands = ships.pop(0)
    lost = False
    
    for c in curCommands:
            if c is 'L':
                shipDir = (shipDir+1)%4
            elif c is 'R':
                shipDir = (shipDir-1)%4
            else:
                if shipDir == N:
                    if curY == 3:
                        lost = True
                    else:
                        curY+=1          
                elif shipDir == E:
                    if curX == 5:
                        lost = True
                    else:
                        curX+=1
                elif shipDir == S:
                    if curY == 0:
                        lost = True
                    else:
                        curY-=1
                else:
                    if curX == 0:
                        lost = True
                    else:
                        curX-=1

    

wf = open("Output.txt", "w")

