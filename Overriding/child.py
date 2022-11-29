from parent import *

# Creating a child class ::
class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("This is a Cat class.")
    # Overriding show method of parent class ::
    def show(self):
        print("Speaks MEOW MEOW everytime..")




