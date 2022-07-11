from tkinter import font
from tkinter import *
import json



class Edit:

    def __init__(self, master: Frame, dest) -> None:
        self.dest = dest
        self.master = master
        self.main_frame = Frame(self.master)
        self.card = Frame(self.master)
        self.editing()

#----------------edit menu-----------------------
    
    def editing(self):
        """edit menu right here"""
        self.master.pack(fill=BOTH, expand=1)
        self.main_frame.pack(fill=BOTH, expand=1)

        self.font1 = font.Font(family='Georgia', size='22', weight='bold')
        self.font2 = font.Font(family='Aerial', size='12')
        self.position = 0

        #-----------------------------UI---------------------------------
        self.label = Label(self.main_frame, text="Edit Card", font=self.font1).pack(side=TOP, anchor=N)

        self.back = Button(self.main_frame, text="BACK", font=self.font2, command=self.back)
        self.back.pack(side=LEFT, anchor=N)
        self.search = Button(self.main_frame, text="search", font=self.font2, command=self.search)
        self.search.pack(side=RIGHT,  anchor=N)
        self.entry = Entry(self.main_frame, width=40, font=self.font2)
        self.entry.pack(side=TOP)


        with open("data.json", "r") as file:
            self.data = json.load(file)
            self.card_list = []
            for key in self.data:
                m = self.data[key]

                self.card_list.append(dict(zip([key], [m])))

        #craete canvas since only the canvas can utilize the scrollbar
        self.canvas = Canvas(self.main_frame)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        #create scrollbar
        self.sb = Scrollbar(self.main_frame, orient=VERTICAL, command=self.canvas.yview)
        self.sb.pack(side=RIGHT, fill=Y)

        #configure scrollbar to link with canvas
        self.canvas.config(yscrollcommand=self.sb.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.config(scrollregion=self.canvas.bbox("all")))
        #create second frame linked to canvas
        self.second_frame = Frame(self.canvas)
        #now put everything in second frame to be scrollable
        self.canvas.create_window(0,0, anchor=NW, window=self.second_frame)

        for k,v in self.data.items():
            self.btn = Button(self.second_frame, text=f"{k} \t {v['meaning']}", width=70, font=self.font2, command= lambda some=self.position: self.click(some))
            self.btn.grid(row=self.position, column=0)
            self.position += 1
            

    def click(self, number):
        """loads in data of clicked card"""
        print(number)
        for k, v in self.card_list[number].items():
            self.chara = k
            self.value = v
        print(self.chara)
        print(self.value)
        self.main_frame.pack_forget()
        self.card_info(self.chara, self.value)


    def clear_frame(self, frame):
        """clears all widgets from the frame"""
        for widgets in frame.winfo_children():
            widgets.destroy()


    def back(self):
        """go back"""
        print("back")
        self.master.pack_forget()
        self.clear_frame(self.master)
        self.dest.grid(row=0,column=0)


    def search(self):
        """search for card"""
        self.position = 0
        self.found = False
        self.query = self.entry.get()
        print(self.query)
        self.clear_frame(self.second_frame)
        for k,v in self.data.items():
            if self.query == k or self.query == v['pronounciation'] or self.query == v['meaning']:
                self.btn = Button(self.second_frame, text=f"{k} \t {v['meaning']}", width=70, font=self.font2, command= lambda some=self.position: self.click(some)).grid(row=self.position, column=0)
                self.position += 1
                self.found = True

        if self.found == False:
            for k,v in self.data.items():
                self.btn = Button(self.second_frame, text=f"{k} \t {v['meaning']}", width=70, font=self.font2, command= lambda some=self.position: self.click(some)).grid(row=self.position, column=0)
                self.position += 1


#----------------------------------------card info-------------------------------

    def card_info(self, character, information):
        """individual card from click in edit menu"""
        self.card.pack(fill=BOTH, expand=1)
        self.list = Frame(self.card)
        self.list.grid(row=0, column=0)
        self.ch = character
        self.info = information
        print(self.ch)
        print(self.info)

        #------------------------Label----------------------
        self.char = Label(self.list, text="Character: ", font=self.font2)
        self.pronoun = Label(self.list, text="Pronounciation: ", font=self.font2)
        self.mean = Label(self.list, text="Meaning: ", font=self.font2)
        self.desc = Label(self.list, text="Description: ", font=self.font2)

        self.char.grid(row=0, column=0, pady=20)
        self.pronoun.grid(row=1, column=0, pady=20)
        self.mean.grid(row=2, column=0, pady=20)
        self.desc.grid(row=3, column=0, pady=20)

        #------------------------Entry--------------------------
        self.char_entry = Entry(self.list, width=40, font=self.font2)
        self.pronoun_entry = Entry(self.list, width=40, font=self.font2)
        self.mean_entry = Entry(self.list, width=40, font=self.font2)
        self.desc_entry = Entry(self.list, width=40, font=self.font2)

        self.char_entry.insert(0, self.ch)
        self.pronoun_entry.insert(0, self.info["pronounciation"])
        self.mean_entry.insert(0, self.info["meaning"])
        self.desc_entry.insert(0, self.info["description"])

        self.char_entry.grid(row=0, column=1, pady=20)
        self.pronoun_entry.grid(row=1, column=1, pady=20)
        self.mean_entry.grid(row=2, column=1, pady=20)
        self.desc_entry.grid(row=3, column=1, pady=20)

        #-----------------------Button------------------------------
        self.back_btn = Button(self.list, text="BACK", width=20, height=5, font=self.font2, command=self.return_back)
        self.delete_btn = Button(self.list, text="DELETE", width=20, height=5, font=self.font2, command=self.delete)
        self.submit_btn = Button(self.list, text="update", width=20, height=5, font=self.font2, command=self.update)

        self.back_btn.grid(row=4, column=0)
        self.delete_btn.grid(row=4, column=1)
        self.submit_btn.grid(row=4, column=2)

    def return_back(self):
        """return to edit menu"""
        self.card.pack_forget()
        self.clear_frame(self.card)
        self.main_frame.pack(fill=BOTH, expand=1)
        self.canvas_update()

    def delete(self):
        """delete card"""
        with open("data.json", "r") as file:
            self.data = json.load(file)

        if self.ch in self.data.keys():
            del self.data[self.ch]
                
        
        with open("data.json", "w") as file:
            json.dump(self.data, file, indent=4)

        self.return_back()
        self.canvas_update()
        
    def canvas_update(self):
        """reload and refresh the cards in edit menu"""
        self.canvas.delete("all")
        self.canvas.create_window(0,0, anchor=NW, window=self.second_frame)
        self.clear_frame(self.second_frame)

        self.card_list = []
        for key in self.data:
            m = self.data[key]

            self.card_list.append(dict(zip([key], [m])))

        self.position = 0

        for k,v in self.data.items():
            self.btn = Button(self.second_frame, text=f"{k} \t {v['meaning']}", width=70, font=self.font2, command= lambda some=self.position: self.click(some))
            self.btn.grid(row=self.position, column=0)
            self.position += 1


    def update(self):
        """update card info"""
        with open("data.json", "r") as file:
            self.data = json.load(file)


            self.char_data = self.char_entry.get()
            self.pronoun_data = self.pronoun_entry.get()
            self.mean_data = self.mean_entry.get()
            self.desc_data = self.desc_entry.get()

            if self.ch in self.data.keys():
                del self.data[self.ch]
                self.ch = self.char_data


            self.new_data = {
                self.char_data: {
                    "pronounciation": self.pronoun_data,
                    "meaning": self.mean_data,
                    "description": self.desc_data
                }
            }

            self.data.update(self.new_data)

        with open("data.json", "w") as file:
            json.dump(self.data, file, indent=4)

        self.canvas_update()
        