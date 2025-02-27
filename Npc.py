
class Dialog:
    def __init__ (self,dialog_true:str=None,condition:str="True",needed_varibles:list[str]=[],dialog_false:str=None,dialog_true_is_last=False,dialog_false_is_last=False,reward_true:dict=None,reward_false:dict=None,add_event_to_story_true:str=None,add_event_to_story_false:str=None,command_to_execute_true:str=None,command_to_execute_false:str=None):
        
        self.condition=condition # "self.player.HP<=5 and self.player.MaxHP>=10" 
        self.needed_varibles_names=needed_varibles
        
        self.dialog_true=dialog_true
        self.dialog_true_is_last=dialog_true_is_last
        self.reward_true=reward_true #item
        self.add_event_to_story_true=add_event_to_story_true
        self.command_to_execute_true=command_to_execute_true

        self.dialog_false=dialog_false # not sure if i'll use it but it can be useful, ps: its usefull for yes/no questions
        self.dialog_false_is_last=dialog_false_is_last
        self.reward_false=reward_false #item
        self.add_event_to_story_false=add_event_to_story_false
        self.command_to_execute_false=command_to_execute_false
        
        
class YesNoDialog(Dialog):
    def __init__(self,question:str,yes_text:str="Yes",no_text:str="No",dialog_true:str=None,condition:str="True",needed_varibles:list[str]=[],dialog_false:str=None,dialog_true_is_last=False,dialog_false_is_last=False,reward_true:dict=None,reward_false:dict=None,add_event_to_story_true:str=None,add_event_to_story_false:str=None,command_to_execute_true:str=None,command_to_execute_false:str=None):
        super().__init__(dialog_true,condition,needed_varibles,dialog_false,dialog_true_is_last,dialog_false_is_last,reward_true,reward_false,add_event_to_story_true,add_event_to_story_false,command_to_execute_true,command_to_execute_false)
        self.question=question
        self.yes_text=yes_text
        self.no_text=no_text

class NPC:
    def __init__(self,name:str,dialog_list:list[list[Dialog|YesNoDialog]]):
        """ ``dialog_list`` is a list of dialogs, first list contains another list wich can contain many dialog options for this one part"""
        # for dialog_options in dialog_list:
        #     if dialog_options[len(dialog_options)-1].condition != "True" and dialog_options[len(dialog_options)-1].dialog_false is None:
        #         raise Exception("Last dialog option must have condition set to True or have dialog_false set to None, error occured in index {}".format(dialog_list.index(dialog_options)))
        self.dialog_list=dialog_list
        self.name=name
        
    def get_needed_varibles(self)->list:
        """returns list of needed varibles for all dialogs"""
        needed_varibles=set()
        for dialog_options in self.dialog_list:
            for dialog_option in dialog_options:
                for needed_varible in dialog_option.needed_varibles_names:
                    needed_varibles.add(needed_varible)
        return list(needed_varibles)
    
    def talk(self,index:int,varibles:dict)->dict:
        """for `varibles` use function to change needed varibles into dict, returns dict <keys>: `dialog`, `is_last_dialog`, `reward`, `add_event_to_story`, `is_question`. If is question then returns dict <keys>: `question`, `yes_text`, `no_text`, `is_question`, `varible` (returns YesNoDialog object)"""
    
        # print(varibles) #Testing only DELETE

        dialog = self.dialog_list[index]
        for dialog_option in dialog:
            for varible_name in dialog_option.needed_varibles_names:
                varible_name_modified=varible_name.replace(".","")
                if varible_name_modified not in varibles.keys():
                    raise Exception("Needed varibles are not provided, missing varible: {}".format(varible_name))
            
            try:
                condition_modified=dialog_option.condition.replace(".","")
                if eval(f"{condition_modified}", globals(), varibles):
                    if type(dialog_option) == YesNoDialog:
                        return {"question":dialog_option.question,
                                "yes_text":dialog_option.yes_text,
                                "no_text":dialog_option.no_text,
                                "dialog_varible":dialog_option,
                                "is_question":True}
                    else:
                        return {"dialog":dialog_option.dialog_true,
                                "is_last_dialog":dialog_option.dialog_true_is_last,
                                "reward":dialog_option.reward_true,
                                "add_event_to_story":dialog_option.add_event_to_story_true,
                                "command":dialog_option.command_to_execute_true,
                                "is_question":False}
                else:
                    if dialog_option.dialog_false is not None:
                        return {"dialog":dialog_option.dialog_false,
                                "is_last_dialog":dialog_option.dialog_false_is_last,
                                "reward":dialog_option.reward_false,
                                "add_event_to_story":dialog_option.add_event_to_story_false,
                                "command":dialog_option.command_to_execute_false,
                                "is_question":False}
                    
                    # return {"dialog":dialog_option.dialog_false,
                    #         "is_last_dialog":dialog_option.dialog_false_is_last,
                    #         "reward":dialog_option.reward_false,
                    #         "add_event_to_story":dialog_option.add_event_to_story_false,
                    #         "command":dialog_option.command_to_execute_false,
                    #         "is_question":False}
                    
            except NameError as e:
                print(e)
            except Exception as e:
                print(e)
        return {"dialog":dialog_option.dialog_false,
                "is_last_dialog":dialog_option.dialog_false_is_last,
                "reward":dialog_option.reward_false,
                "add_event_to_story":dialog_option.add_event_to_story_false,
                "command":dialog_option.command_to_execute_false,
                "is_question":False}
    
    def get_result_for_question (self,answer:bool,dialog_option:YesNoDialog)->dict:
        """returns dict <keys>: `dialog`, `is_last_dialog`, `reward`, `add_event_to_story`, `is_question`"""
        if answer:
            return {"dialog":dialog_option.dialog_true,
                    "is_last_dialog":dialog_option.dialog_true_is_last,
                    "reward":dialog_option.reward_true,
                    "add_event_to_story":dialog_option.add_event_to_story_true,
                    "command":dialog_option.command_to_execute_true,
                    "is_question":False}
        else:
            if dialog_option.dialog_false is not None:
                return {"dialog":dialog_option.dialog_false,
                        "is_last_dialog":dialog_option.dialog_false_is_last,
                        "reward":dialog_option.reward_false,
                        "add_event_to_story":dialog_option.add_event_to_story_false,
                        "command":dialog_option.command_to_execute_false,
                        "is_question":False}
            
        return {"dialog":None,
                "is_last_dialog":dialog_option.dialog_false_is_last,
                "reward":dialog_option.reward_false,
                "add_event_to_story":dialog_option.add_event_to_story_false,
                "command":dialog_option.command_to_execute_false,
                "is_question":False}

#if reaching for player values tpe self.player.<accesed varible>   
# '' in self.player.story_events


#witches items:
First_wand = {"type":"weapon","name":"First wand","dmg":1}

Witch = NPC("Witch",[[Dialog("Hello adventuer"," 'meet_witch_for_the_first_time' not in self.player.story_events",needed_varibles=["self.player.story_events"]),
                      Dialog("Don't you know what you need to do?")],

                     [Dialog("Are you looking for some cursed stuff?"," 'meet_witch_for_the_first_time' not in self.player.story_events",needed_varibles=["self.player.story_events"]),
                      Dialog("Oh wow, you've actually done it","self.player.Lvl >= 2 and 'Witch_quest_1_done' not in self.player.story_events",needed_varibles=["self.player.Lvl","self.player.story_events"]),
                      Dialog("You need to reach level 2, you're still too weak...","self.player.Lvl < 2 and 'Witch_quest_1_done' not in self.player.story_events",needed_varibles=["self.player.Lvl","self.player.story_events"],dialog_true_is_last=True)],

                     [Dialog("I actually have some i could give you"," 'meet_witch_for_the_first_time' not in self.player.story_events",needed_varibles=["self.player.story_events"]),
                      Dialog("well.., here is your reward","self.player.Lvl == 2 and 'Witch_quest_1_done' not in self.player.story_events",needed_varibles=["self.player.Lvl","self.player.story_events"],add_event_to_story_true="Witch_quest_1_done",reward_true=First_wand)],

                     [Dialog("But for now you're too weak for them, reach level 2 and then we'll talk"," 'meet_witch_for_the_first_time' not in self.player.story_events",needed_varibles=["self.player.story_events"],add_event_to_story_true="meet_witch_for_the_first_time",dialog_true_is_last=True),
                      Dialog("Now, you need to decide, do you want to be like me?","'Witch_quest_1_done' in self.player.story_events",needed_varibles=["self.player.story_events"])],
                    
                    [YesNoDialog("Do you want to take this dangerous path? it's irreversible",condition="'Witch_quest_1_done' in self.player.story_events",needed_varibles=["self.player.story_events"],add_event_to_story_true="Witch_path",command_to_execute_true="self.locations[2].list_of_NPC.pop(self.locations[2].list_of_NPC.index(Palladin))",dialog_false="Well, if you change your mind come back",dialog_false_is_last=True)]

                     ])
#palladins items
First_sword = {"type":"weapon","name":"First sword","dmg":1}

Palladin = NPC("Palladin",[[Dialog("Hello adventuer"," 'meet_palladin_for_the_first_time' not in self.player.story_events",needed_varibles=["self.player.story_events"]),
                      Dialog("What to do now?")],

                     [Dialog("Are you thinking of beacoming a palladin like me?"," 'meet_palladin_for_the_first_time' not in self.player.story_events",needed_varibles=["self.player.story_events"]),
                      Dialog("Im impressed by your progress,","self.player.Lvl >= 2 and 'Palladin_quest_1_done' not in self.player.story_events",needed_varibles=["self.player.Lvl","self.player.story_events"]),
                      Dialog("In order to prove yourself, you need to reach level 2","self.player.Lvl < 2 and 'Palladin_quest_1_done' not in self.player.story_events",needed_varibles=["self.player.Lvl","self.player.story_events"],dialog_true_is_last=True)],

                     [Dialog("If you do, you need to prove yourself"," 'meet_palladin_for_the_first_time' not in self.player.story_events",needed_varibles=["self.player.story_events"]),
                      Dialog("Take this, it will be your first step to beacoming a palladin like me","self.player.Lvl == 2 and 'Palladin_quest_1_done' not in self.player.story_events",needed_varibles=["self.player.Lvl","self.player.story_events"],add_event_to_story_true="Palladin_quest_1_done",reward_true=First_sword)],

                     [Dialog("Reach level 2 and then you'll be able to take my path"," 'meet_palladin_for_the_first_time' not in self.player.story_events",needed_varibles=["self.player.story_events"],add_event_to_story_true="meet_palladin_for_the_first_time",dialog_true_is_last=True),
                      Dialog("Now, you need to decide","'Palladin_quest_1_done' in self.player.story_events",needed_varibles=["self.player.story_events"])],
                    
                    [YesNoDialog("Do you want to take this holy path? it's irreversible",condition="'Palladin_quest_1_done' in self.player.story_events",needed_varibles=["self.player.story_events"],add_event_to_story_true="Palladin_path",command_to_execute_true="self.locations[1].list_of_NPC.pop(self.locations[1].list_of_NPC.index(Witch))",dialog_false="If you ever change your mind, come back",dialog_false_is_last=True)]

                     ])


Healer =NPC("Healer",[[Dialog("Hello!")],
                  [Dialog("Oh i see that you're hurt",condition="self.player.HP!=self.player.MaxHP",needed_varibles=["self.player.HP","self.player.MaxHP"],dialog_false="If you ever need to heal yourself, come to me",dialog_false_is_last=True)],

                  [Dialog("That should do it",condition="self.player.HP!=self.player.MaxHP",needed_varibles=["self.player.HP","self.player.MaxHP"],command_to_execute_true="self.player.HP=self.player.MaxHP")]
                  ])

Travel_Person = NPC("Travel Person",[[YesNoDialog("Wanna have a ride?",dialog_false_is_last=True)],
                                     
                                     [Dialog("Bye",command_to_execute_true="self.player.Location=self.choose_location()")]
                                     ])

Bartek = NPC("Bartek",[[Dialog("Welcome to our town")],
                       [Dialog("Here you can recover your health points and chat with us")]
                       ])

Mysterious_Man = NPC("Mysterious Man",[[Dialog("So you've chosen a dangeorus path...","'Witch_path' in self.player.story_events",needed_varibles=["self.player.story_events"]),Dialog("I see that you've chosen to be a holy knigh...","'Palladin_path' in self.player.story_events",needed_varibles=["self.player.story_events"]),Dialog("I've heard that in the forest there is a Witch")],
                                       [Dialog("","'Witch_path' in self.player.story_events",needed_varibles=["self.player.story_events"],command_to_execute_true="self.Witch_ending()",dialog_true_is_last=True),Dialog("","'Palladin_path' in self.player.story_events",needed_varibles=["self.player.story_events"],command_to_execute_true="self.Palladin_ending()",dialog_true_is_last=True),Dialog("Also I've heard that in the castle there is a Palladin")],
                                       [Dialog("After you talk to them and take their path, come back to me after you choose")]
                                       ])


# print(Healer.talk(1,{"selfplayerHP":10,"selfplayerMaxHP":10}))
# print(Witch.talk(0,{"selfplayerstory_events":["meet_witch_for_the_first_time"]}))


#just paste this into your code, into a place where it can acces needed varibles
# delete self paramiter if this function isn't in class obj 

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

# for i in range(len(bartek.dialog_list)):
#     print(i)
    # dialog=bartek.talk(i,turn_varibles_into_dict(bartek.get_needed_varibles()))
#     print(dialog["dialog"])
#     if dialog["is_last_dialog"]:
#         break
# dialog=bartek.talk(0,turn_varibles_into_dict(bartek.get_needed_varibles()))
# print(dialog["varible"])
# print(dialog["question"])
# message=bartek.get_result_for_question(False,dialog["varible"])

# print(message["dialog"])