rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
mychoice = input("rock, paper ou scissors?>>")
choices = [rock, paper, scissors]

if mychoice == "rock": 
  mychoice = rock
  print(f"My choice is:{rock}")
  choices = [paper,scissors]
  computer_choice = random.choice(choices)
  print(f"Computer's choice is: {computer_choice}")
  
elif mychoice == "paper":
  mychoice = paper
  print(f"My choice is:{paper}")
  choices = [rock,scissors]
  computer_choice = random.choice(choices)
  print(f"Computer's choice is: {computer_choice}")
  
elif mychoice == "scissors":  
  mychoice = scissors
  print(f"My choice is:{scissors}")
  choices = [paper,rock]
  computer_choice = random.choice(choices)
  print(f"Computer's choice is: {computer_choice}")

if mychoice == rock and computer_choice == scissors:
  print("You win")
elif mychoice == scissors and computer_choice == paper:
  print("You win")
elif mychoice == paper and computer_choice == rock:
  print("You win")
else:
  print("Computer wins")





