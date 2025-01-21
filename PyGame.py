import Player
# import Enemy
# import Location
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def create_player(player:Player.Player,l_name):
    
        if len(l_name) > 10:
            messagebox.showinfo("Information","Name to long. Name must be less than 15 characters")
        else:
            player.create_player("new_player",input_name=l_name)


class PythonGame:
    def __init__(self,root:tk.Tk,locations=["ala","bab"]):
        self.player=Player.Player()
        self.locations=[locations]
        self.root=root
        self.root.title("Python RPG Game")
        # self.root.resizable(width=0,height=0)
        self.root.eval('tk::PlaceWindow . center')
        # self.root.resizable(0,0)
        self.style=ttk.Style()
        self.style.configure("TButton",font=('Gabriola', 12),foreground="black")
        self.style.configure("TLabel")
        
        self.start()
    
    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
    
    def start(self):
        self.root.geometry("600x300+500+200")
        root.columnconfigure(1,weight=1)
        root.columnconfigure(0,weight=1)
        root.rowconfigure(3,weight=1)
        ttk.Label(self.root,text="Welcome to Python RPG game",font=('Blackadder ITC', 20,"bold"),anchor="center").grid(row=0,column=0,columnspan=2,pady=(30,0),sticky="EW")
        ttk.Label(self.root,text="by Wiktor Durek",anchor="center").grid(row=1,column=0,columnspan=2,pady=(0,50),sticky="EW")
        ttk.Button(self.root,text="Create new character",command=self.new_character_window).grid(row=3,column=0,padx=(100,20),pady=(0,80),ipadx=10,sticky="ESN")
        ttk.Button(self.root,text="Load from save file",command=self.choose_save_file_window).grid(row=3,column=1,padx=(20,100),pady=(0,80),ipadx=10,sticky="WSN")
    
    def choose_save_file_window(self):
        root.columnconfigure(1,weight=0)
        root.columnconfigure(0,weight=0)
        root.rowconfigure(3,weight=0)
        def button_on(number):
            try:
                self.player.create_player("from_save_file",file_number=number)
                self.main_menu()
            except FileNotFoundError:
                messagebox.showerror(title="File not found!",message=f"file {number} doesn't exist")

        window=tk.Toplevel(self.root)
        window.title("Choose save file")
        window.geometry("400x100")

        window.columnconfigure((0,1,2),weight=1)
        window.rowconfigure(0,weight=1)
        ttk.Button(window,text="Save 1", command=lambda:button_on(1)).grid(row = 0, column = 0, pady=30, padx=30, sticky = "NESW")
        ttk.Button(window,text="Save 2", command=lambda:button_on(2)).grid(row = 0, column = 1, pady=30, padx=0, sticky = "NESW")
        ttk.Button(window,text="Save 3", command=lambda:button_on(3)).grid(row = 0, column = 2, pady=30, padx=30, sticky = "NESW")
        # self.main_menu()

    def new_character_window(self):
        root.columnconfigure(1,weight=0)
        root.columnconfigure(0,weight=0)
        root.rowconfigure(3,weight=0)
        def button_on():
            name = name_entry.get()
            new_char_window.destroy()
            self.player.create_player("new_player",input_name=name)
            self.main_menu()
            
        new_char_window = tk.Toplevel()
        name_var=tk.StringVar()
        new_char_window.title('Create new player')
        # new_char_window.geometry('230x50')

        name_entry_label = ttk.Label(new_char_window,text='Enter your name:')
        name_entry = ttk.Entry(new_char_window,width=20,textvariable=name_var)
        close_button = ttk.Button(new_char_window,text="Confirm",width=12,command=button_on)

        name_entry_label.grid(row=0,column=0)
        name_entry.grid(row=0,column=1,sticky="E")
        close_button.grid(row=1,column=0,columnspan=2,sticky="E")

    def main_menu(self):
            self.clear_widgets()
            self.root.geometry("600x600")
            ttk.Label(self.root,text=f"name: {self.player.name}",relief="raised",width=10,font=('Blackadder ITC', 20,"bold")).grid(row=0,column=0,padx=10,pady=10)
            ttk.Label(self.root,text=f"lvl: {self.player.Lvl}",relief="raised",width=10).grid(row=0,column=1,pady=10)

#only for testing
root=tk.Tk()
ala=PythonGame(root)
root.mainloop()
"""
text_varible updates contents of label when changed

"""