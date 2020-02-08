with open(r"C:\Users\nalsadi\Documents\Arduino\Variable\Variable.ino") as f:
    content = f.readlines()
print (content[14][0:9] , "56")
with open('your_file.txt', 'w') as f:
    for item in content:
        f.write("%s\n" % item)