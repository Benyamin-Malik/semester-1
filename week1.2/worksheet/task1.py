# Worksheet 1.2: Task 1 Solution
import sys
try: 
    Number = int(input("what is your number "))
    if Number <= 100 and Number >= 0 :
     ()
    else:
      sys.exit(" Error:Grade must be an integer between 0 and 100")
    if Number >= 0 and Number <= 39 :
     print(f"{Number} is a Fail")
    elif Number >= 40 and Number <= 69 :
     print(f"{Number} is a Pass")
    else:
        print(f"{Number} is a Distinction")
except:
       sys.exit(" Error: Grade must be an integer between 0 and 100")

       #trying to save