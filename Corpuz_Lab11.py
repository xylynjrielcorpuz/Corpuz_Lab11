
student_grades = []
student_passed = 0

while True:
    User_input_grades = input("Enter a student grade (type the word 'done' to exit): ")
    
    if User_input_grades.lower() == "done":
        break
    
    if float(User_input_grades) >= 40 and float(User_input_grades) <= 100: 
        student_grades.append(float(User_input_grades)) 
        
        if float(User_input_grades) >= 75:
             student_passed += 1
        
    else: 
        print("Invalid. Input grade/s must be higher than or equal to 40 or lower than or equal to 100.")
        
   
Student_average = sum(student_grades)/len(student_grades)
Student_passing_percentage = (student_passed/len(student_grades))*100
    
print("\n")
print(f"The average is: {Student_average:.2f}")
print(f"The number of student passed is: {student_passed}")
print(f"The passing percentage is: {Student_passing_percentage:.2f}%")

