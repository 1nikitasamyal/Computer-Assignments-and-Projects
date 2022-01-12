#Question 2: Compute a person's income tax (in $).

#To compute a person's income tax (in $)
Gross_income = float(input("Enter the gross income:\n"))

#There is a $10000 standard deduction.
Standard_deduction = 10000

No_of_dependents = int(input("Enter the number of dependents:\n"))

#There is a $3000 deduction for each dependent.
Dependent_deduction = 3000

Taxable_income = Gross_income - Standard_deduction - (Dependent_deduction * No_of_dependents)
print("Taxable_income:\n", Taxable_income)

#Tax rate = 20%

Tax = (Taxable_income * 20)/100
print("Tax: \n", Tax)
