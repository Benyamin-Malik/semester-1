# Worksheet 1.2: Task 1 Solution
try: 
    Number = int(input("what is your number "))
    if Number <= 100 and Number >= 10 :
        print("valid")
    else:
     print("Please enter a value between 10 and 100 inclusive")    
except:
       ValueError
       print("Please enter a whole number between 10 and 100")
