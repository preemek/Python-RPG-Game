import Player
import Enemy
from Location import village, forest, castle
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class PythonGame:
    def __init__(self,root:tk.Tk,locations=[village,forest,castle]):
        self.player=Player.Player()
        self.locations=[locations]
        self.root=root
        self.root.title("Python RPG Game")
        self.root.configure(background="#dcdad5")
        # self.root.resizable(width=0,height=0)
        
        self.style=ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TButton",font=('Gabriola', 12),foreground="black",background="#c6c4bf")
        self.style.configure("TLabel",font=('Gabriola', 12),foreground="black")
        self.style.configure("TLabelframe.Label",font=('Gabriola', 16,"bold"),foreground="black")
        self.style.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')
        self.style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
        
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
        
        def button_on(number):
            try:
                self.player.create_player("from_save_file",file_number=number)
                root.columnconfigure(1,weight=0)
                root.columnconfigure(0,weight=0)
                root.rowconfigure(3,weight=0)
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
        def button_on():
            name = name_entry.get()
            new_char_window.destroy()
            self.player.create_player("new_player",input_name=name)
            root.columnconfigure(1,weight=0)
            root.columnconfigure(0,weight=0)
            root.rowconfigure(3,weight=0)
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
    def locate_player(self):
        for location in self.locations:
            if location[0].name == self.player.Location:
                return location[0]
    def talk (self):
        location=self.locate_player()
        npc=""
        ttk.Label(self.root,text=f"{location.name}").grid(row=1,column=1)
    def explore (self):
        pass
    def fight (self):
        pass
        
    def main_menu(self):
        def create_user_stats (option,master=tk.Tk):
            if option =="create":
                name=ttk.Label(master,text=f"Name: {self.player.name}",width=16,font=('Blackadder ITC', 20,"bold")).pack(side="left",padx=10)
                hp=ttk.Label(master,text=f"HP: ").pack(side="left",padx=(0,10))
                hp_bar=ttk.Progressbar(master,orient="horizontal",length=100,mode="determinate",maximum=self.player.MaxHP,value=self.player.HP,style="green.Horizontal.TProgressbar").pack(side="left",padx=(0,10))
                lvl=ttk.Label(master,text=f"LVL: {self.player.Lvl}").pack(side="left",padx=(0,10))
                lvl_bar=ttk.Progressbar(master,orient="horizontal",length=50,mode="determinate",maximum=self.player.EXP_needed_to_lvl_up,value=self.player.EXP,style="blue.Horizontal.TProgressbar").pack(side="left",padx=(0,10))
                eq_weapon=ttk.Label(master,text=f"Equiped weapon: {self.player.Equiped_Weapon["name"]}").pack(side="left",padx=(0,10))
            else:
                name.configure(text=f"Name: {self.player.name}")
                hp.configure(text=f"HP: ")
                hp_bar.configure(maximum=self.player.MaxHP,value=self.player.HP)
                lvl.configure(text=f"LVL: {self.player.Lvl}")
                lvl_bar.configure(maximum=self.player.EXP_needed_to_lvl_up,value=self.player.EXP)
                eq_weapon.configure(text=f"Equiped weapon: {self.player.Equiped_Weapon["name"]}")
        self.clear_widgets()
        self.root.geometry("700x600")
        main_menu_frame=ttk.LabelFrame(self.root,relief="raised",text="Stats")
        main_menu_frame.grid(row=0,column=0,columnspan=10,padx=2,pady=2)
        self.root.columnconfigure((0,1,2),weight=1)
        create_user_stats("create",main_menu_frame)

        ttk.Button(text="Fight",command=self.fight,width=12).grid(row=3,column=0)
        ttk.Button(text="Explore",command=self.explore,width=12).grid(row=3,column=1)
        ttk.Button(text="Talk to NPC",command=self.talk,width=12).grid(row=3,column=2)
        
        # ttk.Label(main_menu_frame,text=f"LVL: {self.player.Lvl}").pack(side="left")
        # ttk.Label(main_menu_frame,text=f": {self.player.}").pack(side="left")
        




#only for testing

root=tk.Tk()
PyGamme=PythonGame(root)
root.mainloop()
"""
text_varible updates contents of label when changed

def function():
    for i in range(5):
        var.set(i)
        root.update()
        time.sleep(1) # to slow down

root.after(1, function)

"""