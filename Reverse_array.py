#Write a program to read n number of values in an array and display in reverse order


N=int(input("Enter a length of array"))
TestArray = []
for i in range(N):
    TestArray.append(int(input("Enter a value for array")))

#Brute Force
for i in range(N-1,-1,-1) :
     print(TestArray[i])

#Creating Another array
OutputArray=[]
for i in range(N-1,-1,-1):
    OutputArray.append(TestArray[i])

print(OutputArray)

#Swapping

for i in range(0,int(N/2)) :
    temp=TestArray[i]
    TestArray[i]=TestArray[N-1-i]
    TestArray[N-1-i]=temp

print(TestArray)

