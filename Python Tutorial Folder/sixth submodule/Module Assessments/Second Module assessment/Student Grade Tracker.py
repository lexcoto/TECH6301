# Student Grade Tracker
# Requirements
# Build a program that helps students track their grades. Students can input the 
# grades they achieve for each subject, and the program will read their grades 
# from a file and calculate their average grade. The program should handle 
# exceptions (e.g., invalid input, file errors) and store the grades in a file 
# for future reference. :
    
# Follow these instructions to complete the mini-project.

#     Write the code to input and store subject grades.

### Note: I interpreted this to mean we make our own subjects since none are given. 
### Also, since it says "subject grades" I interpret it to mean final grade in that subject.
    
#     Write the code to calculate and display the average grade.
### I'm interpreting this to mean final Average of all the subjects combined
    
#     Write the code to handle exceptions for invalid input 
#     (e.g., non-numeric grades).
    
#     Write the code to store grades in a file for persistent data.
### Note:It's a little confusing but I'm interpreting this ^^^ to mean we create a file at the end with a record


###!! REMEMBER TO SET FILE PATH (JUST ABOVE READ ME COMMENT (LINE 69))

def main():
    try:
        name = input("What is your full name:") #so that a file can be made for each student based on their name.
        markscience = int(input("Enter your grade percetage (%) for Science:"))
        markenglish = int(input("Enter your grade percetage (%) for English:"))
        markmath = int(input("Enter your grade percetage (%) for Math:"))
        markphysed = int(input("Enter your grade percetage (%) for Phys. Ed.:"))
        markart = int(input("Enter your grade percetage (%) for Art:"))
        markmusic = int(input("Enter your grade percetage (%) for Music:"))
    
    except ValueError: #Handles if they dont enter a number 
        print("Invalid input. Please enter a number only (do not include % symbol)")
    
    else: #If no value error it continues
        #This section handles if a negative mark is entered. 
        if markscience < 0 or markenglish < 0 or markmath < 0 or markphysed < 0 or markart < 0 or markmusic < 0:
            print("Invalid input. Please enter a positive number only.")
            
        #This section handles is a mark over 100 is entered    
        elif markscience > 100 or markenglish > 100 or markmath > 100 or markphysed > 100 or markart > 100 or markmusic > 100:
            print("Invalid input. Mark percentages cannot be greater than 100%.")
        
        else:
            ###these are for the file
            marksciencestr = "\nScience Mark:"+ str(markscience)+"%" 
            markenglishstr = "\nEnglish Mark:"+ str(markenglish)+"%" 
            markmathstr = "\nMath Mark:"+ str(markmath)+"%" 
            markphysedstr = "\nPhys. Ed. Mark:"+ str(markphysed)+"%" 
            markartstr = "\nArt Mark:"+ str(markart)+"%" 
            markmusicstr = "\nMusic Mark:"+ str(markmusic)+"%" 
            
            ls = [markscience, markenglish, markmath, markphysed, markart, markmusic]
            def average(ls):
                avg= sum(ls)/len(ls)
                return avg
            avgstr = "\nTotal Grade Average"+ str(average(ls))+"%"
            formsg = name + ", your total grade average is:"+ str(average(ls))+"%"
            print(formsg)# To tell student their mark in the output
            marks = marksciencestr + markenglishstr + markmathstr + markphysedstr + markartstr + markmusicstr + avgstr
            
            def newentry(): #this section is for new diary entries
                directory = "C:\\Users\\Alex\\Documents\\intro to python\\sixth submodule\\Module Assessments\\Second Module assessment\\"
   ##READ ME!!!    ^^^ this has to be changed for whatever file path the grade files are to be stored in            
                filepath = directory + name + "'s marks.txt" #gives a unique name to the text file based on students grade
                
                
            
                file = open(filepath, "w")
                    
                
                file.write(marks)
                print("Entry saved.") #just to give feedback that it worked
                file.close()
            
            newentry()
        

main()

