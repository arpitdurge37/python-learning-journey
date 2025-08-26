class Employee:
    language = "Python" #this is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Morning")

obj1 = Employee()
obj1.language = "JavaScript"   #this is a object/instance attribute
obj1.greet()
obj1.getInfo()



# Employee.getInfo(obj1)