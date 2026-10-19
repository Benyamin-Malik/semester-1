"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Benyamin Malik
"""
maxtime=int(input("Maximum numbe of steps"))
states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0

state = "red"
for i in range(0,maxtime,1):
    print(i)
    if i%4==0 :
      print(f"Time {systime:03} State {state}")
    else:
       ()

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14