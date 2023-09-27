#String Reverse without using inbuilt function

s=input("Enter the string:")
str=""
for i in s:
    str=i+str
print("Reveres String: ",str)
