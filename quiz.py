import pyperclip, re

text = str(pyperclip.paste())
print(text)
capitals = {}

#regEx = re.compile(r"[^countries|country][A-Za-z&']{2,}[,A-Za-z&' ]+")
regEx = re.compile(r"(?![country|countries])[A-Za-z&'-]{2,}[,A-Za-z&' ]+")
capital = regEx.findall(text)

print(capitals)

for i in range(0,len(capital),2):
        if(i< len(capital)-1):
            capitals[capital[i]] = capital[i+1]
        
print(capitals)