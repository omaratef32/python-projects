from tkinter import *
from tkinter.font import BOLD
import json
import random

wn = Tk()
wn.geometry("800x500")
wn.resizable(0, 0)
wn.title("guess game")

# words_file = open("files\words.json")
# words = json.load(words_file)
# random.shuffle(words)

entry_frame = Frame(wn, width = 800, height = 200)
end_frame = Frame(wn, width=800, height=100)
visual_frame = Frame(wn, width = 800, height = 200)
letter = None
mainWord = "cat"
i = 10
e = 0
x = StringVar()
labels = {}





def letter_lable():
    global mainWord
    global labels
    global e

    labels[f"letter{e + 1}"] =  Label(visual_frame, background="#f0f0ed", width = 6, height = 3, font=("arial bold", 20), borderwidth=.5 ,relief="solid")

    if e < len(mainWord):
        e += 1
        letter_lable()
    else:
        return labels



def check(letter):
    global x
    global i
    global message
    global win
    global user_input
    global tries

    letter = letter.lower()

    if len(letter) > len(mainWord) or len(letter) < len(mainWord):
        message.destroy()
        message = Label(entry_frame, text=f"The word has jsut {len(mainWord)} characters you did {len(letter)} chars")
        message.grid(pady= 10, row=1)
        return
    else:
        message.destroy()

    if i == 0:
        lose.grid(pady=6)
        user_input = Entry(entry_frame, width=15, font=('ariel', 35, BOLD), border=0)
        user_input.grid(row = 2, column = 0, padx = 1, pady = 1)
        return

    for n in range(len(mainWord)):
        
        if mainWord[n]  == letter[n]:
            labels[f"letter{n + 1}"].destroy()
            labels[f"letter{n + 1}"] = Label(visual_frame, background="green", width = 6, height = 3, text=letter[n], fg="white", font=("arial bold", 20))
            labels[f"letter{n + 1}"].grid(row = 2, column = n, pady=45, padx=10)

        else:
            labels[f"letter{n + 1}"].destroy()
            labels[f"letter{n + 1}"] = Label(visual_frame, background="red", width = 6, height = 3, text=letter[n], fg="white", font=("arial bold", 20))
            labels[f"letter{n + 1}"].grid(row = 2, column = n, pady=70, padx=10)

    if mainWord == letter:
        win.grid(pady=20)
        user_input = Entry(entry_frame, width=15, font=('ariel', 35, BOLD), border=0)
        user_input.grid(row = 2, column = 0, padx = 1, pady = 1)
        return
    else:
        i -= 1
        tries.destroy()
        tries = Label(entry_frame, text=f"{i} chanses left!")
        tries.grid(row=4)

letter_lable()

for j in range(len(mainWord)):
            labels[f"letter{j + 1}"].grid(row = 2, column = j, pady=70, padx=10)

entry_frame.pack(side="bottom")
end_frame.pack(side="top")
visual_frame.pack(side="top")
win = Label(end_frame, text="congratulations", font=("Calibri", 50, BOLD), fg="green")
lose = Label(end_frame, text="failed", font=("Calibri", 50, BOLD), fg="red")
user_input = Entry(entry_frame, textvariable=x, width=15, font=('ariel', 35, BOLD), border=0).grid(row = 2, column = 0, padx = 1, pady = 1)
tries = Label(entry_frame, text=f"{i} chanses left!")
tries.grid(row=4)
submet = Button(entry_frame, text="check", font=('Onyx', 20, BOLD),width=10, fg="white", bg="#ed0eaa", border=0, command = lambda: check(x.get())).grid(row = 3, column = 0, padx = 10, pady = 20)
message = Label(entry_frame)

wn.mainloop()