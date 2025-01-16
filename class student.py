class Student:
    def __init__(self, name, age, grade, city):
        self.name = name
        self.age = age
        self.grade = grade
        self.city = city

    def showinfo(self):
        print("My name is : ",self.name)
        print("My age is : ",self.age)
        print("My grade is : ",self.grade)
        print("I live in : ",self.city)

name = input("Enter your name : ")
age = input("Enter your age : ")
grade = input("Enter your grade : ")
city = input("Enter the city in wich you live : ")

rayed = Student(name, age, grade, city)
rayed.showinfo()