#Question 1: Write Python code for the following:-

input_string = "Python is a case sensitive language"
print(input_string)
#(a) Find the length of the input string.
print('\n (a)')
print("The length of the input string: \n",len(input_string))

#(b) Reverse the order of the string in one line code.
print('\n (c)')
print("Reverse of the given input string: \n",input_string[ : :-1])

#(c) Using Slice function store "a case sensitive" in new string.
print('\n (c)')
new_string = input_string[10:26]
print("Store 'a case sensitive' in new string: \n ",new_string)

#(d) Replace "a case sensitive" with "object oriented".
print('\n (d)')
updated_string = input_string.replace("a case sensitive","object oriented")
print("Updated string after replacing 'a case sensitive' with 'object oriented': \n",updated_string)

#(e) Find index of substring "a" in the given input string.
print('\n (e)')
index_substring = input_string.find('a')
print("The index of substring 'a' in the given input string: \n",index_substring)

#(f) Remove the white spaces from the given input string.
print('\n (f)')
input_string = input_string.replace(' ',' ')
print("String after removing the white spaces from the given input string: \n",input_string)

#Question 2: Use the string formatting to print your Name, SID, Department name and CGPA in the following output.

Name = "Nikita Samyal"
SID = 21103005
Department_name = "CSE"
CGPA = 9.9
print(f"\nHey, {Name} Here!\n"
      f"My SID is {SID} \n"
      f"I am from {Department_name} department and my CGPA is {CGPA}")

#Question 3: For a = 56 and b = 10 with the help of bitwise operators calculate the following:-

a = 56
b = 10
print('\n (a)')
print("With the help of bitwise AND operator :\n",a&b)
print('\n (b)')
print("With the help of bitwise OR operator:\n", a|b)
print('\n (c)')
print("With the help of bitwise XOR operator:\n", a^b)
print('\n (d)')
print("Bitwise Left shift a with 2 bits: \n",a<<2)
print("Bitwise Left shift b with 2 bits: \n",b<<2)
print('\n (e)')
print("Bitwise Right shift a with 4 bits: \n",a>>4)
print("Bitwise Right shift b with 4 bits: \n",b>>4)

#Question 4: Find the greatest of three numbers entered by the user.

number_1 = float(input("Enter the first number:\n"))
number_2 = float(input("Enter the second number:\n"))
number_3 = float(input("Enter the third number:\n"))

if(number_1 > number_2) and (number_1 > number_3):
    print(f"First number i.e. {number_1} is the greatest.")
elif(number_2 > number_1) and (number_2 > number_3):
    print(f"Second number i.e. {number_2} is the greatest.")
else:
    print(f"Third number i.e. {number_3} is the greatest.")

#Question 5: Check if the word 'name' is present in the string entered by the user or not(Print : "Yes" or "No").

input_string = input("\nEnter the string:\n")
print("\nThe word 'name' is present in the entered string or not (Yes or No)?")

if 'name' in input_string:
    print("Yes \n")
else:
    print("No \n")

#Question 6: Check whether the given input lengths can form a triangle or not(Print: "Yes" or "No").

Side_1 = int(input("Enter the first side of a triangle:\n"))
Side_2 = int(input("Enter the second side of a triangle:\n"))
Side_3 = int(input("Enter the third side of a triangle:\n"))
print("\nThe given input lengths can form a triangle or not (Yes or No)?")
Sum_1 = Side_1 + Side_2
Sum_2 = Side_2 + Side_3
Sum_3 = Side_3 + Side_1
if(Side_1 > Sum_1) or (Side_1 > Sum_2) or (Side_1 > Sum_3):
    print("No")
elif(Side_2 > Sum_1) or (Side_2 > Sum_2) or (Side_2 > Sum_3):
    print("No")
elif(Side_3 > Sum_1) or (Side_3 > Sum_2) or (Side_3 > Sum_3):
    print("No")
else:
    print("Yes")


    





      
