from tkinter import *
from tkinter import font
import json

class Add_New:

    def __init__(self, master: Frame, dest) -> None:
        self.dest = dest
        self.master = master

        self.font1 = font.Font(family='Georgia', size='22', weight='bold')
        self.font2 = font.Font(family='Aerial', size='12')

        #-------------------------label----------------------

        self.heading = Label(self.master, text="Add New Card", font=self.font1)
        self.character = Label(self.master, text="Character: ", font=self.font2)
        self.pronounciation = Label(self.master, text="Pronouncation: ", font=self.font2)
        self.meaning = Label(self.master, text="Meaning: ", font=self.font2)
        self.desc = Label(self.master, text="Description: ", font=self.font2)

        self.heading.grid(row=0, column=0, pady=30)
        self.character.grid(row=1, column=0, pady=10)
        self.pronounciation.grid(row=2, column=0, pady=10)
        self.meaning.grid(row=3, column=0, pady=10)
        self.desc.grid(row=4, column=0, pady=10)

        #-----------------------entry-----------------------

        self.character_entry = Entry(self.master, width=40, font=self.font2)
        self.pronounciation_entry = Entry(self.master, width=40, font=self.font2)
        self.meaning_entry = Entry(self.master, width=40, font=self.font2)
        self.desc_entry = Entry(self.master, width=40, font=self.font2)

        self.character_entry.grid(row=1, column=1)
        self.pronounciation_entry.grid(row=2, column=1)
        self.meaning_entry.grid(row=3, column=1)
        self.desc_entry.grid(row=4, column=1)

        #----------------------------Button-----------------------------------

        self.submit = Button(self.master, text="submit", width=20, height=5, font=self.font2, command=self.submit)
        self.back = Button(self.master, text="back", width=20, height=5, font=self.font2, command=self.back)

        self.submit.grid(row=5, column=1)
        self.back.grid(row=5, column=0)

        self.master.grid(row=0, column=0)

    def get_value(self):
        """get value of input"""
        self.chara = self.character_entry.get()
        self.pronoun = self.pronounciation_entry.get()
        self.mean = self.meaning_entry.get()
        self.des = self.desc_entry.get()

        self.card = {
            self.chara: {
                "pronounciation": self.pronoun,
                "meaning": self.mean,
                "description": self.des
            } 
        }

        print(self.card)

        return self.card

    def submit(self):
        """submit query"""
        self.new_data = self.get_value()

        with open("data.json", "r") as file:
            self.data = json.load(file)
            self.data.update(self.new_data)
            print(self.data)

        with open("data.json", "w") as file:
            json.dump(self.data, file, indent=4)
        

    def back(self):
        """go back"""
        self.master.grid_forget()
        self.dest.grid(row=0,column=0)


