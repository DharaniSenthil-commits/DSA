#Write a program to search an element in an array

N=int(input("Enter a length of array : "))
TestArray = []
for i in range(N):
    TestArray.append(int(input("Enter a value for array : ")))

SearchElement=int(input("Enter search Element : "))

#BruteForce

for i in range(N):
    if TestArray[i] == SearchElement :
        print("Element is there at :" + str(i+1)+" position")
    else :
        print("Element is not there")

if SearchElement in TestArray :
    print("Search Element is available")
else :
    print("Search element is not available")