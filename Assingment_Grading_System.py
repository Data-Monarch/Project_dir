#  Assignment_Grading_System
#   70 - 100 = A 
#   60 - 69 = B
#   50 - 59 = C
#   45 - 49 = D
#   40 - 44 = E
#   0  - 43 = F 
print("ASSIGNMENT GRADES")
Course = input("Enter The Course: ")
Grades = int(input("Enter_Score: "))

if Grades in range(70 ,101) :
    print("Your " + Course +  " Grade is A")
elif Grades in range(60 ,70) :
    print("Your " + Course +  " Grade is B")
elif Grades in range(50 ,60) :
    print("Your " + Course +  " Grade is C")
elif Grades in range(45 ,50) :
    print("Your " + Course +  " Grade is D")
elif Grades in range(40 ,45) :
    print("Your " + Course +  " Grade is E")
elif Grades in range(0 ,44) :
    print("Your " + Course +  " Grade is D")
else :
    print("Invalid_Entry")
