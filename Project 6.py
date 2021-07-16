# Guessing Game
# Demonstrates text and entry widgets, and the grid layout manager.

from tkinter import *
import random

class Application(Frame):
    """ GUI application which can retrieve an autp number to guess. """
    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """

        """ Instruction Label """

        # Create instruction label for Program
        self.inst_lbl = Label(self, text = "Follow the Steps")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)


        """ Player Name """

        # Create label for name
        self.name_lbl = Label(self, text = "Player Name: ")
        self.name_lbl.grid(row = 1, column = 0, sticky = W)

        # Create entry widget to accept name
        self.name_ent = Entry(self)
        self.name_ent.grid(row = 1, column = 1, sticky = W)

        self.number=random.randint(1,100)


        """ Guess Input """

        # Create label for entering Guess
        self.guess_lbl = Label(self, text = "Enter your Guess.")
        self.guess_lbl.grid(row = 3, column = 0, sticky = W)

        # Create entry widget to accept Guess
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 3, column = 1, sticky = W)

        # Create a space
        self.gap1_lbl = Label(self, text = " ")
        self.gap1_lbl.grid(row = 4, column = 0, sticky = W)

        """ Submit Button """

        # Create submit button
        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 5, column = 0, sticky = W)

        # Create a space
        self.gap2_lbl = Label(self, text = " ")
        self.gap2_lbl.grid(row = 6, column = 0, sticky = W)

        """ Display """

        # Create text widget to display welcome_msg
        self.display1_txt = Text(self, width = 45, height = 1, wrap = WORD)
        self.display1_txt.grid(row = 7, column = 0, columnspan = 2, sticky = W)


        # Create text widget to display welcome_msg
        self.display2_txt = Text(self, width = 45, height = 1, wrap = WORD)
        self.display2_txt.grid(row = 8, column = 0, columnspan = 2, sticky = W)

        # Create text widget to display welcome_msg
        self.display3_txt = Text(self, width = 45, height = 2, wrap = WORD)
        self.display3_txt.grid(row = 9, column = 0, columnspan = 2, sticky = W)

        # Create text widget to display welcome_msg
        self.display4_txt = Text(self, width = 45, height = 2, wrap = WORD)
        self.display4_txt.grid(row = 10, column = 0, columnspan = 2, sticky = W)


    def reveal(self):

        name = self.name_ent.get()
        guess = self.guess_ent.get()
        welcome_msg = "Welcome " + name
        guess_msg = " Your guess was: " + guess
        number=self.number


        tries = 1
        tries = str(tries)
        tries_msg = 0
        tries_msg = str(tries_msg)
        tries_msg = int(tries_msg) + int(tries)

        if int(guess) > number:
            result_msg = "Lower ..."
        elif int(guess) < number:
            result_msg = "Higher ..."
        else:
            result_msg = "You got it."

        '''
        tries = 1
        tries = str(tries)
        tries_msg = 0
        tries_msg = str(tries_msg)
        tries_msg = int(tries_msg) + int(tries)

        if guess > number:
            result_msg = "Lower ..."
        elif guess < number:
            result_msg = "Higher ..."
        else:
            result_msg = "You got it."
        '''

        # Display
        self.display1_txt.delete(0.0, END)
        self.display1_txt.insert(0.0, welcome_msg)
        self.display2_txt.delete(0.0, END)
        self.display2_txt.insert(0.0, guess_msg)
        self.display3_txt.delete(0.0, END)
        self.display3_txt.insert(0.0, result_msg)
        self.display4_txt.insert(0.0, tries_msg)


# Main manager
root = Tk()
root.title("Guessing Game")
root.geometry("300x200")

app = Application(root)

root.mainloop()