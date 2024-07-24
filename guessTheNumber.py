import random
import math

lower = int(input("Enter lower bound : "))

upper = int(input("Enter upper bound : "))

x = random.randint(lower, upper)

total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("you have only", total_chances, "chances to guess the number")

count =  0
flag = False

while count < total_chances:
    count += 1

    guess = int(input("Enter your no. : "))

    if x == guess:
        print("Congratulation your guess is correct")

        flag = True
        break

    elif x < guess:
        print("You guess bigger number than actual number.")

    else:
        print("You guess smaller no. than actual number ")

if not flag:
    print("The number is",x)
    print("Better luck next time")            