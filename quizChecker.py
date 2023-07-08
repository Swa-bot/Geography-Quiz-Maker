import re, capitals as cap

try:
    file_name = str(input("What is the name of the file you would like checked? eg. 'quiz1.txt'")).lower()

    with open(file_name,"r") as file:
        file.read()
except:
    print("Looks like an error occured, check if you typed the write file name and if the file is valid.")
else:
    with open(file_name,"r") as file:
        text = file.read()
        regEx = re.compile(r"(.*)\n")
        lines = regEx.findall(text)
        for line in lines:
            print(line)
