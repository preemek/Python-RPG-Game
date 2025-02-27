from typing import Literal
import Player
import Enemy
from Location import village, forest, castle
from Location import location
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Npc import NPC
from Npc import Palladin, Witch

class PythonGame:
    def __init__(self,root:tk.Tk,locations=[village,forest,castle]):
        self.player=Player.Player()
        self.locations:list[location]=locations # stores location class objects
        self.root=root
        self.root.title("Python RPG Game")
        self.root.configure(background="#dcdad5")
        self.root.resizable(width=0,height=0)
        self.stats=ttk.Labelframe(self.root,relief="raised",text="Stats")
        # styles
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
        """clear all widgets in ``self.root``"""
        for widget in self.root.winfo_children():
            if widget != self.stats:
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

    def Witch_ending (self):
        self.root.destroy()
        messagebox.showinfo("Game over","And... As a follower of that Mysterious Witch, you'll follow her and embark on a new journey")
    
    def Palladin_ending (self):
        self.root.destroy()
        messagebox.showinfo("Game over","And... As a follower of a great knight, you'll follow him and follow his path")

    def turn_varibles_into_dict(self,list_of_varibles:list[str])->dict:
        dict={}
        for varible in list_of_varibles:
            try:
                varible_modified=varible.replace(".","")
                dict[varible_modified]=eval("{}".format(varible))
            except NameError:
                raise Exception("Needed varible '{}' is not provided".format(varible))
            except Exception as e:
                print(type(e),e)
        return dict

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
                self.main_menu()
                window.destroy()

        window=tk.Toplevel(self.root)
        window.title("Choose save file")
        window.geometry("400x100+300+200")
        window.configure(background="#dcdad5")
        if option=="save":
            window.protocol("WM_DELETE_WINDOW",lambda:[window.destroy(),self.main_menu()])

        window.columnconfigure((0,1,2),weight=1)
        window.rowconfigure(0,weight=1)
        ttk.Button(window,text="Save 1", command=lambda:button_on(1)).grid(row = 0, column = 0, pady=30, padx=30, sticky = "NESW")
        ttk.Button(window,text="Save 2", command=lambda:button_on(2)).grid(row = 0, column = 1, pady=30, padx=0, sticky = "NESW")
        ttk.Button(window,text="Save 3", command=lambda:button_on(3)).grid(row = 0, column = 2, pady=30, padx=30, sticky = "NESW")

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

    def locate_player(self) -> location:
        """returns ``location`` object of current player location"""
        for location in self.locations:
            if location.name == self.player.Location:
                return location
            
    def talk (self): # choosing npc
        location=self.locate_player()
        window=tk.Frame(self.root)
        window.grid(row=2,column=0,columnspan=4,pady=(40,100))
        listbox = tk.Listbox(window, height = 5, width = 15, bg = "#c6c4bf", activestyle = 'dotbox', font = ('Gabriola', 16,"bold"),fg = "black")
        listbox.pack()
        def on_select(event:tk.Event):
            w:tk.Listbox = event.widget
            index = int(w.curselection()[0])
            npc=location.talk()
            npc:NPC=npc[index]
            window.destroy()
            if npc.name != "Travel_Person":
                self.normal_dialog(npc)
            else:
                self.player.Location=self.choose_location()

        listbox.bind('<<ListboxSelect>>', on_select)
        
        for npc in location.talk():
            listbox.insert(tk.END, str(npc.name))
        listbox.grid(row=2,column=0)

    def normal_dialog(self,npc:NPC):
        def proces_information (text):
            print(text) # <----------here is a print
            if text["dialog"] is not None:
                dialog_label.config(text=f"{text["dialog"]}")
            if text["reward"] is not None:
                self.player.found_item(text["reward"])
            if text["command"] is not None:
                exec("{}".format(text["command"])) #just hope that npc doesnt accidentaly have some bad commands that will break programm
            if text["add_event_to_story"]:
                self.player.story_events.add(text["add_event_to_story"])
            if text["is_last_dialog"]:
                btt.configure(text="close",command=self.main_menu)
            if text["dialog"] is None and not text["is_last_dialog"]:
                if len(iterator)==0:
                    btt.configure(text="close",command=self.main_menu)
                else:
                    print("automatic next dialog") # <---- her is a print
                    next_dialog(iterator.pop(0))
            
 
        def next_dialog(iterator):
            print(iterator)
            text=npc.talk(iterator,self.turn_varibles_into_dict(npc.get_needed_varibles()))
            if text["is_question"]:
                def answer(answer):
                    yes_btt.destroy()
                    no_btt.destroy()
                    btt.configure(state="normal")
                    proces_information(npc.get_result_for_question(answer,text["dialog_varible"]))

                # print("question {}".format(iterator)) # <----------here is a print
                dialog_label.config(text=text["question"])
                yes_btt=ttk.Button(window,text=text["yes_text"],command=lambda:answer(True),width=5)
                yes_btt.pack(side="left",pady=5,padx=(0,20))
                no_btt=ttk.Button(window,text=text["no_text"],command=lambda:answer(False),width=5)
                no_btt.pack(side="right",pady=5)
                btt.configure(state="disabled")

            else:
                # print("triggered proces info {}".format(iterator)) # <----------here is a print
                proces_information(text)

            if iterator==len(npc.dialog_list)-1:
                print("closing dialog")
                btt.configure(text="close",command=self.main_menu)


        dialog_label=ttk.Label(text="")
        dialog_label.grid(row=1,column=0,columnspan=4,pady=(10,0))
        
        window=tk.Frame(self.root,background="#dcdad5")
        window.grid(row=2,column=0,columnspan=4,pady=(40,100))

        btt=ttk.Button(window,text="next",command=lambda:next_dialog(iterator.pop(0)))
        btt.pack(side="bottom")

        iterator=list(range(0,len(npc.dialog_list)))
        print(iterator)
        next_dialog(iterator.pop(0)) #first dialog appears right after choosing npc

    def choose_location(self):
        new_location=tk.StringVar()
        def on_select(event:tk.Event):
            w:tk.Listbox = event.widget
            index = int(w.curselection()[0])
            new_location.set("{}".format(self.locations[index].name))

        window=tk.Frame(self.root)
        window.grid(row=2,column=0,columnspan=4,pady=(40,100))
        
        dialog_label=ttk.Label(text="choose location")
        dialog_label.grid(row=1,column=0,columnspan=4)
        listbox = tk.Listbox(window, height = 3,width=15, bg = "#c6c4bf", activestyle = 'dotbox', font = ('Gabriola', 16,"bold"),fg = "black")
        listbox.pack()
        listbox.bind('<<ListboxSelect>>', on_select)
        
        for location in self.locations:
            listbox.insert(tk.END, str(location.name))
        listbox.grid(row=2,column=0)

        window.wait_variable(new_location) # might cause errors idk
        window.destroy()
        dialog_label.destroy()
        return(new_location.get())
        
    def explore (self):
        def quit():
            self.main_menu()
        location=self.locate_player()
        event=location.exploration()

        if event=="loot":
            found_item = location.draw_random_item()
            ttk.Label(text="You have just found {}".format(found_item["name"])).grid(row=1,column=0,columnspan=4)
            self.player.found_item(found_item)
            ttk.Button(text="continue",command=self.main_menu).grid(row=2,column=1,pady=20)

        if event=="wishing well":
            def throw_coin():
                if self.player.Gold > 0:
                    self.player.Gold-=1

                    found_item=location.draw_from_wishing_well()
                    if found_item!="nothing":
                        wishing_well_label.configure(text="You have just found {}\n you have {} Gold".format(found_item["name"],self.player.Gold))
                        self.player.found_item(found_item)
                    else:
                        wishing_well_label.configure(text="There's nothing here, try again\n you have {} Gold".format(self.player.Gold))

                else:
                    wishing_well_label.configure(text="You don't have any gold left")

            wishing_well_label=ttk.Label(text="you have found a wishing well\n you have {} Gold".format(self.player.Gold),justify="center")
            wishing_well_label.grid(row=2,column=0,columnspan=4)
            
            ttk.Button(text="throw coin",command=throw_coin).grid(row=3,column=0,columnspan=2,sticky="e",padx=(0,177),pady=(10,50))
            ttk.Button(text="leave",command=quit).grid(row=3,column=1,columnspan=2,sticky="w",padx=(177,0),pady=(10,50))
    
    def fight (self):
        self.counter=0
        def quit():
            self.main_menu()
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

                self.create_user_stats()
                
                button.config(text="continue",command=self.main_menu)

            def progress_round():
                if self.counter%2==0:
                    button.config(text="enemy's turn")
                    player_turn()
                else:
                    button.config(text="your turn")
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
                self.create_user_stats()
                if self.player.HP <= 0:
                    self.game_over()
            
            window=tk.Frame(self.root,background="#dcdad5")
            window.grid(row=2,column=0,columnspan=3,pady=20)
            button=ttk.Button(window,text="attack",command=progress_round)
            button.pack(side="bottom")
            log=tk.Listbox(window,height=5,width=40,background="#dcdad5",relief="sunken")
            log.pack(side="right",padx=(10,0))
            
            

        location=self.locate_player()
        enemy:Enemy.Enemy=location.fight()
        if type(enemy)==str:
            if enemy == "no enemies":
                messagebox.showinfo("no enemies",f"there are no enemies in {location.name}")
                self.main_menu()
                return None
            
        information_label=ttk.Label(text=f"{enemy.name} has appeared! do you want to fight it?")
        information_label.grid(row=1,column=0,columnspan=3,pady=(10,0))
        Yes_Button=ttk.Button(text="Yes",command=fight,width=10)
        No_Button=ttk.Button(text="No",command=quit,width=10)

        Yes_Button.grid(row=2,column=0,columnspan=2,sticky="e",padx=(0,177),pady=10)
        No_Button.grid(row=2,column=1,columnspan=2,sticky="w",padx=(177,0),pady=10)
        # ttk.Button(text="inventory",command=self.open_inventory).grid(row=6,column=0,columnspan=2,sticky="e",padx=(0,177),pady=10)
        # ttk.Button(text="save file",command=lambda:self.choose_save_file_window("save")).grid(row=6,column=1,columnspan=2,sticky="w",padx=(177,0),pady=10)
        
    def open_inventory (self):
        def use():
            item_name=inventory.get(int(inventory.curselection()[0]))
            item_name=item_name.split(" x")[0]
            self.player.use_item(item_name)
            self.create_user_stats()
            inventory.delete(0,tk.END)
            inventory.insert(tk.END,f"Gold x{self.player.Gold}")
            for item in self.player.Items.values():
                inventory.insert(tk.END,f"{item["name"]} x{item["quantity"]}")
        def item_info():
            item_name=inventory.get(int(inventory.curselection()[0]))
            item_name=item_name.split(" x")[0]
            window=tk.Toplevel()
            window.title("Item info")
            window.resizable(width=0,height=0)
            window.configure(background="#dcdad5")
            try:
                for key, value in self.player.Items[item_name].items():
                    ttk.Label(window,text=f"{key}: {value}").pack(padx=10,pady=(0,10))
            except Exception as err:
                print(err)

        window=tk.Toplevel()
        window.title("Inventory")
        window.resizable(width=0,height=0)
        window.configure(background="#dcdad5")
        window.protocol("WM_DELETE_WINDOW",lambda:[window.destroy(),self.main_menu()])
        
        inventory = tk.Listbox(window,height=5,width=40,background="#dcdad5",relief="sunken")
        inventory.grid(row=2,column=1,pady=20)
        

        ttk.Button(window,text="close",command=self.main_menu).grid(row=3,column=0,pady=10,padx=(10,0),sticky="e")
        ttk.Button(window,text="use",command=use).grid(row=3,column=1,pady=10)
        ttk.Button(window,text="info",command=item_info).grid(row=3,column=2,pady=10,padx=(0,10),sticky="w")
        
        inventory.insert(tk.END,f"Gold x{self.player.Gold}")
        for item in self.player.Items.values():
            inventory.insert(tk.END,f"{item["name"]} x{item["quantity"]}")
        
    def create_user_stats (self,master="none"):
        if master=="none":
            master=self.stats
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
        """clears all widgets in root, creates main menu"""
        def disable_buttons():
            for widget in self.root.winfo_children():
                if type(widget) == ttk.Button:
                    widget.configure(state="disabled")
                    
        self.clear_widgets_in_root()
        self.root.geometry("730x600+300+100")
        
        self.stats.grid(row=0,column=0,columnspan=10,padx=2,pady=2)
        self.root.columnconfigure((0,1,2),weight=1)
    
        self.create_user_stats()

        #disable buttons after choice
   
        ttk.Separator(self.root, orient="horizontal").grid(row=4,column=0, columnspan=3, sticky="ew",padx=40)

        ttk.Button(text="Fight",command=lambda:[disable_buttons(),self.fight()],width=12).grid(row=5,column=0,padx=(33,0),pady=(10,0))
        ttk.Button(text="Explore",command=lambda:[disable_buttons(),self.explore()],width=12).grid(row=5,column=1,pady=(10,0))
        ttk.Button(text="Talk to NPC",command=lambda:[disable_buttons(),self.talk()],width=12).grid(row=5,column=2,padx=(0,33),pady=(10,0))
        ttk.Button(text="inventory",command=lambda:[disable_buttons(),self.open_inventory()]).grid(row=6,column=0,columnspan=2,sticky="e",padx=(0,177),pady=10)
        ttk.Button(text="save file",command=lambda:[disable_buttons(),self.choose_save_file_window("save")]).grid(row=6,column=1,columnspan=2,sticky="w",padx=(177,0),pady=10)
        
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