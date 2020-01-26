#Michael Guarino
#StratumFive Coding Challenge

rf = open("SampleInput.txt", "r")
x, y = rf.readline().split(" ")

grid = [['0' for col in range(int(x))] for row in range(int(y))]

wf = open("Output.txt", "w")

