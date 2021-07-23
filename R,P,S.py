import random as r
user_choice = input('Select a from Rock , Paper , Scissors(r,p,s): ')

user_choice = user_choice.lower()

choices = ['r','p','s']

ai_choice = r.choice(choices)

meaning_choices = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissors'
}

if user_choice in choices:
    print(f'your choice: {meaning_choices[user_choice]}\tAi choice: {meaning_choices[ai_choice]}')

    #! r > s  -  p > r  -  s > p : user_win
    #? user_choice == ai_choice : Tie

    if user_choice == 'r' and ai_choice == 's':
        print('You Win !')

    elif user_choice == 'p' and ai_choice == 'r':
        print('You Win !')

    elif user_choice == 's' and ai_choice == 'p':
        print('You Win !')

    elif user_choice == ai_choice:
        print('Tie')


    else:
        print('You Lost')

else:
    print('Error: Invalid input')