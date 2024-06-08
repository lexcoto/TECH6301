# Calculate Factorial Using Recursion
# Requirements
# Write a function to calculate factorials using recursion.

###Note: I'm interpreting the instructions to want you to make a calculator that can handle any number.

# Follow these instructions to complete the mini-project.

#     Define your function.
#     Write the base condition.
#     Write the recursive return.

# Recursion definition: Recursion is a method of solving a computational problem where the solution depends on 
# solutions to smaller instances of the same problem.



def main():
    
    n = int(input("Enter the number you want a factorial for (Note: Number must be >= 0): ")) #User enters number they want factorial of
    
    def factorial(x):
        
        if x == 1: #Handles if the input is 1, since x-1 would be 0 
            
            return 1
            
        
        elif x == 0: #Handles if the input is 0  
            
            return 1
        
        elif x < 0: #Factorial has to come from a positive number   
        
           return "Number must be positive"
        
              
        else:
            return (x * factorial(x-1)) #recursive return
    
    
      
    nfact = factorial(n)
    if nfact == "Number must be positive": #This little if else loop handles the case of negative numbers entered
        print("Entered number must be positive")
    else:     
        print(n,"! is:",nfact)

main()

