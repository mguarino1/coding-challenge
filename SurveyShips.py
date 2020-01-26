#Michael Guarino
#StratumFive Coding Challenge

#Open input and output files
rf = open("SampleInput.txt", "r")
wf = open("Output.txt", "w")
#Grabs first line to create grid bounds
x, y = rf.readline().split(" ")

x = int(x)
y = int(y)

#Puts all ship positions and commands into list, removes line spacing
ships = rf.readlines()
for i in range(len(ships)-1):
    ships[i] = ships[i].strip()

#Directions
N=0
E=1
S=2
W=3

#Reference for moves that have been marked as invalid
invalidMoves = []

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
 
    curCommands = ships.pop(0).strip()
    lost = False
    
    for c in curCommands:
        #Turn left
        if c is 'L':
            shipDir = (shipDir-1)%4
        #Turn right
        elif c is 'R':
            shipDir = (shipDir+1)%4
        #Move forward
        elif c is 'F':
            #Ignores move if it's invalid
            if [curX,curY,shipDir] not in invalidMoves:
                #Moves ship in appropriate direction or marks the ship
                #as lost and records the invalid move if ship goes
                #off the edge
                if shipDir == N:
                    if curY == y:
                        lost = True
                        invalidMoves.append([curX,curY,shipDir])
                    else:
                        curY+=1          
                elif shipDir == E:
                    if curX == x:
                        lost = True
                        invalidMoves.append([curX,curY,shipDir])
                    else:
                        curX+=1
                elif shipDir == S:
                    if curY == 0:
                        lost = True
                        invalidMoves.append([curX,curY,shipDir])
                    else:
                        curY-=1
                else:
                    if curX == 0:
                        lost = True
                        invalidMoves.append([curX,curY,shipDir])
                    else:
                        curX-=1
        #If a ship falls off the edge, ignore the rest of the commands                
        if lost:
            break
    #Changes directions back to characters for output purposes
    if shipDir == 0:
        shipDir = 'N'
    elif shipDir == 1:
        shipDir = 'E'
    elif shipDir == 2:
        shipDir = 'S'
    else:
        shipDir = 'W'
    #Writes the result of each ship to the file     
    if lost:
        print(curX,curY,shipDir,'LOST', file=wf)
    else:
        print(curX,curY,shipDir, file=wf)

rf.close()
wf.close()
    



