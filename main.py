#Insert the ASCII art and save each of the to corresponded variable
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

# Start coding by creating random
import random

# Link images with numbers
game_images = [rock, paper, scissors]

# Create the conditional statement if you insert number out of range
user_choice = int(input("What do you choose? rock, paper or scissors?\n"))
if user_choice >= 3 or user_choice < 0:
  print("You entered the invalid number!")
else:
  print(game_images[user_choice])

# Computer chooses random number from the range (0, 2)
  ai_choice = random.randint(0, 2)
  print(f'Computer chooses {ai_choice}')
  print(game_images[ai_choice])

# Create conditional statements to see if you choose any of the variables, you will win or lose to computer. But there can be draw as well 
  if user_choice == 0 and ai_choice == 2:
    print("You win!")
  elif user_choice == 0 and ai_choice == 1:
    print("You lost!")
  elif user_choice > ai_choice:
    print("You win!")
  elif user_choice < ai_choice:
    print("You lost!")
  elif user_choice == ai_choice:
    print("It is a tie game!")
