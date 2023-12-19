#DSA Zero to Mastery

#Array
#An array is a powerful data structure that allows users to store and manipulate a collection of elements, all of the same data type in a single variable. Simply, it is a collection of elements of the same data type stored at contagious memory locations that can be randomly accessed with their index number

import array
arr=array.array("i",[1,2,3,4,5])
print(arr)


class ArrayExample:
    def __init__(self):
        # declaring the array of type int and size 4
        self.a = [1, 2, 5, 6]

        # declaring the array of type char and size 3
        self.b = ['a', 'b', 'c']

        # declaring the array of type float and size 5
        self.c = [0.2, 0.7, 0.8, 0.21, 0.9]

    def display_elements(self):
        # accessing the 2nd element of array a
        print(self.a[1])

        # accessing the elements of array b
        for i in range(3):
            print(self.b[i])

        # accessing the 3rd element of array c
        print(self.c[2])

# Create an instance of the ArrayExample class and display elements
array_example = ArrayExample()
array_example.display_elements()

fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

for fruit in fruits:
    print(fruit)

