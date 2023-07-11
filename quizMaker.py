import random, capitals as cap

countries = []

for i in range(3):
    countriesVar = list(cap.capitals.keys())
    countriesConst = list(cap.capitals.keys())

    with open(f"quiz{i+1}.txt","w") as file:

        file.write("Type '//' after your answer.\n")

        for j in range(len(countriesVar)):

            random.shuffle(countriesVar)
            random.shuffle(countriesConst)

            file.write(f"What is the capital of {countriesVar[-1]}?\n")

            print(countriesVar[-1])
            print(len(countriesVar))
            answers = [cap.capitals[countriesVar[-1]],cap.capitals[countriesConst[-2]],cap.capitals[countriesConst[-4]],cap.capitals[countriesConst[-3]]]
            
            countriesVar.pop()
            
            random.shuffle(answers)

            for k in range(4):
                file.write(f"{k+1}. {answers[k]}\n")
            


            