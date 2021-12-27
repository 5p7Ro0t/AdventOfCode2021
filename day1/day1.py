#--- Day 1: Sonar Sweep ---

data = open("input.txt","r")
previous_depth,count,previous_sum,sum = 0,0,0,0
list = data.readlines()

#Part1
for i in list:
    i = int(i)
    if(previous_depth == 0):
        #print(i, "(N/A - no previous measurement)") 
        pass
    elif(i > previous_depth):
        count+=1
        #print(i,"(INCREASED)" , "count : ",count)
    else:
        #print(i, "(decreased)", "count : ",count)
        pass
    previous_depth = i
print("Count : " , count)

#Part2
count=0
for i in range(len(list)-2):
    sum = int(list[i])+int(list[i+1])+int(list[i+2])
    if(previous_sum==0):
        #print(sum, " (N/A - no previous sum)")
        pass
    elif(sum>previous_sum):
        count+=1
        #print(sum, " (INCREASED)")
        pass
    else:
        pass
    previous_sum=sum
print("Count of Sums : ",count)

