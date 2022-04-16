#Create a Python class Person with attributes: name and age of type string

class Person:
   def __init__(self, name, age):
    self.name= name
    self.age= age
    
#Create a display() method that displays the name and age of an object created via the Person class.

    def display(self):
       print("Person name : ", self.name)
       print("Person age = ", self.age)
       
#Create a child class Student which inherits from the Person class and which also has a section attribute.

class Student(Person):
    def __init__(self, name , age , section):
        Person.__init__(self,name, age)
        self.section = section
        
#Override the method display() for the Student class. Make it such that it displays the name, age and section of an object created via the Student class.

    def display(self):
       print("Person name : ", self.name)
       print("Person age = ", self.age)
       print("Person section = ", self.section)
       




#Create Person and Student objects and then test the display() method for both.

x=Person("Elif", 28 )
y=Student("Merve", 23, "Political Science")

x.display()
y.display()
    
       
    
        
        
    