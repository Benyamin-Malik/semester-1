# Week 1.2, Session 2: Task 4

# A till system needs to offer a range of discounts:
# if the user is a member of the subscription service, they get 25% off
# if they are a student and a member, 30% off
# if they are just a student, 15% off
# if none of the above, they don't get a discount

# Look at the discounts in the final_cost calculation to match these up,
# and think about WHY they are in this order!

cost = int(input("Amount spent: "))
is_member = input("Are you a member? (y/n): ").lower()
is_student = input("Are you a student? (y/n): ").lower()

if is_member == "y" and is_student == "y"
    final_cost = cost * 0.7
elif  is_member == "y":
    final_cost = cost * 0.75
elif is_student == "y":
    final_cost = cost * 0.85
else:
    final_cost = cost

print(f"Final amount including discount: {final_cost}")

# they have to be in this order as if the 2nd condtion was first it would overall the  current first condition,
# i will sya hwoevevr can you not solve this issue by forcing the user to input the values y or n for both input fields.
#tthen we can refer to all possible input of the 2 conditions allowing us represent the statements in any order 