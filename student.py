def display_student():
    name="Vijay"
    roll_no=10
    print("Student Name:",name)
    print("Roll Number:",roll_no)
display_student() 
def calculate_grade(marks):
    if marks>=90:
        return "A"
    elif marks >=75:
        return "B"
    elif marks >=50:
        return "C"
    else:
        return "Fail"
def display_student():
    name="Vijay"
    roll_no=10
    print("Student Name:",name)
    print("Roll Number:",roll_no)
display_student()
print("Grade:",calculate_grade(int(input("enter marks\t"))))
