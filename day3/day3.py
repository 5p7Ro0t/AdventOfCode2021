#The code may look messy or lengthly to you. If you have better code than this, please share with me or raise an issue here on Github :) Thanks

#--- Day 3: Binary Diagnostic ---

data = open("input.txt","r")
data_list = data.readlines()

#Part1
#--------------------------------------------------------------------------------------

length = len(data_list[0].strip())
gamma_rate,epsilon_rate,count_one,count_zero='0','0',0,0
# print(  " : ", length)
for i in range(length):
    for bit in data_list:
        # print("Testing")
        value = int(bit[i])
        # print(bit[i]," : ",value)
        if(value == 1):
            count_one+=1
        else:
            count_zero+=1
    if(count_one>count_zero):
        gamma_rate = gamma_rate+'1'
        epsilon_rate = epsilon_rate+'0'
        # print("Testing if")
    else:
        # print("Testing else")
        gamma_rate = gamma_rate+'0'
        epsilon_rate = epsilon_rate+'1'
    count_one,count_zero=0,0

#Result - 1
print("Submarine's Power Consumption is : " ,int(gamma_rate,2)*int(epsilon_rate,2))


#Part2
#---------------------------------------------------------------------------------------

oxygen_rating,co_rating = '0','0'
list_oxygen= list(data_list)
list_co=list(data_list)


def calculate(array,index,data):
    # print(index, " ; ",data)
    for i in range(len(array)):
        for j in array:
            if(j[index]==data):
                array.remove(j)
                # print(array)
            # print("Removed : ", i)


def oxygen(list_oxygen,count_one,count_zero):
    for i in range(length):
        # print(len(list_oxygen))
        for bit in list_oxygen:
            value = int(bit[i])
            if(value == 1):
                count_one+=1
            else:
                count_zero+=1
        if(count_one>count_zero):
            calculate(list_oxygen, i,'0')
        elif(count_one==count_zero):
            calculate(list_oxygen,i,'0')
        else:
            calculate(list_oxygen,i,'1')
        count_one,count_zero=0,0

    return list_oxygen
res_oxy = oxygen(list_oxygen,count_one,count_zero)

print("----------------------------------------------------")

def co(list_co,count_one,count_zero):
    for j in range(length):
        if(len(list_co)==1):
            # print("breaked")
            break
        # print(len(list_co))
        for bit in list_co:
            value = int(bit[j])
            if(value == 1):
                count_one+=1
            else:
                count_zero+=1
        if(count_one>count_zero):
            calculate(list_co, j,'1')
        elif(count_one==count_zero):
            calculate(list_co,j,'1')
        else:
            calculate(list_co,j,'0')
        count_one,count_zero=0,0
    return list_co

res_co = co(list_co,count_one,count_zero)

# Result - 2

print("The life support rating of the submarine is : ",int(res_oxy[0],2)*int(res_co[0],2))
    
