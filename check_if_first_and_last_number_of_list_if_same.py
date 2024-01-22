# Check if the first and last number of a list is the same
# Exercise 5

# Creating pseudocode

# Creating the starting code indicating the def of first_same_last
def first_same_last(numbers) :
    # Creating the code for given list
    print("The given list is: ", numbers)
    if numbers[0] == numbers[-1]:
        # Indicate true if they are the same
        return "the same. True!"
    else: 
        return "same. False!"
    
# Write the list and make the code to print
numbers_x = [10, 20, 30, 40, 10]
print("First and last number of the given are,", first_same_last(numbers_x))
    
numbers_y = [75, 65, 35, 75, 30]
print("First and last number of the given aren't the", first_same_last(numbers_y))
