try:
     with open("./12_advanced_python1/1.txt", "r") as f:
         print(f.read())
except Exception as e:
     print(e)

try:
     with open("./12_advanced_python1/2.txt", "r") as f:
         print(f.read())
except Exception as e:
     print(e)

try:
     with open("./12_advanced_python1/3.txt", "r") as f:
         print(f.read())
except Exception as e:
     print(e)


print("Thank You")
