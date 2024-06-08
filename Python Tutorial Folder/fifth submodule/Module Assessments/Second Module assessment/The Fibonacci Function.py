# The Fibonacci Function
# Requirements
# Write the Fibonacci function you wrote in the last submodule, but this time with recursion. 

# Follow these instructions to complete the mini-project.

#     Define your function.
#     Write the base condition.
#     Write the recursive return.

def main():

    def fibonacci(x):
       if x <= 1: #base condition to stop
           return x #if amt is 1. range(amt) is 0
       else:
           return(fibonacci(x-1) + fibonacci(x-2)) #recursion part
    
    
    amt= int(input("Enter how many Fibonacci numbers you would like (Note: number must be >0):"))
    
    
    if amt <= 0: #catches both them putting zero or a negative number
       print("Entered number must be greater than 0")
    else:
       print("Fibonacci sequence", amt, "numbers long:")
       for item in range(amt): #ex if amt is 3, range is 0, 1, 2 -> just a note for future me 
           print(fibonacci(item), end=' ')
       
       
main()       
      
