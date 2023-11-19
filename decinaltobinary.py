import math
def decimal_to_binary (num):
    i=0
    binaryNum = 0
    while (num>=1):
        binaryNum+= (num%2)*(pow(10,i))
        i+=1
        num= math.floor(num/2)
    return binaryNum

def complement_to_two(binaryNum):
    carry=1
    complement=''.join(['1' if i=='0' else '0' for i in binaryNum])
    for i in range(len(complement)):
        i = len(complement) -1 - i
        if complement[i]=='0':
            complement= complement[:i] + '1' + complement[i+1:]
            return complement
        else:
            complement= complement[:i] + '0' + complement[i+1:]
    return complement

num= int(input("please enter a dicimal number"))
dataSize= int(input("please enter memory size"))   

binaryNum= str(decimal_to_binary(num))
complementTwo= complement_to_two(binaryNum.zfill(dataSize))
print("the binary number after applying the 2's cimplement is: " , complementTwo)
