class Employee:
    language = "Python" #this is a class attribute
    salary = 1200000

obj1 = Employee()
obj1.language = "JavaScript"   #this is a object/instance attribute
print(obj1.language, obj1.salary)
