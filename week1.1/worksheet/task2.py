"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name?")
print(f"Welcome to LeedsBank's savings calculator {name}!")

try:
 Monthly_Contribution=int(input("Please enter your montly savings amount:"))
 Yearly_Contribution=(float((Monthly_Contribution)*12))
 print(f"You will save £{Yearly_Contribution:.2f} each year")
 Yearly_Intrest=Yearly_Contribution*0.008
 Final_yearly_value=Yearly_Contribution+Yearly_Intrest
 print(f"With intrest you will save £{Final_yearly_value:.2f}")
except:
  print("Invalid amount")



# Ask the user to input an amount they want  to save every month - this should be an integer.
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

