# Week 1.2, Session 2: Task 6
machine_temp = input("what is the temperature of the machine")
machine_pressure=input("what is the pressure of the machine")
machine_OP=input("what is the operating status of the machine")

if machine_temp > 80 :
    print("alert: The temperature is too high! please shut down the machine.")
elif machine_temp >=50 and machine_temp <=80 :
    print("temperature iswithin safe limits.")
else:
    machine_temp<50
                                          