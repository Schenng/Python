import sys

str = "This is a string"
str2 = ""

badLetter = "a"

for letter in str:
    if(letter != badLetter):
        str2 += letter
        
print(str2)