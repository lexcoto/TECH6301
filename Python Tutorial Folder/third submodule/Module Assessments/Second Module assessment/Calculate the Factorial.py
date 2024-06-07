# Calculate the Factorial

# Requirements
# Write a program that calculates the factorial of a number given by the user, then prints the output. 


# Follow these instructions to complete the mini-project.

#     Take the required input from the user.
#     Start the loop and apply your algorithm.
#     Print the factorial.

# Factorial Definition
# factorial, in mathematics, the product of all positive integers less than or equal to a given positive integer
#symbol for factorial is n! where n is number chosen


def main():
    
    n = int(input("Enter the number you want a factorial for (Note: Number must be >0): "))
    
    nfact = 1
    
    
    if n == 0: #Handles if the input is 0  
       print(n,"! is:",1)
       
    elif n < 0: #Factorial has to come from a positive number   
       print("Number must be greater than 0")
       
    else:
       for item in range(1,n + 1): #n+1 so that the last value, n, is included 
           nfact = nfact*item
           
       print(n,"! is:",nfact)
   

main()   



