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

answer = str(input('What do you choose? Type 0 for Rock, 1, for Paper or 2 for Scissors.'))

if answer == '0':
    print(rock)
elif answer == '1':
    print(paper)
elif answer == '2':
    print(scissors)
else: 'Choose an option'    
    