class Employee:
    language = "Python" #this is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language):  #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating a object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

obj = Employee("Nikhil", 130000, "Javascript")
# obj.name = "Arpit"
obj.getInfo()
print(obj.name, obj.salary)

# rohan = Employee()
