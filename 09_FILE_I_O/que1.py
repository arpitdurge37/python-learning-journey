f = open("./09_FILE_I_O/poem.txt")
content = f.read()
if("twinkle" in content):
    print("twinkle is present")

else: 
    print("twinkle is not present in content")


f.close()