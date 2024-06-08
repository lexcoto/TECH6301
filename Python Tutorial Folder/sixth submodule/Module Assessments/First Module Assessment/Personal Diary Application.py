# Personal Diary Application
# Requirements
# Create a simple personal diary application where users can write and 
# save their daily thoughts or experiences to a text file. The program should 
# allow users to view their previous entries and handle exceptions in a controlled 
# manner (e.g., file not found errors and permission issues). 

# Follow these instructions to complete the mini-project.

#     Write the code to create a new diary entry.
#     Write the code to view previous diary entries.
#     Write the code to handle exceptions (e.g., file not found errors and 
#     permission issues).
#     Write the code to optionally add timestamps to entries.

def main():
        
    task = int(input("what would you wish to do (Enter 1 for new diary entry, 2 to read previous entries):"))
    
    if task == 1:
        def newentry(): #this section is for new diary entries
            from datetime import datetime
            current = datetime.now() #timestamp of current time
            date_time = current.strftime("%m/%d/%Y, %H:%M:%S") #converts timestamp to string for writing
            timestamp= "\n" + date_time #this just attaches a new line so the date prints on a new line
            
            user_entry = input("Enter Diary entry: ")
            entry = "\n" + user_entry # same thing just puts it on new line
            
            try:
                file = open("diary.txt", "a")
                
            except PermissionError: #Handles permission error
               print("You do not have permission to view this file") 
                
            else:     
                file.write(timestamp)
                file.write(entry)
                print("Entry saved.")
                file.close()
    
        newentry()
        
        
    elif task == 2: #this section to review diary
        def viewprev():
             try:
                 file = open("diary.txt", "r")
             except FileNotFoundError: #Handles file not found
                 print("file not found. Please check file location.")
             
             except PermissionError: #Handles permission error
                print("You do not have permission to view this file")
                
             else:
                 out = file.read()
                 print(out)
                 file.close()

        viewprev()
        
        
    else: #Handles if user inputs any other number
        print("Invalid entry. Pleae enter 1 for new diary entry, 2 to read previous entries)")
        
main()

