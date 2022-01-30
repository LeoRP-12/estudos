# coding: utf-8 

import random 
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman():
    def __init__(self,word):
        self.word = word
        self.missed_letters=[]
        self.guessed_letters=[]
        self.word_len= len(word)
        self.iteration = 0
        self.hidden = self.word_len*"_ "
        self.wrong = []
        self.hits= []
        self.word_hits = ""
        self.word_wrong = ""

    def guess(self,letter):
        #guess = input("Digite uma letra: ")
        #self.value = guess
        #for i in self.word:
         #   if guess == i:
          #      check = True
           # else:
            #    check = False
        #if check == False:
         #   self.wrong.append(guess+',')
        #else:
         #   self.hits.append(guess+',')
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    def hangman_over(self):
        if self.hangman_won() or len(self.missed_letters) == 6 :
            return True
        else:
            return False

    def hangman_won(self):

        #if self.hidden == self.word:
         #   return True
        #else:
         #   return False
        if '_' not in self.hide_word():
            return True
        return False

    def hide_word(self):
        screen = ""
        for letter in self.word:
            if letter not in self.guessed_letters:
                screen = screen + "_"
            else:
                screen = screen + letter
        return screen

        #self.index = [i for i, x in enumerate(self.word) if x == self.value] # obtem indices de todas as ocorrencias de uma letra
       # for i in self.index:
        #    self.hidden= self.hidden[:i]+self.word[i] + self.hidden[i+1:]   # troca uma letra de uma string na posição i

    def print_game_status(self):
        #for i in range(len(self.hits)):
         #   self.word_hits = self.word_hits[:i] +self.hits[i] + self.word_hits[i+1:]
        #for i in range(len(self.wrong)):
         #   self.word_wrong = self.word_wrong[:i] + self.wrong[i]+self.word_wrong[i+1:] 
        #print(board[self.iteration])
        print(board[len(self.missed_letters)])
        print("Palavra: " + self.hide_word())
        print("\n")
        print("Letras erradas: ",)
        for letter in self.missed_letters:
            print(letter,)
        print("\n")
        print("Letras corretas: ",)
        for letter in self.guessed_letters:
            print(letter,)



def random_word():
    with open('words.txt','rt') as f :
        bank= f.readlines()
    return bank[random.randint(0,len(bank))-1].strip()

def main():
    game = Hangman(random_word())
    while not game.hangman_over():
        game.print_game_status()
        user_input=input('\nDigite um letra: ')
        game.guess(user_input)
        #game.hide_word()
        #game.iteration = game.iteration+1
    game.print_game_status()

    if game.hangman_won():
        print('\nParabéns! você venceu')

    else:
        print('\nGameover! você perdeu.')
        print('A palavra era '+ game.word)
    print('\n Foi bom jogar com você agora vá estudar!\n')

if __name__== "__main__":
    main()

