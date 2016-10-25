import sys

def reverseString(string):
    return string[::-1]

str = "This is a string"
strFinal = ""

print(reverseString(str))

for letter in reversed(str):
    strFinal += letter

print(strFinal)