# @Author  : Vijayalakshmi K @Time    : 12/5/2020 7:53 PM
import random
mynos = []

print (" addition")

for counter in range (0,2):
      mynumber = random.randint(1,9)
      mynos.append(mynumber)
print(mynos)

the_answer = sum(mynos)
#print(the_answer)
player_answer =int(input("What is the answer?"))


def main():
    if player_answer is the_answer:
        print("Correct! Well done!")
        print("You scored 1 out of 10 so far!")
        print("Good job!")
    else:
        print("Incorrect! You scored null points!")
        print("Try Again")
        exit()

main()