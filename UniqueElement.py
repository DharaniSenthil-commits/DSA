# Write a program to Print Unique Elements in Array
#
# Sample Output
#
# Array = {10, 20, 40, 20, 10}
#
# Display Array Unique Elements= {10,20,40}

def UniqueElements(GivenArray):
    UniqueArray=[]
    for i in range(len(GivenArray)):
        if GivenArray[i] not in UniqueArray :
            UniqueArray.append(GivenArray[i])

    return UniqueArray


GivenArray=[10,20,40,20,10]
print(set(GivenArray))

print(UniqueElements(GivenArray))