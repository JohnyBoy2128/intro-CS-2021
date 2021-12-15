#   Program to generate 25 random numbers from 0 to 99, split them into odd and evens, and then print the three arrays
#   Module 8 Performance Task
#   John Paul Cannon
#   11 - 10 - 21

# importing random to create the random numbers
import random


# function to split the randNums array into even and odd parts, each in randEven and randOdds respectively
def splitNums():

    # loop to go through each number in the array and split them into even and odd using the modulo operator
    for i in range(len(randNums)):
        if (randNums[i] % 2 == 0):          # checks if number is even (evenly divisible by 2)
            randEven.append(randNums[i])
        else:                               # all odd numbers go here
            randOdds.append(randNums[i])


# function to print each of the arrays depending on which one needs to be printed
def printIt(arr):
    
    # conditional to check for which array is being printed
    if (arr == randNums):
        # printing appropriate title for random numbers 
        print("Random Numbers:")
        
        # loop to go through each index and print them with 2 spaces in between
        for i in range(len(randNums)):
            print(randNums[i], end="  ")
        
        # printing a new line to allow for appropriate spacing
        print("\n")
    
    elif (arr == randEven):
        # printing appropriate title for even numbers
        print("Even Numbers:")
        
        # loop to go through each index and print them with 2 spaces in between
        for i in range(len(randEven)):
            print(randEven[i], end="  ")
                    
        # printing a new line to allow for appropriate spacing
        print("\n")

    else:
        # printing appropriate title for odd numbers
        print("Odd Numbers:")
        
        # loop to go through each index and print them with 2 spaces in between
        for i in range(len(randOdds)):
            print(randOdds[i], end="  ")
                    
        # printing a new line to allow for appropriate spacing
        print("\n")



##########**********----**********##########
########    ********MAIN********    ########
##########**********----**********##########

# initializing variables
randNums = []           # array to hold all the randomly generated numbers
randEven = []           # array to hold the randomly generated even numbers
randOdds = []           # array to hold the randomly generated odd numbers


# for loop that runs 25 times and makes a random number each time. It appends them all to an array called randNums
for i in range(25):
    randNums.append(random.randint(0, 99))

# calling the splitNums function to split the even and odds into their respective arrays
splitNums()

# calling the printIt function 3 times, to print the randNums, randEven, and randOdds arrays
printIt(randNums)
printIt(randEven)
printIt(randOdds)