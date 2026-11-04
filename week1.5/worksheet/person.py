# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.

    """
    def __init__(self, name:str,birth:date):
    
     self.name =  name
     self.birth= birth

     if   not isinstance(name,str):
        raise TypeError("Name must be a string")
    
     if  name  == "":
        raise ValueError("must enter a name ")

     if not isinstance(birth,date):
        raise TypeError("birth must be a date ")

    

    # Implement methods initials() and is_birthday() here
    def initials(self):
        initials = ""
        for word in self.name.split():
            initials += word[0].upper()
        return initials

    def is_birthday(self):
     today=date.today()
     if today.strftime("%Y%m%d") == self.birth.strftime("%Y%m%d"):
      return("its your birthday")

     
a = Person("johnny smith",date(2026,11,4))
print(a.is_birthday())