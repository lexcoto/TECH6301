# The Fibonacci Sequence

# Requirements
# Write a program to print the Fibonacci sequence for a count given by the user. 

### Note: I interpret this ^^ to mean the user specifies how many numbers of the fibonnaci sequence is run

# Define your required variables.
# Take the input from the user.
# Start the loop to get the Fibonacci numbers for the user’s input.
# Print the number of every loop.

### Note: I'm interpreting this ^^^ to mean you label each loop after the first two numbers


def main():


    num1 = 0
    num2 = 1
    x = 0 #For a counter to l1abel loops
    question= int(input("Enter how many Fibonacci numbers you would like (Note: number must be >0):"))
    
    loop_amt = question - 2 # The way I'm interpreting this, the user is asked for the length of the whole 
                               # sequence (including the first two numbers), not just the number of loops. 
                               # so user input would have to be input - 2
    if loop_amt == -1 : # if they enter a 1 then loop_amt would be -1, so this part just prints the first number
        print('First number: ', num1)
       
    elif loop_amt <= -2 : # this is just to catch if they enter a zero or negative number
        print("Number must be greater than 0")
    
    else: #if they enter 2 it just prints the first two numbers, if more it runs the loop
        print('First number: ', num1)
        print('Second number:', num2)
        for item in range(loop_amt):
            subsequentnums = num1 + num2
            x = x + 1 #with each loop this increments the counter
            print('Loop #',x,':', subsequentnums)
            num1 = num2
            num2 = subsequentnums
        
main()        