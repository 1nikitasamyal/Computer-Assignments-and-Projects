#Question 4: Make a list to enter marks of five students and display them in a sorted manner.

Student1_marks = int(input("Enter the marks of the Student 1: "))
Student2_marks = int(input("Enter the marks of the Student 2: "))
Student3_marks = int(input("Enter the marks of the Student 3: "))
Student4_marks = int(input("Enter the marks of the Student 4: "))
Student5_marks = int(input("Enter the marks of the Student 5: "))

Student_markslist = [Student1_marks, Student2_marks, Student3_marks, Student4_marks, Student5_marks]
print("\n List of the Student Marks:\n ", Student_markslist)

#Sorted list
print("\n Sorted Student List (increasing order): ")
Student_markslist.sort()
print(Student_markslist)
