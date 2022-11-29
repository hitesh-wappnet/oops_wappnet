from multipledispatch import dispatch

class Overload:
    
    # Printing below statement whenever object creates ::
    def __init__(self):
        print("Initializing Overload class")
     
    # Defining a method to take 2 parameters and return sum
    @dispatch(int,int)
    def sum(self,a,b):
        print("Sum is : ",a+b)
        
    # Overloading the sum method to take 3 parameters and return sum
    @dispatch(int,int,int)
    def sum(self,a,b,c):
        print("Sum is : ",a+b+c)
    
    # Overloading the sum method to take 4 parameters and return sum
    @dispatch(int,int,int,int)
    def sum(self,a,b,c,d):
        print("Sum is : ",a+b+c+d)


