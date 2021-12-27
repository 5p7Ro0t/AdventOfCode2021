#--- Day 2: Dive! ---

file = open("input.txt",'r')
commands = file.readlines()
depth,position,aim=0,0,0

# Part1
for i in commands:
    i=i.strip()
    command_number = int(i[-1])
    # print(command_number)
    if(i.find('forward') == 0):
        position+=command_number
    elif(i.find('up')==0):
        depth-=command_number
    else:
        depth+=command_number
print("Part 1 Answer : ",depth*position)

#Part2
depth,position=0,0
for i in commands:
    i=i.strip()
    command_number = int(i[-1])
    # print(command_number)
    if(i.find('forward') == 0):
        position+=command_number
        depth=depth+(aim*command_number)
    elif(i.find('up')==0):
        aim-=command_number
    else:
        aim+=command_number
print("Part 2 Answer : ",depth*position)