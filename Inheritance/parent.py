import os

class Person:
    
    # protected and private class variables 
    _name = None
    _age = None
    
    # Using Constructor for filling up name and age of a person.
    def __init__(self,name):
        self._name = name
        self._age = 0
        print("Onboarding started....")
        
    # Private class methods
    # Will take the self as parameter and will greet him/her with below message.
    def _greet(self):
        print("Hello " + self._name + "! Welcome to Wappnet Systems.\nThis is greeting message from Person class.")
    
    # It will take self as parameter and ask for the year of birth 
    # and will calculate age and print it. 
    def _calAge(self):
        y = input("Enter your Year of birth: ")
        self._age = 2022 - int(y)
        print()
        os.system("clear")
        print(self._name + ", you are " + str(self._age) + " years old !")

"""obj = Person("Hitesh")
obj._greet()
print()
obj._calAge()"""
