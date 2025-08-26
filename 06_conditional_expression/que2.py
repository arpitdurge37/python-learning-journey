marks1 = int(input("Marks1:"))
marks2 = int(input("Marks2:"))
marks3 = int(input("Marks3:"))

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass")

else:
    print("You failed")