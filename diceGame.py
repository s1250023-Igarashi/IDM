import random

print("Rolling the dice...")

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

print("Die 1: " + str(die1))
print("Die 2: " + str(die2))
print("Total value: " + str(total))

if total > 7:
    print("You won")
else:
    print("You lost")
