#Question :3 Store different data type values into a list.

Name = input("Enter the name of the Student: ")
SID = int(input("Enter the Student ID:"))
Gender = input("Enter the gender of the Student(F,M,U): ")
Course_name = input("Enter the Student's course name: ")
CGPA = float(input("Enter the Student's CGPA: "))

Student_list = ['Name','SID','Gender','Course_name','CGPA']
print(Student_list)

Student_info = [Name,SID,Gender,Course_name,CGPA]
print("\n The list of the student information:\n ",Student_info)
           
