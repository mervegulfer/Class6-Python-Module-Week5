#Write a Rectangle class, allowing you to build a rectangle with length and width attributes.

class Rectangle():
    def __init__ (self,length,width):
        self.length= length
        self.width= width
        
#Create a perimeter() method to calculate the perimeter of the rectangle and an area() method to calculate the area of ​​the rectangle.
    def Perimeter(self):
        return 2*(self.length + self.width)
    
    def Area(self):
        return self.length * self.width
    
#Create a method display() that displays the length, width, perimeter and area of an object created using an instantiation on Rectangle class.
     
    def display(self):
        print("The length of rectangle is: ", self.length)
        print("The width of rectangle is: ", self.width)
        print("The perimeter of rectangle is: ", self.perimeter)
        print("The area of rectangle is: ", self.area)
          
          
#Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another volume() method to calculate the volume of the Parallelepiped.

class Parallelepipede(Rectangle):
    def __init__(self,height):
        self.height= height
                     
    def volume(self):
       return self.length * self.width * self.height