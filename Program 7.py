from tkinter import *
from tkinter import messagebox
import random

main = Tk()
main.title("Guess The Number")
main.geometry("420x320")

mark_img = PhotoImage(file="Mark.png") #Add the directoru of the image file

canvas = Canvas(main,width=90,height=90)
canvas.place(x=169,y=20,width=90,height=100) #defining postion of the canvas/image as distance from x-axis and x-axis in pixels
canvas.create_image(10,10,anchor=NW,image=mark_img)

guess = [0]

def generator():
    guess[0]=random.randint(1,1000)
    print(guess[0])
generator()

def game():
    global user_guess_gui
    guess_text = Label(main,text="Guess the number") #Adding a label/text in our window=main.
    guess_text.place(x=160,y=120)
    user_guess_gui = Entry(main)
    # Entry widget to take input from user
    # here () defines window in which we want our widget to be placed in
    user_guess_gui.place(x=150, y=150)

# placing the widget

def user():
    global user_guess_gui
    root = Tk()  # Creating another window named root
    root.title("AGAIN?")
    root.geometry("320x240")
    # root.configure(bg='color') #Using the Following code we can change the bg color of window

    user_guess = int(user_guess_gui.get())  # get() function to get the user input

    if user_guess == guess[0]:  # Comparing user guess with the generated number
        again = Label(root, text="\tYOU WON!!!!!", fg='green')
        # NOTE this Label widget is created in the root window
        again.place(x=90, y=45)

        again = Label(root, text="Would you like to play again?")
        again.place(x=90, y=85)

        def greeting():
            greet = Label(root, text="Thank You for Playing.")
            greet.place(x=100, y=160)
            root.withdraw()
            main.withdraw()
            # withdraw() to close the window is user does not wish to continue

        def Restart():
            game()
            root.withdraw()

        def yes():
            generator()
            yes_but = Button(root, text="YES?", command=Restart)
            # Creating button to take user input in the Yes/No format
            # command funtion to define the fuction which is to be executed by the button
            yes_but.place(x=90, y=120)

        def no():
            no_but = Button(root, text="NO?", command=greeting)
            # NOTE greeting function will close both the windows
            no_but.place(x=200, y=120)

        yes()
        no()

    elif user_guess < guess[0]:
        messagebox.showinfo('Hint',"Too Low.Try again")
        #greet = Label(root, text="Too Low.Try again")
        # greet.place(x=100, y=100)
        # GFG
        game()

    elif user_guess > guess[0]:
        messagebox.showinfo('Hint',"Too High.Try again")
        #greet = Label(root, text="Too High.Try again")
        #greet.place(x=100, y=100)
        game()

submit = Button(main, text="CHECK", command=user)
# Submit button to submit the user input
# to get the user input we have used the get() function
submit.place(x=180, y=175)
game()

main.mainloop()