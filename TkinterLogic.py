from tkinter import *

#klasa tkinter

def error_message(message:str):
    error = Toplevel(title="error")
    error_message = Label(error,text=message)
    error_message.pack()
    error.mainloop()

def new_character_window():
    def button_on():
        name = name_entry.get()

        # if len(name) > 15:
        #     error_message("Name to long. Maximum 15 characters")
        # else:
        #     return name
    
    new_char_window = Toplevel()
    text = Label(new_char_window,text="empty")
    new_char_window.title('Create new player')
    new_char_window.geometry('230x50')

    name_entry_label = Label(new_char_window,text='Enter your name:')
    name_entry = Entry(new_char_window,width=20)
    close_button = Button(new_char_window,text="Confirm",width=12,command=button_on)

    name_entry_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    close_button.grid(row=1,column=0,columnspan=2)
    text.grid(row=3,column=0,columnspan=10)
    new_char_window.mainloop()



new_character_window()

