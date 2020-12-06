# the factorial of a number
from math import  factorial

def factorial(n):
   if n == 1:
      return 1
   else:
     return (n * factorial(n-1))

print("Tell me the number to know the factorial:")
num = input()
fact_num = int(num)
result = factorial(fact_num)
print("The factorial of number {} is {}".format(fact_num, result))
