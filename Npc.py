
class Dialog:
    def __init__ (self,dialog_true:str,condition:str="True",needed_varibles:list[str]=[],dialog_false:str=None,dialog_true_is_last=False,dialog_false_is_last=False,reward_true:dict=None,reward_false:dict=None,add_event_to_story_true:str=None,add_event_to_story_false:str=None,command_to_execute_true:str=None,command_to_execute_false:str=None):
        
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
    def __init__(self,question:str,dialog_true:str,dialog_false:str=None,condition:str="True",yes_text:str="Yes",no_text:str="No",needed_varibles:list[str]=[],dialog_true_is_last=False,dialog_false_is_last=False,reward=None):
        super().__init__(dialog_true,condition,needed_varibles,dialog_false,dialog_true_is_last,dialog_false_is_last,reward)
        self.question=question
        self.yes_text=yes_text
        self.no_text=no_text

class NPC:
    def __init__(self,name:str,dialog_list:list[list[Dialog|YesNoDialog]]):
        """ ``dialog_list`` is a list of dialogs, first list contains another list wich can contain many dialog options for this one part"""
        for dialog_options in dialog_list:
            if dialog_options[len(dialog_options)-1].condition != "True" and dialog_options[len(dialog_options)-1].dialog_false is None:
                raise Exception("Last dialog option must have condition set to True or have dialog_false set to None, error occured in index {}".format(dialog_list.index(dialog_options)))
        self.dialog_list=dialog_list
        self.name=name
        
    def get_needed_varibles(self)->list:
        """returns list of needed varibles for all dialogs"""
        needed_varibles=[]
        for dialog_options in self.dialog_list:
            for dialog_option in dialog_options:
                needed_varibles.extend(dialog_option.needed_varibles_names)
        return needed_varibles
    
    def talk(self,index:int,varibles:dict)->dict:
        """for `varibles` use function to change needed varibles into dict, returns dict <keys>: `dialog`, `is_last_dialog`, `reward`, `add_event_to_story`, `is_question`. If is question then returns dict <keys>: `question`, `yes_text`, `no_text`, `is_question`, `varible` (returns YesNoDialog object)"""
    
        # print(varibles) #Testing only DELETE

        dialog = self.dialog_list[index]
        for dialog_option in dialog:
            for varible_name in dialog_option.needed_varibles_names:
                if varible_name not in varibles.keys():
                    raise Exception("Needed varibles are not provided, missing varible: '{}'".format(varible_name))
            
            try:
                if eval(f"{dialog_option.condition}", globals(), varibles):
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
                    
            except NameError as e:
                print(e)
            except Exception as e:
                print(e)

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
                "is_last_dialog":None,
                "reward":None,
                "add_event_to_story":None,
                "command":None,
                "is_question":False}

bartek = NPC("bartek",[[YesNoDialog("how are you","nice")],
                       [Dialog("1 apple?","False",dialog_false="oh nevermind",needed_varibles=["self.player.HP"])]])

kali =NPC("kali",[[Dialog("hej")],
                  [Dialog("jak sie masz?")],
                  [Dialog("no to pa")]])

"""
def turn_varibles_into_dict(list_of_varibles)->dict:
    dict={}
    for i in list_of_varibles:
        try:
            dict[i]=eval("{}".format(i))
        except NameError:
            raise Exception("Needed varible '{}' is not provided".format(i))
        except Exception as e:
            print(type(e),e)
    return dict
"""

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