import tkinter
from PIL import Image, ImageTk
import random
root = tkinter.Tk()
root.geometry('400x300')
root.title('Dice Roll by Abhishek Jaiswal')

# Adding label into the frame
l0 = tkinter.Label(root, text="Make Random Dice Roll")
l0.pack()
l1 = tkinter.Label(root, text="Click on ROLL THE DICE at the bottom", fg = "light yellow",
        bg = "dark red",
        font = "Arial 16")
l1.pack()

# images
dice = ['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png']
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

lab = tkinter.Label(root, image=image1)
lab.image = image1
lab.pack( expand=True)

# function of button
def rolling_dice():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    lab.configure(image=image1)
    lab.image = image1

button = tkinter.Button(root, text='Roll the Dice', fg='black', command=rolling_dice)
button.pack( expand=True)

root.mainloop()