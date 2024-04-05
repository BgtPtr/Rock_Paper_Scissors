import random
import os
import re


def check_play_status():
  valid_responses = ['igen', 'nem']
  while True:
      try:
          response = input('Játszunk még egyet? (Igen vagy Nem): ')
          if response.lower() not in valid_responses:
              raise ValueError('Igen vagy Nem')

          if response.lower() == 'igen':
              return True
          else:
              os.system('cls' if os.name == 'nt' else 'clear')
              print('Köszönöm a játékot!')
              exit()

      except ValueError as err:
          print(err)


def play_rps():
   play = True
   while play:
       os.system('cls' if os.name == 'nt' else 'clear')
       print('')
       print('Kő, Papír, Olló!')

       user_choice = input(' [K]ő, [P]apír vagy [O]lló: ')

       if not re.match("[OoKkPOp]", user_choice):
           print('Válassz egy betút:')
           print('[K]ő, [P]apír vagy [O]lló')
           continue

       print(f'Te választasz: {user_choice}')

       choices = ['K', 'P', 'O']
       bot_choice = random.choice(choices)

       print(f'Én választok: {bot_choice}')

       if bot_choice == user_choice.upper():
           print('Döntetlen!')
           play = check_play_status()
       elif bot_choice == 'K' and user_choice.upper() == 'O':
           print('Kő veri az ollót, nyertem!')
           play = check_play_status()
       elif bot_choice == 'O' and user_choice.upper() == 'P':
           print('Olló veri a papírt, nyertem!')
           play = check_play_status()
       elif bot_choice == 'P' and user_choice.upper() == 'K':
           print('Papír veri a követ, nyertem!')
           play = check_play_status()
       else:
           print('Gratulálok, nyertél!\n')
           play = check_play_status()


if __name__ == '__main__':
   play_rps()