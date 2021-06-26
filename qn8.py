''' Given a three-digit number. Find the sum of its digits.'''
'''num=int(input("enter a number: "))
def getSum(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum

print(getSum(num))'''

number = int(input("enter a number three digit number : "))
a = number // 100
b = number // 10 % 10
c = number % 10
print(a + b + c)
