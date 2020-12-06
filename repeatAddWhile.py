# @Author  : Vijayalakshmi K @Time    : 12/5/2020 10:49 PM
# Repeated addition using while loop
num1 = int(input("Enter number1: "))
num2 = int(input("Enter the number2: "))
result = int(input("Enter the sum"))
sum = num1 + num2
while result != sum:
    result = int(input("Enter the sum"))
print("The Addition of {} and {}".format(num1, num2))
print(format(sum))


