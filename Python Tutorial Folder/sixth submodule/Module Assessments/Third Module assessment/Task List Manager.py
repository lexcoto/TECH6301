# Task List Manager
# Requirements
# Develop a simple task list manager that allows users to add, remove, and view tasks. The program should save
# the task list to a text file and handle exceptions in a controlled manner

# Follow these instructions to complete the mini-project.

#     Write a function to add tasks to the list.
#     Write a function to remove completed tasks.
#     Write a function to view the current task list.
#     Write a function to save and load tasks from a file.
#     Write a function to handle exceptions for file read/write errors.

def main():
    try:        
        task = int(input("What would you wish to do (Enter 1 for new ToDo entry, 2 to see ToDo list, 3 to delete completed task):"))
        
    except ValueError: #handles if input is not number    
        print("Invalid entry. Please enter 1 for new ToDo entry, 2 to see ToDo list, 3 to delete completed task")

    else:     
        if task == 1:
            def newentry(): #this section is for new todo entries
                
                
                user_entry = input("Enter task (one at a time): ")
                entry = "\n" + user_entry # puts it on new line
                
                try:
                    file = open("todo.txt", "a")
                    
                except PermissionError: #Handles permission error
                   print("You do not have permission to view this file") 
                    
                else:     
                    
                    file.write(entry)
                    print("Entry saved.")
                    file.close()
        
            newentry()
            
            
        elif task == 2: #this section to review diary
            def viewprev():
                 try:
                     file = open("todo.txt", "r")
                 except FileNotFoundError: #Handles file not found
                     print("file not found. Please check file location.")
                 
                 except PermissionError: #Handles permission error
                    print("You do not have permission to view this file")
                    
                 else:
                     out = file.read()
                     print("Current ToDo list is:","\n",out)
                     file.close()
    
            viewprev()
       
        elif task == 3:
            def remove():
                try:
                    try:
                        file = open("todo.txt", "r")
                    except FileNotFoundError: #Handles file not found
                        print("file not found. Please check file location.")
                    
                    except PermissionError: #Handles permission error
                       print("You do not have permission to view this file")
                       
                    else:
                        out = file.read()
                        print("Current ToDo list is:","\n", out)
                        file.close()
                                
                except FileNotFoundError: #Handles file not found
                    print("file not found. Please check file location.")
                
                except PermissionError: #Handles permission error
                   print("You do not have permission to view this file")
                   
                else:
                    descision = int(input("Which line would you like to remove?:")) #user input for which line to remove

                    if descision < 0 :
                            print ("Invalid entry. Please enter a number greater than 0")
                            
                    
                    else:
                        lines = []
                        with open("todo.txt", 'r') as fp:                            
                            lines = fp.readlines() #first makes a list of all the lines
                        
                        
                        with open("todo.txt", 'w') as fp:                            
                            for number, line in enumerate(lines):
                                if number not in [descision]: #rewrites the whole thing not including the chosen line
                                    fp.write(line)
                                
                        fp.close()
                        print("line removed")
            remove()
    
        else: #Handles if user inputs any other number than 1,2,3
            print("Invalid entry. Please enter 1 for new ToDo entry, 2 to see ToDo list, 3 to delete completed task")
            
main()

# ValueError: