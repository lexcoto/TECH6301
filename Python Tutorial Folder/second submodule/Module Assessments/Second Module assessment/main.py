
#Create your Python file and call it main.py.
#Take the first input from the user and call it first_number.
#Take the second input from the user and call it second_number.
#Create the variables sum, subtraction, multiplication and division and assign them their values based on the two inputs.
#Print the four variables.
#Upload your Project to GitHub.


def main ():
    first_number= int(input("Enter the first number:"))
    second_number= int(input("Enter the second number:"))
    sum= first_number + second_number
    subtraction= first_number - second_number
    multiplication= first_number * second_number
    division= first_number / second_number
    
    
    print("Sum:", sum)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division", division)
main ()