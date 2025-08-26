# class Employee:
#     company = "ITC"
#     name = "Default name"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the company is {self.company}")

# class Coder:
#     language = "Pyhton"
#     def showLanguage(self):
#         print(f"out of all the languages here is your languages: {self.language}")

# class Programmer(Employee, Coder):
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.company} and he is good with {self.language} language")

# a = Employee()
# b = Programmer()

# b.show()
# b.showLanguage
# b.showLanguage




# //////



class A:
    def showA(self): print("A")

class B:
    def showB(self): print("B")

class C(A, B):    # inherits from both
    def showC(self): print("C")

c = C()
c.showA()
c.showB()
c.showC()
