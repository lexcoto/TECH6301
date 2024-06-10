# Student Database System
# Requirements
# Create a simple student database system that stores information about students, such as their 
# names, ages, and grades. Use classes to represent students and include methods for displaying student 
# information and calculating average grades. 


# Student Database System
# Follow these instructions to complete the mini-project.

#     Create a class for students with attributes like name, age, and a list of grades.
#     Implement methods to display student information and calculate average grades.
#     Allow users to add new students to the database.
#     Print a simple scenario of interactions with all these steps.

class Student: 
    'A student class'
    stuCount = 0 #keeps track of which student it's on
  
    
    def __init__(self):   
        
        
        
        self.name = str(input("Please input students name:"))
        
        self.age = int(input("Please enter the students age:"))
        
        self.grades = float(input("Please enter the Student grade by precent calculated above:")) #ideally I wouldve wanted the user to be able to 
                                                                                                #input the grades and total here directly but couldnt 
                                                                                                #get it to work so did grade calculator separate
        
    
       
        Student.stuCount += 1
        
        
    
    # displayStudent method of class Student 
    def description(self): 

        print(f"Student: {self.name}. They are {self.age} years old. Their average grade is: {self.grades} ")
        
def gradecalc(): 
    for item in range(3): ### ! READ ME: The number in range() must be changed for how many students you have.
        def conv_grade_to_percentage(grades_earned, total_grades_available): 
        
            assert (grades_earned>=0 and total_grades_available>=0), "Your course grade or total grade is below zero." 
        
            return (grades_earned/total_grades_available)*100 
        name = str(input("Please input students name for calculator:"))
        
        grades_earned=float(input("Enter student grades earned:")) 
        
        total_grades_available= float(input("Enter total grade for course:"))
        
        percentage = conv_grade_to_percentage(grades_earned,total_grades_available) 
        print(">>>",name,"'s average grade(%):",round(percentage,2))    

gradecalc()
print("end of calculator")
print(" ")  
stud1 = Student() ### ! READ ME: Must create as many stud# = Student() for as many students you would like

stud2 = Student()

stud3 = Student()
 
stud1.description() 
stud2.description() 
stud3.description() 

