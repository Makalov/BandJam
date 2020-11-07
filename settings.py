
class Settings:
    def __init__(self):
        self.activity_list = ["Activity Z", "Activity Y", "Activity X", "Activity W", "Activity V", "Activity U", "Activity T", "Activity S"]
        self.stat_list = ["Charisma", "Creativity", "Vitality", "Technical Skill", "Street Cred", "Intelligence", "Energy"]

        #set up activity dictionary structure
        self.activity_dict = {}

        #make an empty dictionary for each activity
        for i in self.activity_list:
            self.activity_dict[i]={}

        #fill out the activity actions
        self.activity_dict["Activity Z"]= {"Charisma":2, "Intelligence":-2}
        self.activity_dict["Activity Y"]= {"Charisma":-2, "Creativity":2, "Technical Skill":1}
        self.activity_dict["Activity X"]= {"Creativity":-2, "Energy":2, "Vitality":-1}
        self.activity_dict["Activity W"]= {"Vitality": 2, "Energy":-2, "Charisma":-1}
        self.activity_dict["Activity V"]= {"Technical Skill": 2, "Intelligence":2, "Charisma":-1}
        self.activity_dict["Activity U"]= {"Technical Skill": -2, "Street Cred":-2, "Energy":1}
        self.activity_dict["Activity T"]= {"Intelligence":2, "Energy":2, "Vitality":-1}
        self.activity_dict["Activity S"]= {"Charisma":1, "Vitality":-2, "Street Cred":2, "Intelligence":-1}

        #set up stats dictionary structure
        self.stat_dict = {}
        #make an empty dictionary for each stat
        for i in self.stat_list:
            self.stat_dict[i]={}

        #set default, maximum and minimum values
        self.stat_dict["Charisma"]= {"Max":60, "Min":0, "Default":30}
        self.stat_dict["Creativity"]= {"Max":60, "Min":0, "Default":30}
        self.stat_dict["Vitality"]= {"Max":60, "Min":0, "Default":30}
        self.stat_dict["Technical Skill"]= {"Max":60, "Min":0, "Default":30}
        self.stat_dict["Street Cred"]= {"Max":60, "Min":0, "Default":30}
        self.stat_dict["Intelligence"]= {"Max":60, "Min":0, "Default":30}
        self.stat_dict["Energy"]= {"Max":60, "Min":0, "Default":30}



