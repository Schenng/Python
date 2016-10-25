import sys

def reverseString(string):
    return string[::-1]

str = "dallad"

str2 = reverseString(str)

if(str == str2):
    print("Palindrome")
else:
    print("Not Palindrome")