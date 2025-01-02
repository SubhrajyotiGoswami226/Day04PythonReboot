import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
\n
"""


scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\n
"""

userInput=int(input("Your Turn\n Press 0 for Rock\n Press 1 for Paper\n Press 2 for Scissor\n"))
compChoice=[0,1,2]
compInput=random.choice(compChoice)

if userInput==0:
    print(rock)
    if compInput==userInput:
        print("Computer shows rock.")
        print(rock)
        print("It's a draw!!")
    elif compInput==1:
        print("Computer shows paper.")
        print(paper)
        print("You lost. Paper wins.")
    elif compInput==2:
        print("Computer shows scissor.")
        print(scissor)
        print("You win. Scissor lost.")
elif userInput==1:
    print(paper)
    if compInput==userInput:
        print("Computer shows paper.")
        print(paper)
        print("It's a draw!!")
    elif compInput==0:
        print("Computer shows rock.")
        print(rock)
        print("You win. Rock lost.")
    elif compInput==2:
        print("Computer shows scissor.")
        print(scissor)
        print("You lost. Scissor win.")
elif userInput==2:
    print(scissor)
    if compInput==userInput:
        print("Computer shows scissor.")
        print(scissor)
        print("It's a draw!!")
    elif compInput==1:
        print("Computer shows paper.")
        print(paper)
        print("You win. Paper lost.")
    elif compInput==0:
        print("Computer shows rock.")
        print(rock)
        print("You lost. Rock win.")