marks = int(input("Enter Marks: ",))
attendance = int(input("Enter Attendance: "))

if marks >= 80 and attendance >= 75 :
    print("Excellent: ", marks, attendance)

elif marks >= 40 and attendance >= 75 :
    print("Passed:", marks, attendance)
else:
    print("Failed:", marks, attendance )
   
    
