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
        self.style.configure("Blackadder.TLabel",font=('Blackadder ITC', 20,"bold"))
        self.style.configure("TLabelframe.Label",font=('Gabriola', 16,"bold"),foreground="black")
        self.style.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')
        self.style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
        
        self.start()
    
    def clear_widgets_in_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
    def start(self):
        self.root.geometry("600x300+500+200")
        root.columnconfigure(1,weight=1)
        root.columnconfigure(0,weight=1)
        root.rowconfigure(3,weight=1)
        ttk.Label(self.root,text="Welcome to Python RPG game",style="Blackadder.TLabel",anchor="center").grid(row=0,column=0,columnspan=2,pady=(30,0),sticky="EW")
        ttk.Label(self.root,text="by Wiktor Durek",anchor="center").grid(row=1,column=0,columnspan=2,pady=(0,50),sticky="EW")
        ttk.Button(self.root,text="Create new character",command=self.new_character_window).grid(row=3,column=0,padx=(100,20),pady=(0,80),ipadx=10,sticky="ESN")
        ttk.Button(self.root,text="Load from save file",command=lambda:self.choose_save_file_window(option="load")).grid(row=3,column=1,padx=(20,100),pady=(0,80),ipadx=10,sticky="WSN")
    
    def choose_save_file_window(self,option=""):
        def button_on(number):
            if option=="load":
                try:
                    self.player.create_player("from_save_file",file_number=number)
                    root.columnconfigure(1,weight=0)
                    root.columnconfigure(0,weight=0)
                    root.rowconfigure(3,weight=0)
                    self.main_menu()
                    window.destroy()
                except FileNotFoundError:
                    messagebox.showerror(title="File not found!",message=f"file {number} doesn't exist")
            if option=="save":
                self.player.save_player_data(file_number=number)
                window.destroy()

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
            new_char_window.destroy()
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
        scrollbar = tk.Scrollbar(self.root)
        listbox = tk.Listbox(self.root, height = 10, width = 15, bg = "#c6c4bf", activestyle = 'dotbox', font = ('Gabriola', 16,"bold"),fg = "black",yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        def on_select(event):
            w = event.widget
            index = int(w.curselection()[0])
            npc=location.talk()
            npc=npc[index]
            listbox.destroy()
            if npc["name"] != " Travel Person":
                # print(npc["name"])
                self.normal_dialog(npc)
            else:
                self.travel(npc)
                
                

        listbox.bind('<<ListboxSelect>>', on_select)
        n=0 
        for npc in location.talk():
            listbox.insert(n, str(npc["name"]))
            n+=1
        listbox.grid(row=2,column=0)
        #after npc selection
    def normal_dialog(self,npc):
        
        dialog=npc["dialog"].splitlines()
        text=dialog.pop(0)
        dialog_label=ttk.Label(text=f"{text}")
        dialog_label.grid(row=1,column=0,columnspan=4)
        def next_dialog():
            if len(dialog)==0:
                self.main_menu()
            else:
                text=dialog.pop(0)
                dialog_label.config(text=f"{text}")
        ttk.Button(text="next",command=lambda:next_dialog()).grid(row=2,column=0)

    def travel(self,npc):
        def quit():
            self.main_menu()
        def choose_location():
            def on_select(event):
                print("hii")
            Yes_Button.destroy()
            No_Button.destroy()

            text=dialog.pop(0)
            dialog_label.config(text=text)
            scrollbar = tk.Scrollbar(self.root)
            listbox = tk.Listbox(self.root, height = 2, width = 15, bg = "#c6c4bf", activestyle = 'dotbox', font = ('Gabriola', 16,"bold"),fg = "black",yscrollcommand=scrollbar.set)
            scrollbar.config(command=listbox.yview)
            listbox.bind('<<ListboxSelect>>', on_select)
            n=0 
            print(self.locations)
            for i in range(5):
                listbox.insert(i,f"hii{i}")
            # for location in self.locations:
            #     listbox.insert(n, str(location[0].name))
            #     n+=1
            listbox.grid(row=2,column=0)

        dialog=npc["dialog"].splitlines()
        text=dialog.pop(0)
        dialog_label=ttk.Label(text=f"{text}")
        dialog_label.grid(row=1,column=0,columnspan=4)
        
        Yes_Button=ttk.Button(text="Yes",command=choose_location,width=10)
        Yes_Button.grid(row=2,column=1)
        No_Button=ttk.Button(text="No",command=quit,width=10)
        No_Button.grid(row=2,column=2)
        
        

    def explore (self):
        location=self.locate_player()
        event=location.exploration()
        if event=="loot":
            pass
    def fight (self):
        pass
        
    def main_menu(self):
        def create_user_stats (master=None):
            for widget in master.winfo_children():
                widget.destroy()
            ttk.Label(master,text=f"Name: {self.player.name}",width=16,font=('Blackadder ITC', 20,"bold")).pack(side="left",padx=10)
            ttk.Label(master,text=f"HP: ").pack(side="left",padx=(0,10))
            ttk.Progressbar(master,orient="horizontal",length=100,mode="determinate",maximum=self.player.MaxHP,value=self.player.HP,style="green.Horizontal.TProgressbar").pack(side="left",padx=(0,10))
            ttk.Label(master,text=f"LVL: {self.player.Lvl}").pack(side="left",padx=(0,10))
            ttk.Progressbar(master,orient="horizontal",length=50,mode="determinate",maximum=self.player.EXP_needed_to_lvl_up,value=self.player.EXP,style="blue.Horizontal.TProgressbar").pack(side="left",padx=(0,10))
            ttk.Label(master,text="Equiped weapon: {}".format(self.player.Equiped_Weapon["name"])).pack(side="left",padx=(0,10))

        self.clear_widgets_in_root()
        self.root.geometry("700x600")
        main_menu_frame=ttk.LabelFrame(self.root,relief="raised",text="Stats")
        main_menu_frame.grid(row=0,column=0,columnspan=10,padx=2,pady=2)
        self.root.columnconfigure((0,1,2,3),weight=1)
        create_user_stats(main_menu_frame)
        self.player.Lvl=10
        ttk.Button(text="Fight",command=self.fight,width=12).grid(row=3,column=0,padx=(33,0))
        ttk.Button(text="Explore",command=self.explore,width=12).grid(row=3,column=1)
        ttk.Button(text="Talk to NPC",command=self.talk,width=12).grid(row=3,column=2)
        ttk.Button(text="save file",command=lambda:self.choose_save_file_window("save")).grid(row=3,column=3,padx=(0,33))
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