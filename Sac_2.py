# Prompt the user to enter the total number of students in the class. 
Total_Students = int(input("How many students are in your class?" ))
Student_count = Total_Students
# For each student, prompt the user to enter the student's name.
while Total_Students > 0:
    input("What is the Student's name? ")
    Total_Students = Total_Students - 1


# Prompt the user to enter the total number of periods of the class held in the week (between 1 and 5).
Periods_here = int(input("How many periods of class were held this week?")) + 1
Periods = Periods_here - Periods_here + 1

# For each student, prompt the user to enter attendance for each period (either 'P' for present or 'A' for absent).
while Periods < Periods_here:
    Letter = input("Was this student Present in class", Periods, "? (P for present, A for absent)")
    Periods = Periods + 1
       
# Use a nested loop to handle daily attendance entries for each student.


# Calculate the total number of classes each student was present for and the attendance percentage for each student.
Total_Periods = Periods - 1
if Letter == "P":
    attendance = attendance + 1
else:
if attendance = 1:
    Student_attendance = Total_periods / attendance
    

# Display each student's name, total days present, and attendance percentage. Include a warning for students with attendance below 75%. 


# Store the student names and daily attendance records in a file.
