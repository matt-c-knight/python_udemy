myfile = open("fruits.txt")
content = myfile.read()
myfile.close()

# opening files using "with"
with open("fruits.text") as myfile:
    content = myfile.read()




# def foo(char, filepath="bear.txt"):
#     file = open(filepath)
#     content = file.read()
#     return content.count(char)