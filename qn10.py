''' Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.'''
#num=int(input("enter a number:"))
'''def sum(a,b,c):
    if a==b or b==c or c==a:
        sum=0
    else:
        sum=a+b+c
        return sum
    print(sum)'''


num1=int(input("enter a number : "))
num2=int(input("enter a number : "))
num3=int(input("enter a number : "))
sum=0
if num1==num2 or num2==num3 or num1==num3:
    print(sum)
else:
    total=num1+num2+num3
    sum=total
    print("the total",sum)
