from tkinter import *
from PIL import ImageTk, Image

class Hangman:
    """
    A class representing the game of hangman
    """
    def __init__(self, window: any, images: list, word: str) -> None:
        """
        Method that to set default values
        :param window: The tkinter window
        :param images: list of png's for Man
        :param word: Word selected in main to be guessed
        """
        self.word = list(word)
        self.track_list = []
        self.choice_file = 0
        self.guess = ''
        self.win = 0
        self.word_hide, self.word_check = ['_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_']
        self.images = images
        self.root = window
        self.frame_man = Frame(self.root, background='black')
        self.image = ImageTk.PhotoImage(Image.open(self.images[self.choice_file]))
        self.label_man = Label(self.frame_man, image=self.image)
        self.label_man.image = self.image
        self.label_man.pack(pady=20)
        self.frame_man.pack(side=LEFT, expand=True, fill=BOTH)

        self.frame_guess = Frame(self.root, background='grey')
        self.label_answer = Label(self.frame_guess, text=' '.join(self.word_hide), font=('Ariel', 20), background='#c2bebe')
        self.label_guess = Label(self.frame_guess, text='Enter 6 letter word', font=('Ariel', 15), background='#c2bebe')
        self.entry_guess = Entry(self.frame_guess, width=20, font=('Ariel', 10))
        self.button_check = Button(self.frame_guess, width=10, text='CHECK', font=('Ariel', 20), background='#c2bebe', command=self.check)
        self.label_res = Label(self.frame_guess, text='', font=('Ariel', 12), background='grey')

        self.label_answer.pack(padx=5, pady=5, side=TOP)
        self.label_guess.pack(padx=5, pady=30)
        self.entry_guess.pack(padx=5)
        self.button_check.pack(padx=20, pady=50, side=TOP)
        self.label_res.pack(padx=15, pady=10, side=TOP)
        self.frame_guess.pack(side=LEFT, expand=True, fill=BOTH)

    def check(self) -> None:
        """
        Method to check inputted guess
        """
        self.label_res.config(text='')
        try:
            self.guess = str(self.entry_guess.get()).lower().strip()
            if len(self.guess) < len(self.word) or len(self.guess) > len(self.word):
                raise ValueError
            elif self.guess.isdigit():
                raise ValueError
            else:

                self.guess = list(self.guess)
                for i in range(len(self.word)):
                    if self.guess[i] == self.word_check[i]:
                        self.track_list.append('0')
                    elif self.guess[i] == self.word[i]:
                        self.word_hide[i] = self.word[i]
                        self.track_list.append('1')
                        self.word_check[i] = self.word[i]
                        if ''.join(self.word_hide) == ''.join(self.word):
                            self.win = 1
                    else:
                        self.track_list.append('0')
                if ''.join(self.track_list) == '000000':
                    self.entry_guess.delete(0, len(self.guess))
                    self.track_list = []
                    self.choice_file += 1
                    self.image = ImageTk.PhotoImage(Image.open(self.images[self.choice_file]))
                    self.label_man.config(image=self.image)
                    self.label_man.image = self.image
                    if self.choice_file >= 4:
                        self.loser()
                else:
                    self.track_list = []
                    if self.win == 1:
                        self.winner()
                    else:
                        self.label_answer.config(text=str(''.join(self.word_hide)))
        except ValueError:
            self.label_res.config(text='Input 6 letter word', fg='red', font=('Ariel', 15))

    def winner(self) -> None:
        """
        Method to display winning screen
        """
        self.label_res.config(text=f'Answer: {''.join(self.word)}', fg='black', font=('Ariel', 20), background='green')
        self.label_answer.config(text='YOU WIN', font=('Ariel', 20), background='green')
        self.label_guess.destroy()
        self.entry_guess.destroy()
        self.button_check.destroy()
        self.frame_guess.config(background='green')
        self.frame_man.config(background='green')
    def loser(self) -> None:
        """
        Method to display losing screen
        """
        self.frame_guess.config(background='red')
        self.frame_man.config(background='red')
        self.label_res.config(text=f'Answer: {''.join(self.word)}', fg='black', font=('Ariel', 20), background='red')
        self.label_answer.config(text='YOU LOSE', font=('Ariel', 20), background='red')
        self.label_guess.destroy()
        self.entry_guess.destroy()
        self.button_check.destroy()














