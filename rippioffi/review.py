from tkinter import font
from tkinter import *
import random
import json

class Reviewing:

    def __init__(self, master: Frame, dest) -> None:
        self.master = master
        self.dest = dest
        

        self.master.pack(fill=BOTH, expand=1)

        self.font1 = font.Font(family='Georgia', size='40', weight='bold')
        self.font2 = font.Font(family='Aerial', size='12')

        #----------------------get data from file-----------------------------
        with open("data.json", "r") as file:
            self.data = json.load(file)
            self.card_list = []
            for key in self.data:
                m = self.data[key]

                self.card_list.append(dict(zip([key], [m])))
        #-initiate random question---------------------------------------------
        self.random_question()

        self.character = Frame(self.master, width=800, height=100, background="purple")
        self.character.grid(row=0,column=0, sticky=NW)

        self.label_character = Label(self.character, text=self.char, font=self.font1, background="purple", foreground="white")
        self.label_character.place(x=400, y=50, anchor="center")

        #------------------------form fill in the blank--------------------
        self.form = Frame(self.master)
        self.form.grid(row=1, column=0)

        self.pronoun = Label(self.form, text="Pronoun: ", font=self.font2)
        self.mean = Label(self.form, text="Meaning: ", font=self.font2)

        self.pronoun.grid(row=0, column=0, pady=10)
        self.mean.grid(row=1, column=0, pady=10)

        self.pronoun_entry = Entry(self.form, width=40, font=self.font2)
        self.mean_entry = Entry(self.form, width=40, font=self.font2)

        self.pronoun_entry.grid(row=0, column=1, padx=20)
        self.mean_entry.grid(row=1, column=1, padx=20)

        #------------------answer----------------------------------------
        self.answer = Frame(self.master)
        self.answer.grid(row=2, column=0, sticky=W)

        self.pronoun_answer = Label(self.answer, text=f"Pronoun: {self.info['pronounciation']}", font=self.font2, foreground="red")
        self.mean_answer = Label(self.answer, text=f"Meaning: {self.info['meaning']}", font=self.font2, foreground="red")
        self.desc_answer = Label(self.answer, text=f"Description: {self.info['description']}", font=self.font2, foreground="red")

        self.pronoun_answer.grid(row=0, column=0, sticky=W)
        self.mean_answer.grid(row=1, column=0, sticky=W)
        self.desc_answer.grid(row=2, column=0, sticky=W)

        self.answer.grid_remove()

        #---------------------Buttons---------------------------------------
        self.buttons = Frame(self.master)
        self.buttons.grid(row=3, column=0, sticky=NSEW, pady=40)

        self.back_btn = Button(self.buttons, text="BACK", font=self.font2, command=self.back)
        self.submit_btn = Button(self.buttons, text="SUBMIT", font=self.font2, command=self.submit_click)
        self.next_btn = Button(self.buttons, text="NEXT", font=self.font2, command=self.next_click)

        self.back_btn.pack(side=LEFT)
        self.submit_btn.pack(side=RIGHT)

    def clear_frame(self, frame):
        """clears all widgets in frame"""
        for widgets in frame.winfo_children():
            widgets.destroy()

    def back(self):
        """return back to menu"""
        self.master.pack_forget()
        self.clear_frame(self.master)
        self.dest.grid(row=0,column=0)

    def submit_click(self):
        """check the answer if correct or not"""
        self.correct1 = False
        self.correct2 = False
        self.submit_btn.pack_forget()
        self.next_btn.pack(side=RIGHT)
        self.ans1 = self.pronoun_entry.get()
        self.ans2 = self.mean_entry.get()

        if self.info["pronounciation"] == self.ans1:
            self.correct1 = True
            self.pronoun_entry.config(bg="green")
        else:
            self.pronoun_entry.config(bg="red")

        if self.info["meaning"] == self.ans2:
            self.correct2 = True
            self.mean_entry.config(bg="green")
        else:
            self.mean_entry.config(bg="red")

        if self.correct1 == False or self.correct2 == False:
            self.answer.grid(row=2, column=0, sticky=W)

    def next_click(self):
        """refresh the whole thing with another new question"""
        self.next_btn.pack_forget()
        self.submit_btn.pack(side=RIGHT)
        self.answer.grid_remove()
        self.pronoun_entry.config(bg="white")
        self.mean_entry.config(bg="white")
        self.pronoun_entry.delete(0, END)
        self.mean_entry.delete(0, END)


        self.random_question()

        self.label_character.config(text=self.char)
        self.pronoun_answer.config(text=f"Pronoun: {self.info['pronounciation']}")
        self.mean_answer.config(text=f"Meaning: {self.info['meaning']}")
        self.desc_answer.config(text=f"Description: {self.info['description']}")


    def random_question(self):
        """main brain to generate question"""
        #take a random number and loop for info
        self.rand = random.randint(0, len(self.card_list) - 1)

        for k, v in self.card_list[self.rand].items():
            self.char = k
            self.info = v
        #remove from list 
        del self.card_list[self.rand]
        #if empty refresh
        if len(self.card_list) == 0:
            with open("data.json", "r") as file:
                self.data = json.load(file)
                self.card_list = []
                for key in self.data:
                    m = self.data[key]

                    self.card_list.append(dict(zip([key], [m])))

            
            self.rand = random.randint(0, len(self.card_list) - 1)

            for k, v in self.card_list[self.rand].items():
                self.char = k
                self.info = v

            del self.card_list[self.rand]