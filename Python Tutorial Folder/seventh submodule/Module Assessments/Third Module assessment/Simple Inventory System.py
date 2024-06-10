# Simple Inventory System
# Requirements
# Create a simple inventory system that manages information about products in a store. 
# Each product should have specified attributes like name, price, and quantity. 
# Use classes to represent products and include methods for displaying product 
# information, updating quantities, and calculating the total value of the inventory. 


# Follow these instructions to complete the mini-project.

#     Create a class named product with attributes like name, price, and quantity.
    
#     Implement methods to display product information, including its name, price, 
#     and available quantity.
    
#     Allow users to add new products to the inventory.
    
#     Implement a method to update the quantity of a product when it is sold or restocked.
    
#     Calculate and display the total value of the inventory 
#     (sum of the values of all products).
###Note: I enterpret this^^^ to mean the total monetary value of the entire inventory (sum of (item price * item stock)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
 
    def restock(self): #using deposit since return is a keyword
        print(f'You have chosen to restock {self.name}.')
        amount = int(input("Enter amount to be restocked:"))
        self.quantity += amount
        print("\n Amount restocked:",amount)
        print(" Stock is now:",self.quantity)
        print(" ") #unessessary but just adding a line to make it easier on the eyes
 
    def sold(self):
        print(f'Sale of "{self.name}".')
        amount = int(input("Enter how many are to be sold:"))
        if self.quantity>=amount:#checks if theres enough stock
            self.quantity-=amount
            print("\n You sold:", amount)
            print(" There are now:",self.quantity, "in stock.")
            print(" ")
        else: #if theres not enough in stock 
            print(f"\n There are not enough of item: {self.name} in stock to fulfill your request")
            print(" Current stock:",self.quantity)
            print(" ")
 
    def displaystock(self): #if user just wants to check the stock
        print(f'Checking the stock of item: {self.name}')
        print("\n Available stock:",self.quantity,"in stock")
        print(" ")
        
    def description(self): #if user wants full descricption
        print("Item Description:")
        print(f'Item:{self.name}, Price:{self.price}. Current Stock:{self.quantity}')
        print(" ")
 
        
def totalinventoryvalue(): #For calculating the total value of the inventory
    
    item1pricestr = str(item1.price)  #you cant call integers or you get a value error, so this is a workaround calling it as a string then converting it back to int
    item1pricefloat = float(item1pricestr)
    item1quantstr = str(item1.quantity) #and again for quantity
    item1quantint = int(item1quantstr)
    
    item2pricestr = str(item2.price)
    item2pricefloat = float(item2pricestr)   
    item2quantstr = str(item2.quantity) 
    item2quantint = int(item2quantstr)

    item3pricestr = str(item3.price) #one of these blocks must be made for each new item, and the formula below updated
    item3pricefloat = float(item3pricestr)
    item3quantstr = str(item3.quantity) 
    item3quantint = int(item3quantstr)
    
    totalvalue = (item1quantint * item1pricefloat) + (item2quantint * item2pricefloat) + (item3quantint * item3pricefloat) #total value of an item is quantity in stock * price
    
    print("Total monetary value of Inventory($):", totalvalue)


###
#Scenario examples
  
# creating a items
item1 = Product("chicken", 20, 5) #user can make new items they just have to make it in format item# = Product("name", "price(number)", amount in stock(number))
item2 = Product("mango", 2, 3)  
item3 = Product("broccoli", 4.99, 1)


#original inventory value    
totalinventoryvalue()

#example of restock
item1.description()
item1.restock()
item1.displaystock()

#example of item sale
item2.description()
item2.sold()
item2.description() #showing balance in description has changed

#example of both restock and sale happening to same item and it being updated
item3.description()
item3.restock()
item3.sold()
item3.displaystock()

#updated inventory value after restocks and sales above
totalinventoryvalue()


    
