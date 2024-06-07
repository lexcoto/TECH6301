#Prime Numbers

# Requirements
# Write a program to print all the prime numbers between 2 and a number (N) given by the user. 

### I'm interpreting this ^^^ to mean we ask them how many prime numbers there are in a range that starts with 2, 
#but we also include 2. So we dont print 1 


# Take the required input from the user.
# Start the loop and apply your algorithm.
# Print the prime numbers inside the loop.

#Prime number definition:A prime number is a number that can only be divided by itself and 1 without remainders. 
#Prime numbers are only positive

def main():

    start = 2
    n = int(input("Enter the upper bound of a range (starting at 2) that you would like the prime numbers for (Note: Number must be >=2): "))
    
    print("The Prime numbers for your range are:")
    
    for number in range(start, n + 1):
       
       if number >= 2:
           for item in range(2, number):
               if (number % item) == 0:
                   break
           else:
               print(number)
               
main()