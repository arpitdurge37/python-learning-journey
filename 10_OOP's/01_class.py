class Employee:
    language = "Python" #this is a class attribute
    salary = 1200000

obj1 = Employee()
obj1.name = "arpit1"   #this is a object/instance attribute
print(obj1.name, obj1.language, obj1.salary)

obj2 = Employee()
obj2.name = "rohan1"
print(obj2.salary, obj2.name, obj2.language)


# Here name is object/instance attribute and salary and language are class attribute as they directly belong to the class