#String Palindrome without using inbuilt function
s=input("Enter the string:")
str=""
for i in s:
    str=i+str
if(s==str):
    print("This is the palindrome string")
else:
    print("This is not a palindrome string")