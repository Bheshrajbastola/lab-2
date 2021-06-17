'''WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint: more than 70% –> distinction, more than 60% –>
first, more than 40% –> pass, less than 40% –> fail'''

computer=int(input("enter a number of computer:"))
english=int(input("enter a number of english :"))
math=int(input("enter a number of math :"))
science=int(input("enter a number of science :"))

total = english + math + computer + science
percentage = (total / 400) * 100

print("Total Marks = %.2f"  %total)
print("Marks Percentage = %.2f"  %percentage)

if(percentage > 70):
    print("discition")
elif(percentage > 60):
    print("first")
elif(percentage >40):
    print("pass")
elif(percentage <40):
    print("fail")

else:
    print("invalid")
