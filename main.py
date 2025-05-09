from hangman_gui import *
import random

def main() -> None:
    """
    Method to create window and choose word to guess
    """
    window = Tk()
    with open('word_list.txt', 'r') as word_list:
        words = word_list.readline().split(',')
    rng = random.randint(0, len(words)-1)
    word = words[rng]
    images = ['Man_1.png', 'Man_2.png', 'Man_3.png', 'Man_4.png', 'Man_dead.png']
    window.title('Final_Project_2')
    window.geometry('550x400')
    Hangman(window, images, word)
    window.mainloop()

if __name__=='__main__':
    main()