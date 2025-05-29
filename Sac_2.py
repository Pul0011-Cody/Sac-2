# Find out how many students are in the class 
Total_Students = int(input("How many students are in your class?" ))
Student_count = Total_Students
Student_count_2 = Total_Students
# Finds out the name of each student in the class and adds them to a list
Student_Names = []
while Total_Students != 0:
    Student_Names.append(input("What is the student's name? "))
    Total_Students = Total_Students - 1
    

       
# asks for how many periods of class happened within the week. Can only be 1 to 5 classes
Total_Periods = "hi"
Total_Periods = int(input("How many periods of class were held this week?"))
while Total_Periods not in range(1,6):
    print("Please state the number of periods of class that was held this week (1 to 5)")
    Total_Periods = int(input("How many periods of class were held this week?"))
Period_counter = Total_Periods

# Finds out if student 1 has been to class for the amount of periods stated
if Student_count >= 1:
    Student_1_Attendance = []
    if Period_counter >= 1:
        Student_1_Attendance.append(input("Was {} Present for the First period? (P for Present, A for Absent) ".format(Student_Names[0])))
        Period_counter = Period_counter - 1
    if Period_counter >= 1:
        Student_1_Attendance.append(input("Was {} Present for the Second period? (P for Present, A for Absent) ".format(Student_Names[0])))
        Period_counter = Period_counter - 1
    if Period_counter >= 1:
        Student_1_Attendance.append(input("Was {} Present for the Third period? (P for Present, A for Absent) ".format(Student_Names[0])))
        Period_counter = Period_counter - 1
    if Period_counter >= 1:
        Student_1_Attendance.append(input("Was {} Present for the Fourth period? (P for Present, A for Absent) ".format(Student_Names[0])))
        Period_counter = Period_counter - 1
    if Period_counter >= 1:
        Student_1_Attendance.append(input("Was {} Present for the Fifth period? (P for Present, A for Absent) ".format(Student_Names[0])))
        Period_counter = Period_counter - 1
    
    Period_counter = Total_Periods
    Student_count = Student_count - 1
# Finds out if student 2 has been to class for the amount of periods stated
if Student_count >= 1:
    Student_2_Attendance = []
    for Student_2 in Student_Names:
        if Period_counter >= 1:
            Student_2_Attendance.append(input("Was {} Present for the First period? (P for Present, A for Absent) ".format(Student_Names[1])))
            Period_counter = Period_counter - 1
        if Period_counter >= 1:
            Student_2_Attendance.append(input("Was {} Present for the Second period? (P for Present, A for Absent) ".format(Student_Names[1])))
            Period_counter = Period_counter - 1
        if Period_counter >= 1:
            Student_2_Attendance.append(input("Was {} Present for the Third period? (P for Present, A for Absent) ".format(Student_Names[1])))
            Period_counter = Period_counter - 1
        if Period_counter >= 1:
            Student_2_Attendance.append(input("Was {} Present for the Fourth period? (P for Present, A for Absent) ".format(Student_Names[1])))
            Period_counter = Period_counter - 1
        if Period_counter >= 1:
            Student_2_Attendance.append(input("Was {} Present for the Fifth period? (P for Present, A for Absent) ".format(Student_Names[1])))
            Period_counter = Period_counter - 1
    
    Period_counter = Total_Periods
    Student_count = Student_count - 1
# Finds out if student 3 has been to class for the amount of periods stated
if Student_count >= 1:
    Student_3_Attendance = []
    for Student_3 in Student_Names:
        if Period_counter >= 1:
            Student_3_Attendance.append(input("Was {} Present for the First period? (P for Present, A for Absent) ".format(Student_Names[2])))
            Period_counter = Period_counter - 1
        if Period_counter >= 1:
            Student_3_Attendance.append(input("Was {} Present for the Second period? (P for Present, A for Absent) ".format(Student_Names[2])))
            Period_counter = Period_counter - 1
        if Period_counter >= 1:
            Student_3_Attendance.append(input("Was {} Present for the Third period? (P for Present, A for Absent) ".format(Student_Names[2])))
            Period_counter = Period_counter - 1
        if Period_counter >= 1:
            Student_3_Attendance.append(input("Was {} Present for the Fourth period? (P for Present, A for Absent) ".format(Student_Names[2])))
            Period_counter = Period_counter - 1
        if Period_counter >= 1:
            Student_3_Attendance.append(input("Was {} Present for the Fifth period? (P for Present, A for Absent) ".format(Student_Names[2])))
            Period_counter = Period_counter - 1

# Finds the total number of classes student 1 was present for and the attendance percentage 
if Student_count_2 >= 1:
    P_count = "P"
    A_count = "A"
    Student_1_P_Total = Student_1_Attendance.count(P_count)
    Student_1_A_Total = Student_1_Attendance.count(A_count)
    Total_Classes = Student_1_P_Total + Student_1_A_Total
    Total_Classes_Percentage = int(Student_1_P_Total / Total_Classes * 100)
    Student_1_Percentage = Total_Classes_Percentage
    Student_1_Total_Classes = Total_Classes
    Student_1_Days = Student_1_P_Total,"classes, out of", Student_1_Total_Classes
# Finds the total number of classes student 2 was present for and the attendance percentage    
if Student_count_2 >= 2:
    Student_2_P_Total = Student_2_Attendance.count(P_count)
    Student_2_A_Total = Student_2_Attendance.count(A_count)
    Total_Classes = Student_2_P_Total + Student_2_A_Total
    Total_Classes_Percentage = int(Student_2_P_Total / Total_Classes * 100)
    Student_2_Percentage = Total_Classes_Percentage
    Student_2_Total_Classes = Total_Classes
    Student_2_Days = Student_2_P_Total,"classes, out of", Student_2_Total_Classes
# Finds the total number of classes student 3 was present for and the attendance percentage 
if Student_count_2 >= 3:
    Student_3_P_Total = Student_3_Attendance.count(P_count)
    Student_3_A_Total = Student_3_Attendance.count(A_count)
    Total_Classes = Student_3_P_Total + Student_3_A_Total 
    Total_Classes_Percentage = int(Student_3_P_Total / Total_Classes * 100)
    Student_3_Percentage = Total_Classes_Percentage
    Student_3_Total_Classes = Total_Classes
    Student_3_Days = Student_3_P_Total,"classes, out of", Student_3_Total_Classes
    
# Displays each student's name, total days present, and attendance percentage including a warning for students with attendance below 75% and stores it into a list
Data = []
if Student_count_2 >= 1:
    print("(",Student_Names[0],")","(",Student_1_Days,")","(",Student_1_Percentage,")")
    Data.append(Student_Names[0])
    Data.append(Student_1_Days)
    Data.append(Student_1_Percentage)
    if Student_1_Percentage < 75:
        print(Student_Names[0], "has a attendance below 75%, they need to go to more classes")
if Student_count_2 >= 2:
    print("(",Student_Names[1],")","(",Student_2_Days,")","(",Student_2_Percentage,")")
    Data.append(Student_Names[1])
    Data.append(Student_2_Days)
    Data.append(Student_2_Percentage)
    if Student_2_Percentage < 75:
        print(Student_Names[1], "has a attendance below 75%, they need to go to more classes")
if Student_count_2 >= 3:
    print("(",Student_Names[2],")","(",Student_3_Days,")","(",Student_3_Percentage,")")
    Data.append(Student_Names[2])
    Data.append(Student_3_Days)
    Data.append(Student_3_Percentage)
    if Student_3_Percentage < 75:
        print(Student_Names[2], "has a attendance below 75%, they need to go to more classes")

# Stores the students names and daily attendance records in a file.
myFile = open ("Student_Attendance", "wt")
myList = Data
for item in myList:
    myFile.write(str(item)+ "\n")
myFile.close()