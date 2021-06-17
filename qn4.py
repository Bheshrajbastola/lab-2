'''Given three integers, print the smallest one. (Three integers should be user input)'''
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if(a<b and a<c):
    print("a is smaller")
elif(b<a and b<c):
    print("b is samller")
else:
    print("c is smaller")
