"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Benyamin Malik
"""
maxtime=int(input("Maximum number of steps"))
states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = int(-1)

state = "red"
for systime in range(maxtime):
    if systime %15 <4 :
       state="red"
    elif systime%15<7 :
      state = "red_amber"
    elif systime%15<12:
      state="green"
    else:
      state="amber"
    print(f"Time {systime:04} State {state}")
    
    
# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14aaaaa
