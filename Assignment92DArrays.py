#   Program to make a 5 x 5 array that will be flipped both horizontally and vertically and printed each time.
#   Assignment 9: 2D Arrays
#   John Paul Cannon
#   11 - 16 - 21


# function to print out all the numbers in the arrays
def printArray(a):
    for r in range(len(a)):
        for c in range(len(a[0])):
            print(a[r][c], end=" ")
        print("")


# function to flip the array horizontally
def flipHorizontal(a):
    for r in range(len(a)):
        a[r].reverse()

    printArray(a)


# function to flip the array vertically
def flipVertical(a):
    j = len(a) - 1
    i = 0
    
    while(i <= j):
        a[i], a[j] = a[j], a[i]
        j -= 1
        i += 1
    printArray(a)


####****----MAIN----****####

# initializer list
array = [[0, 2, 0, 0, 0], [0, 2, 0, 0, 0], [0, 2, 2, 0, 0], [0, 2, 0, 2, 0], [0, 2, 0, 0, 2]]

# printing the array first
printArray(array)
print("")

# calling flipHorizontal() function to do just that
flipHorizontal(array)
print("")

# resetting the array back to its original state
array = [[0, 2, 0, 0, 0], [0, 2, 0, 0, 0], [0, 2, 2, 0, 0], [0, 2, 0, 2, 0], [0, 2, 0, 0, 2]]

# calling flipVertical() function to do just that
flipVertical(array)