import random, capitals as cap

countries = []

for i in range(3):
    countries = list(cap.capitals.keys())

    with open(f"quiz{i+1}.txt","w") as file:
        file.write("Type '//' after your answer.\n")
        for j in range(50):
            random.shuffle(countries)
            file.write(f"What is the capital of {countries[j]}?\n")
            answers = [cap.capitals[countries[j]],cap.capitals[countries[20]],cap.capitals[countries[4]],cap.capitals[countries[30]]]
            random.shuffle(answers)
            for k in range(4):
                file.write(f"{k+1}. {answers[k]}\n")
    
    with open(f"answers{i+1}.txt","w") as file:
        for j in range(50):
            file.write(f"The capital of {countries[j]} is  {cap.capitals[countries[j]]}.\n")
            


            