'''
salary = (float)(input("Enter your salary : "))


if salary > 2000:
    salary*=0.9
print("your salary after tax :",salary)
'''

number = (int)(input("Enter a number : "))

print("your number is",number, end="")

if (number % 3) == 0 and (number % 5) == 0:
    print(" ,divides by 5 and 3")