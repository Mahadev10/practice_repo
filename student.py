# Classes are used tocreate custom datatypes
# For Modularity
# No code duplication
# Code reuseability
# class have both properties and attributes
# properties are instance variables
# attributes are methods
class Student:
    def __init__(self,id,firstName,lastName,age,cgpa,grade): # constructor
        self.id=id
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.cgpa=cgpa
        self.grade=grade
    def getPercentage(self):
        return int(self.cgpa * 10)
    def getFullName(self):
        return f"{self.firstName} {self.lastName}"
s1=Student(11,"Mahadev","Reddy",22,9.8,10)
s2=Student(10,"Leo","Messi",35,9,9)
print(s1.getPercentage())
print(s1.getFullName())