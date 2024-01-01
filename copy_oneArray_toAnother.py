#Write a program in to copy the elements of one array into another array

LengthOfArray=int(input("Enter Length of Array"))

TestArray=[]

for i in range(LengthOfArray):
    TestArray.append(int(input("Enter Array Element :")))


OutputArray=[]

for i in range(LengthOfArray):
    OutputArray.append(TestArray[i])

print(OutputArray)


destination_array = [0] * LengthOfArray
print(destination_array)
for i in range(LengthOfArray):
    destination_array[i]=TestArray[i]

print(destination_array)
