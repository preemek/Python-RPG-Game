from typing import Literal
import Player
import Enemy
from Location import village, forest, castle
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class PythonGame:
    def __init__(self,root:tk.Tk,locations=[village,forest,castle]):
        self.player=Player.Player()
        # self.fight_counter=0 # i dont know how to make that without making varible here
        self.locations=locations
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
        self.root.geometry("600x300+400+200")
        root.columnconfigure(1,weight=1)
        root.columnconfigure(0,weight=1)
        root.rowconfigure(3,weight=1)
        ttk.Label(self.root,text="Welcome to Python RPG game",style="Blackadder.TLabel",anchor="center").grid(row=0,column=0,columnspan=2,pady=(30,0),sticky="EW")
        ttk.Label(self.root,text="by Wiktor Durek",anchor="center").grid(row=1,column=0,columnspan=2,pady=(0,50),sticky="EW")
        ttk.Button(self.root,text="Create new character",command=self.new_character_window).grid(row=3,column=0,padx=(100,20),pady=(0,80),ipadx=10,sticky="ESN")
        ttk.Button(self.root,text="Load from save file",command=lambda:self.choose_save_file_window(option="load")).grid(row=3,column=1,padx=(20,100),pady=(0,80),ipadx=10,sticky="WSN")
    
    def game_over(self):
        self.root.destroy()
        messagebox.showinfo("Game over","you've been defeated, try again next time!")
    def choose_save_file_window(self,option:Literal["save","load"]):
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
        window.geometry("400x100+300+200")
        window.configure(background="#dcdad5")

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
        new_char_window.geometry('240x95+300+200')
        new_char_window.configure(background="#dcdad5")

        name_entry_label = ttk.Label(new_char_window,text='Enter your name:')
        name_entry = ttk.Entry(new_char_window,width=20,textvariable=name_var)
        close_button = ttk.Button(new_char_window,text="Confirm",width=12,command=button_on)

        name_entry_label.grid(row=0,column=0,sticky="W",padx=(10,0))
        name_entry.grid(row=0,column=1,sticky="E",padx=(0,10))
        close_button.grid(row=1,column=0,columnspan=2,sticky="ES",pady=(5,10),padx=10)

    def locate_player(self):
        for location in self.locations:
            if location.name == self.player.Location:
                return location
            
    def talk (self):
        location=self.locate_player()
        window=tk.Frame(self.root)
        window.grid(row=2,column=0,columnspan=4,pady=(40,100))
        listbox = tk.Listbox(window, height = 5, width = 15, bg = "#c6c4bf", activestyle = 'dotbox', font = ('Gabriola', 16,"bold"),fg = "black")
        listbox.pack()
        def on_select(event):
            w = event.widget
            index = int(w.curselection()[0])
            npc=location.talk()
            npc=npc[index]
            window.destroy()
            if npc["name"] != " Travel Person":
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
        dialog_label.grid(row=1,column=0,columnspan=4,pady=(10,0))
        def next_dialog():
            if len(dialog)==0:
                self.main_menu()
            else:
                text=dialog.pop(0)
                dialog_label.config(text=f"{text}")
        window=tk.Frame(self.root)
        window.grid(row=2,column=0,columnspan=4,pady=(40,100))
        ttk.Button(window,text="next",command=next_dialog).pack()

    def travel(self,npc):
        def quit():
            self.main_menu()
        def choose_location():
            def on_select(event):
                w = event.widget
                index = int(w.curselection()[0])
                self.player.Location="{}".format(self.locations[index].name)
                self.main_menu()
            
            Yes_Button.destroy()
            No_Button.destroy()


            window=tk.Frame(self.root)
            window.grid(row=2,column=0,columnspan=4,pady=(40,100))
            
            text=dialog.pop(0)
            dialog_label.config(text=text)
            listbox = tk.Listbox(window, height = 3,width=15, bg = "#c6c4bf", activestyle = 'dotbox', font = ('Gabriola', 16,"bold"),fg = "black")
            listbox.pack()
            listbox.bind('<<ListboxSelect>>', on_select)
            
            
            n=0 
            for location in (self.locations):
                listbox.insert(n, str(location.name))
                n+=1
            listbox.grid(row=2,column=0)

        dialog=npc["dialog"].splitlines()
        text=dialog.pop(0)
        dialog_label=ttk.Label(text=f"{text}")
        dialog_label.grid(row=1,column=0,columnspan=4)
        
        Yes_Button=ttk.Button(text="Yes",command=choose_location,width=10)
        Yes_Button.grid(row=2,column=1,pady=10)
        No_Button=ttk.Button(text="No",command=quit,width=10)
        No_Button.grid(row=2,column=2,pady=10)
        

    def explore (self):
        location=self.locate_player()
        event=location.exploration()
        if event=="loot":
            pass
    def fight (self,stats:ttk.Labelframe):
        self.counter=0
        def fight():
                
            Yes_Button.destroy()
            No_Button.destroy()
            information_label.destroy()

            def enemy_defeated():
                log.insert(tk.END,f"you've just defeated {enemy.name}!")
                log.insert(tk.END,f"you've recieved XP!")
                player_lvl_before=self.player.Lvl
                self.player.recieve_EXP(enemy.XP_on_death)
                if self.player.Lvl > player_lvl_before:
                    log.insert(tk.END,f"you've reached lvl {self.player.Lvl}!")

                for widget in stats.winfo_children():
                        widget.destroy()
                self.create_user_stats(stats)
                
                button.config(text="ok",command=self.main_menu)

            def progress_round():
                if self.counter%2==0:
                    player_turn()
                else:
                    enemy_turn()
                self.counter+=1

            def player_turn():
                player_dmg=self.player.attack()
                log.insert(tk.END,f"you've hit {enemy.name} for {player_dmg} dmg!")
                enemy.take_dmg(player_dmg)
                if enemy.hp <= 0:
                    enemy_defeated()
            
            def enemy_turn():
                enemy_dmg=enemy.attack()
                log.insert(tk.END,f"you've been hit by {enemy.name} for {enemy_dmg} dmg!")
                self.player.take_dmg(enemy_dmg)
                for widget in stats.winfo_children():
                    widget.destroy()
                self.create_user_stats(stats)
                if self.player.HP <= 0:
                    self.game_over()
            
            window=tk.Frame(self.root,background="#dcdad5")
            window.grid(row=4,column=0,columnspan=4,pady=20)
            log=tk.Listbox(window,height=5,width=40,background="#dcdad5",relief="sunken")
            log.pack(side="top")
            
            button=ttk.Button(window,text="attack",command=progress_round)
            button.pack(side="top")

        def quit():
            self.main_menu()

        location=self.locate_player()
        enemy:Enemy.Enemy=location.fight()
        if type(enemy)==str:
            if enemy == "no enemies":
                messagebox.showinfo("no enemies",f"there are no enemies in {location.name}")
                self.main_menu()
                return None
            
        information_label=ttk.Label(text=f"{enemy.name} has appeared! do you want to fight it?")
        information_label.grid(row=1,column=0,columnspan=4,pady=(10,0))
        Yes_Button=ttk.Button(text="Yes",command=fight,width=10)
        Yes_Button.grid(row=2,column=1,pady=10)
        No_Button=ttk.Button(text="No",command=quit,width=10)
        No_Button.grid(row=2,column=2,pady=10)
        
        
        
    def create_user_stats (self,master:tk.Tk):
        for widget in master.winfo_children():
            widget.destroy()
        ttk.Label(master,text=f"Name: {self.player.name}",width=16,font=('Blackadder ITC', 20,"bold")).pack(side="left",padx=10)
        ttk.Label(master,text=f"HP: ").pack(side="left",padx=(0,10))
        ttk.Progressbar(master,orient="horizontal",length=100,mode="determinate",maximum=self.player.MaxHP,value=self.player.HP,style="green.Horizontal.TProgressbar").pack(side="left",padx=(0,10))
        ttk.Label(master,text=f"LVL: {self.player.Lvl}").pack(side="left",padx=(0,10))
        ttk.Progressbar(master,orient="horizontal",length=50,mode="determinate",maximum=self.player.EXP_needed_to_lvl_up,value=self.player.EXP,style="blue.Horizontal.TProgressbar").pack(side="left",padx=(0,10))
        ttk.Label(master,text="Equiped weapon: {}".format(self.player.Equiped_Weapon["name"])).pack(side="left",padx=(0,10))
        ttk.Label(master,text=f"Location: {self.player.Location}").pack(side="left",padx=(0,10))

    def main_menu(self):
        
        self.clear_widgets_in_root()
        self.root.geometry("720x600+300+100")
        main_menu_frame=ttk.Labelframe(self.root,relief="raised",text="Stats")
        main_menu_frame.grid(row=0,column=0,columnspan=10,padx=2,pady=2)
        self.root.columnconfigure((0,1,2,3),weight=1)
        self.create_user_stats(main_menu_frame)
        self.player.Lvl=10
        ttk.Button(text="Fight",command=lambda:self.fight(main_menu_frame),width=12).grid(row=5,column=0,padx=(33,0))
        ttk.Button(text="Explore",command=self.explore,width=12).grid(row=5,column=1)
        ttk.Button(text="Talk to NPC",command=self.talk,width=12).grid(row=5,column=2)
        ttk.Button(text="save file",command=lambda:self.choose_save_file_window("save")).grid(row=5,column=3,padx=(0,33))
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