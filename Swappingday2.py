#Swapping of two number without using 3rd varible
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

print("After Swapping")
n1=n1+n2
n2=n1-n2
n1=n1-n2
print(n1)
print(n2)