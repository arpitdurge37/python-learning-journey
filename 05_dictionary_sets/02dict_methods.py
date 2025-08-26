marks = {
    "Arpit": 100,
    "Shubham" : 85,
    "Rohan" : 45, 
    "list" : [1,5,9],
    0: "nikhil"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Arpit": 99, "Priti": 100})
# print(marks)

# print(marks.get("Yash")) #none
# print(marks.get("Arpit"))
# print(marks["Harry"]) #returns an error
# print(marks.clear)

removed = marks.pop("Rohan")

print(removed)
print(marks)
