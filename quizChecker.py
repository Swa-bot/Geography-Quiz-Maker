import re, capitals as cap

total = 0
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


        for i in range(0,250):
            
            question = re.compile(r'What is the capital of (.*[^?])')

            check_answer = re.compile(r'[1-9]\. (.*)')
            
            answerFound = False
            
            if question.search(lines[i]):
                country = question.search(lines[i]).group(1)
                for j in range(4):

                    if lines[i+j+1] == f"{j+1}. {cap.capitals[country]}//" or lines[i+j+1] == f"{j+1}. {cap.capitals[country]} //":
                        total = total+1
                        answerFound = True

                if not answerFound:
                    print(f"The capital of {country} is {cap.capitals[country]}")
    print(total)

                



