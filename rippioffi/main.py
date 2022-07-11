from review import Reviewing
from edit import Edit
from adding import Add_New
from tkinter import *


win = Tk()
win.geometry("800x400")
win.title("rippi offi")

def remove_buttons():
    home.grid_forget()

def change_to_review():
    remove_buttons()
    Reviewing(review_section, home)

def change_to_add():
    remove_buttons()
    Add_New(adding, home)

def change_to_edit():
    remove_buttons()
    Edit(edit_section, home)
    

#---------frames(basically surfaces)----------------------

home = Frame(win) #home, main page
adding = Frame(win) #add section
edit_section = Frame(win) #edit
review_section = Frame(win) #review

#-----------button------------------------
add_btn = PhotoImage(file="images/add_new.png")
edit_btn = PhotoImage(file="images/edit.png")
quit_btn = PhotoImage(file="images/quit.png")
review_btn = PhotoImage(file="images/review.png")

add_button = Button(home, image=add_btn, command=change_to_add)
edit_button = Button(home, image=edit_btn, command=change_to_edit)
quit_button = Button(home, image=quit_btn, command=win.destroy)
review_button = Button(home, image=review_btn, command=change_to_review)

add_button.grid(row=0, column=0, padx=55, pady=30)
edit_button.grid(row=0, column=1)
review_button.grid(row=1, column=0)
quit_button.grid(row=1, column=1)

home.grid(row=0, column=0)

win.mainloop()