# Library Catalogue System
# Requirements
# Build a library catalogue system that manages information about books, including their title, author, 
# and availability status. Use classes to represent books and include methods for checking out and returning books.


# Follow these instructions to complete the mini-project.

#     Create a class for books with attributes like title, author, and availability status.
#     Implement methods to check out and return books, updating their availability status.
#     Allow users to add new books to the catalogue.
#     Print a simple scenario interaction with all these steps


class Books:
    def __init__(self, title, author, balance):
        self.title = title
        self.author = author
        self.balance = balance
        
 
    def deposit(self): #using deposit since return is a keyword
        print(f'You have chosen to return "{self.title}" by {self.author}.')
        amount=int(input("Enter amount to be returned: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
        print(" There are now",self.balance, "copies available.")
        print(" ") #unessessary but just adding a line to make it easier on the eyes
 
    def withdraw(self):
        print(f'You have chosen to withdraw "{self.title}" by {self.author}.')
        amount = int(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:#checks if theres enough copies
            self.balance-=amount
            print("\n You Withdrew:", amount, "copies")
            print(" There are now:",self.balance, "copies available.")
            print(" ")
        else: #if theres not enough copies 
            print("\n There are not enough available copies to fulfill your request")
            print(" Copies currently available:",self.balance)
            print(" ")
 
    def displaybalance(self): #if user just wants to check the balance
        print(f'Checking the balance of: "{self.title}" by {self.author}.')
        print("\n Net Available Balance=",self.balance)
        print(" ")
        
    def description(self): #if user wants full descricption
        print("Book Description:")
        print(f'"{self.title}", written by {self.author}. There are {self.balance} copies currently available')
        print(" ")
        
#Scenario examples
  
# creating a book
book1 = Books("Redwall", "Brian Jacques", 0) #user can make new books they just have to make it in format book# = Books("title", "author", balance of books in library (number only))
book2 = Books("Roverandom", "J.R.R. Tolkien", 3)  
book3 = Books("Math Rock Essentials", "Stephen Hazel", 0)

#book 1 examples (deposits)
book1.description()
book1.deposit()
book1.displaybalance()#shows the updated balance

#book 2 examples (withdrawals)
book2.description()
book2.withdraw()
book2.description() #showing balance in description has changed

#book 3 examples (doing both deposit and withdrawal on one book)
book3.description()
book3.deposit()
book3.withdraw()
book3.displaybalance()

