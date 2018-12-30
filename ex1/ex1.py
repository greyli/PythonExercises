import random

c_choice = random.randint(100,999)
a = int(input("Guess a number?(100-999) "))
running = True

while running: 

  if a == c_choice:
    print("BINGO!")
    running = False

  elif a < c_choice:
    print("The answer is bigger.")
    a = int(input("Try again~ "))

  elif a > c_choice:
    print("The answer is smaller.")
    a = int(input("Try again~ "))
