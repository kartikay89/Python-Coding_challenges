
from tkinter import *
from tkinter import messagebox
from googletrans import Translator

# GUI
top = Tk()
top.geometry("200x100")

# A translator to convert words
def translation():
	translator = Translator()
	wordDetetctor = translator.detect('Ik ben een data scientist')
	Converter = translator.translate('Ik ben een data scientist')
	msg = messagebox.showinfo("Hi! there",'The input language {} and the meaning is: {}'.format(wordDetetctor, Converter))


B = Button(top, text="Check meaning here", command = translation)
B.place(x = 50, y=50)
top.mainloop()


