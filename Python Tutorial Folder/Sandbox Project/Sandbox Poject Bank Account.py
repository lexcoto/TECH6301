IDdatabase = [] #stores the IDs of accounts created so they can be checked by the ID generator when a new account is created
class BankAccount(object):    
    def __init__(self, name, accountType ,balance = 0):
        self.name = name
        self.accountType = accountType
        self.balance = 0 #balance starts at zero
        def IDgenerator():
            import random
            while True: # If it does happen to generate the same number twice, this loop ensures it will continue until it gets a unique ID
                number = random.randrange(1000,9999) #will generate ID from 1000 to 9999 
                if number not in IDdatabase:
                    IDdatabase.append(number)
                    return number
                    break
                elif len(IDdatabase) == 9999: #stops if it runs out of possible ID's 
                    print("out of unique IDs, please increase possible number of IDs") #just gotta add more significant digits to the range above
                    break
                else:
                    continue ##if number matches one already generated, this tries again
        
        self.accountNumber = IDgenerator()
        self.filename = str(self.accountNumber)+"_"+self.accountType+"_"+self.name+".txt"
        self.accountTypestr = f"{self.accountType}"
                
    def deposit(self): #depositing money into the account
        if self.accountTypestr == "chequing" or self.accountTypestr == "savings": #This section checks if account type is one of the two options
            print(f'{self.name}, You have chosen to deposit into {self.accountType} account:')
            try:
                amount = round(float(input("Enter amount you wish to deposit (Dollars):")), 2) #float rounded up to 2 so they can enter cents if they wish     
            except ValueError: #if they dont enter a number
               print("Invalid Input: Please enter just the numerical amount of dollars you wish to deposit (no symbols).")
            else:
                if amount >= 0:
                    self.balance += amount
                    print("\n Amount deposited: $",amount) 
                    print(f" Current {self.accountType} account balance: $",self.balance)
                    print(" ") #unessessary but just adding a line to make it easier on the eyes
                    
                    from datetime import datetime
                    current = datetime.now() #timestamp of current time
                    date_time = current.strftime("%m/%d/%Y, %H:%M:%S") #converts timestamp to string for writing
                    timestamp= "\n" + date_time #this just attaches a new line so the date prints on a new line
                    
                    transaction = "\nDeposit: $" + str(amount)
                    
                    try:
                        file = open(self.filename, "a") 
                        
                    except PermissionError: #Handles permission error
                       print("You do not have permission to view this file") 
                        
                    else:     
                        file.write("\n" + timestamp) #\n unnessecary but just to make a space between transactions making it easier on the eyes
                        file.write(transaction)
                        file.write("\nCurrent Balance: $" + str(self.balance))
                        print("Transaction logged") #just to give feedback that transaction was recorded
                        print(" ")
                        file.close()
                else:
                    print("Invalid Input: Please enter a positive number.") #if they enter negative number
                  
        else:
            print('Incorrect Account type entered. Please ensure account type is either "chequing" or "savings"(case sensitive)')
    
    def withdraw(self): #withdrawing money from the account
        if self.accountTypestr == "chequing" or self.accountTypestr == "savings":
            print(f'{self.name}, You have chosen to withdraw from {self.accountType} account:')
            try:
                amount = round(float(input("Enter amount you wish to withdraw (Dollars):")), 2)
            except ValueError:
               print("Invalid Input: Please enter just the numerical amount of dollars you wish to deposit (no symbols).")
            else:
                if amount >=0: #for checking if number entered was positive
                    if self.balance>=amount:#checks if theres enough balance
                        self.balance-=amount
                        print("\n Amount withdrawn: $", amount)
                        print(f" Current {self.accountType} account balance: $",self.balance)
                        print(" ")
                    
                 
                        from datetime import datetime
                        current = datetime.now() #timestamp of current time
                        date_time = current.strftime("%m/%d/%Y, %H:%M:%S") #converts timestamp to string for writing
                        timestamp= "\n" + date_time #this just attaches a new line so the date prints on a new line
                        
                        transaction = "\nWithdawal: $" + str(amount)
                        
                        try:
                            file = open(self.filename, "a") 
                            
                        except PermissionError: #Handles permission error
                           print("You do not have permission to view this file") 
                            
                        else:     
                            file.write("\n" + timestamp)
                            file.write(transaction)
                            file.write("\nCurrent Balance: $" + str(self.balance))
                            print("Transaction logged")
                            print(" ")
                            file.close()
                            
                    else: #if theres not enough balance in account
                        print(f"\n There insufficient funds in {self.accountType} account to fulfill your request.")
                        print(" Current {self.accountType} account balance:",self.balance)
                        print(" ")
                else:
                  print("Invalid Input: Please enter a positive number.")  
        else:
            print('Incorrect Account type entered. Please ensure account type is either "chequing" or "savings"(case sensitive)')
 
    def displaybalance(self): #getting the account’s balance.
        print(f'Retrieving Current Balance for account {self.accountNumber}:')
        print(f" Current {self.accountType} account balance: $",self.balance)
        print(" ")
        
    def displayuserid(self): #getting the user ID (Account Number)
        print('Retrieving User ID:')
        print("\n User ID number:", self.accountNumber)### fill this once you figure it out
        print(" ")
        #print(str(IDdatabase)) -> This was just a check i made to check if ID was actually added to the database, can be uncommented to confirm
        
    def displayusername(self): #Getting the holder name.
        print('Retrieving Username:')
        print("\n Username:", self.name)
        print(" ")

    def checkaccounttpye(self): #getting ccount type
        if self.accountTypestr == "chequing" or self.accountTypestr == "savings":
            print(f'Retrieving Account Type Balance for account {self.accountNumber}:')
            print("\n Account Type:",self.accountType)
            print(" ")
        else:
            print('Incorrect Account type entered. Please ensure account type is either "chequing" or "savings"(case sensitive)')

    def displaystransactionhistory(self): #getting transaction history
        print(f'Retrieving Transaction History for account {self.accountNumber}:')
        try:
            file = open(self.filename, "r")
        except FileNotFoundError: #Handles file not found
            print("file not found or no transactions have been made. Please check file location.")
        
        except PermissionError: #Handles permission error
           print("You do not have permission to view this file")
           
        else:
            out = file.read()
            print(out)
            print(" ")
            file.close()
        

###Examples###

#---Available functions---
#.deposit() #For deposits
#.withdraw() #For Withdrawals
#.displaybalance() #To display current Balance for the account
#.displayuserid() #To display account ID number
#.displayusername() #To display name of the account holder
#.checkaccounttpye() #To check if account is chequing or savings
#.displaystransactionhistory() #To read out the statement file 



#---Clients---
client1 = BankAccount("Bob", "chequing", 5) #This one has 5 just to show balance will start at 0 regardless like it's supposed to
client2 = BankAccount("Dude", "savings", 0)  
client3 = BankAccount("Kirby", "savings", 0)



#---testing different transactions---

client1.displaybalance()
client1.deposit()
client1.withdraw()

client2.deposit()
client2.withdraw()
client2.deposit()
client2.withdraw()
client2.displaystransactionhistory()

client1.displaybalance() #again to show balance was updated
client1.withdraw()#this one to show that you dont need to do all functions for a client consecutively before switching to another client


client3.displayusername()
client3.displayuserid()
client3.checkaccounttpye()
client3.displayuserid() #Twice just to show user ID stays constant once created





 

    