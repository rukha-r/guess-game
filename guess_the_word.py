sec_word = 'cool'
guess = ''
max_guess = 3
user_guess = 0
while guess != sec_word and max_guess > user_guess:
       guess = input('Type a word:  ')
       user_guess += 1
       if max_guess <= user_guess:
              print('You lost :(')
              play_again = input('Play again Y/N: ')
              if (play_again == str.lower('y')):
                     user_guess = 1
                     guess = input('Type a word:  ')
              elif (play_again == str.lower('n') ):
                     print('****  See you next time!  ****')
                     break

       elif max_guess > user_guess and guess == sec_word:
              print('****  You win!  ****')
              print('It took you ' + str(user_guess) + ' guesses to win...')
