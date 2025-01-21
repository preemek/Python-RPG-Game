import Player
# import Enemy
# import Location
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def create_player(player:Player.Player,l_name):
    
        if len(l_name) > 5:
            messagebox.showinfo("Information","Name to long. Name must be less than 15 characters")
        else:
            player.create_player("new_player",input_name=l_name)


class PythonGame:
    def __init__(self,root:tk.Tk,locations=["ala","bab"]):
        self.player=Player.Player()
        self.locations=[locations]
        self.root=root
        self.root.title("Python RPG Game")
        # self.root.resizable(0,0)
        self.style=ttk.Style()
        self.style.configure("TButton",font=('Gabriola', 12),foreground="black")
        self.style.configure("TLabel")
        
        self.start()
    
    def clear_widgets(self):
        for frame in self.root.winfo_children():
            for widget in frame.winfo_children():
                widget.destroy()
        
    
    def start(self):
        self.root.geometry("600x300")
        ttk.Label(self.root,text="Welcome to Python RPG game",font=('Blackadder ITC', 20,"bold")).grid(row=0,column=0,sticky="EW")
        ttk.Label(self.root,text="by Wiktor Durek").grid(row=1,column=0,sticky="EW")
        ttk.Button(self.root,text="Create new character",command=self.new_character_window).grid(row=3,column=0)
        ttk.Button(self.root,text="Load from save file",command=self.choose_save_file_window).grid(row=4,column=0)
        
    def main_menu(self):
        self.clear_widgets()
        self.root.geometry("600x600")
        ttk.Label(self.root,text=self.player.name,relief="raised",width=100,).pack(side="left",pady=50,padx=25)
    
    def choose_save_file_window(self):
        pass


    def new_character_window(self):
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



#only for testing
root=tk.Tk()
ala=PythonGame(root)
root.mainloop()
"""
text_varible updates contents of label when changed

"""