# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


def format_data(day, month, year, separator="-"):
    # complete your code here
    formatted_date=print(f"{day}{separator}{month}{separator}{year}")

    return formatted_date


# Write code to test the function with separators such as "/", ":", "."
format_data(25,1,2007,"/")
#this tests the "/" sepeartor
format_data(25,1,2007,",")
#this tests the "," sepeartor
format_data(25,1,2007,":")
#this tests the ":" sepeartor
format_data(25,1,2007,".")
#this tests the "." sepeartor