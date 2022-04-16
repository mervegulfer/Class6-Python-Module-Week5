from unicodedata import name


class School():
    student=[]
    capacity=2
        
class Student(School):
    def __init__ (self,name, age,gender):
        self.name= name
        self. age= age
        self.gender=gender
        
    def __str__(self):
        print("Name: __str__ Age: __str Gender: __str__")
        
        return F'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'

    def add_student(self):
        if len(self.student) == self.capacity:
          print("Capacity is full!")
        else:
            self.student.append(self.name)
            print("okey")
    def print_students():
        for i in School.student:
           print(i)
    
    
school= School()
      
student1= Student("John", 39, "Male")
student2= Student("Maria", 23, "Female")
student3= Student("Ali", 78, "Male")

Student.add_student(student1)
Student.add_student(student2)
Student.print_students()
Student.add_student(student3)
print(student1.__dict__)

        
            
         