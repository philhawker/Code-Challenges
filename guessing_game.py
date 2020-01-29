# def guessing_game():
#   while True:
#     print('what is your guess?')
#     guess = input('42')

#     if guess == '42':
#       print('your guess is correct')
#       return False
#     else:
#       print(f'no, {guess} is not the answer, please try again')


import random


num = random.randint(1, 100)



def guessing_game(num):
    
    print(num)
    user_guess = int(input('Guess a number between 1 and 100: '))
    while True:
        if user_guess > num:
            print('Your guess is too high')
        elif user_guess < num:
            print('Your guess is too low')
        else:
            print(f'{num} is correct')
            break
  
  

            
        
            

guessing_game(num)

    

    








