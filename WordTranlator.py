
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from googletrans import Translator

# GUI
window = tk.Tk()
window.title("Learn any language")
window.geometry("400x200")
# window.configure(background="black")

# A translator to convert words
def translation():
	translator = Translator()
	wordDetetctor = translator.detect('Ik ben een data scientist')
	Converter = translator.translate('Ik ben een data scientist')
	msg = messagebox.showinfo("Hi! there",'The input language {} and the meaning is: {}'.format(wordDetetctor, Converter))


# Create label
tk.Label (window, text="Enter something..", bg="black").pack()
# Create a text entry box
textEntry = tk.Entry(window, width=20, bg="white")
textEntry.bind("", translation)
textEntry.pack()
res = tk.Label(window)
res.pack()

# B = Button(window, text="Check meaning here", command = translation)
# B.place(x = 50, y=50)
window.mainloop()


