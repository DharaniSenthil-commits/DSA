#Given a sorted array, return the index of a given value, or -1 if the element cannot be found.

N=int(input("Enter a length of array : "))
TestArray = []
for i in range(N):
    TestArray.append(int(input("Enter a value for array : ")))

SearchElement=int(input("Enter search Element : "))

def searchElementFunction(TestArray,SearchElement,N) :

    low=0
    high=N

    while(low<high):
        mid = int((low+high)//2)
        if TestArray[mid] == SearchElement :
            return mid
        elif (TestArray[mid] < SearchElement) :
            low=mid+1
        else :
            high=mid-1
    return -1

print(searchElementFunction(TestArray,SearchElement,N))




