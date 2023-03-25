import random

def play_hangman():
    words = ['python', 'programming', 'computer', 'algorithm', 'variable']
    
    word = random.choice(words)
    
    guesses = ''
    turns = 6
    
    while turns > 0:        
        print('Word:', ''.join([l if l in guesses else '-' for l in word]))
        print('Guesses left:', turns)
                
        guess = input('Guess a letter: ').lower()
                
        if guess in word:
            print('Correct!')
            guesses += guess
        else:
            print('Incorrect!')
            turns -= 1
                        
            print('  _______')
            print(' |       |')
            if turns == 5:
                print(' |       O')
            elif turns == 4:
                print(' |       O')
                print(' |       |')
            elif turns == 3:
                print(' |       O')
                print(' |      /|')
            elif turns == 2:
                print(' |       O')
                print(' |      /|\\')
            elif turns == 1:
                print(' |       O')
                print(' |      /|\\')
                print(' |      /')
            else:
                print(' |       O')
                print(' |      /|\\')
                print(' |      / \\')
                    
        if set(word) <= set(guesses):
            print('Congratulations, you won!')
            break
            
    if turns == 0:
        print('Sorry, you ran out of turns. The word was', word)

play_hangman()
