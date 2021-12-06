
class Settings:
    def __init__(self):
        self.activity_list = ["Activity Z", "Activity Y", "Activity X", "Activity W", "Activity V", "Activity U", "Activity T", "Activity S"]
        self.weekend_activity_list = ["Weekend Activity 1"]
        self.stat_list = ["Charisma", "Creativity", "Vitality", "Technical Skill", "Street Cred", "Intelligence", "Energy"]

        #set up activity dictionary structure
        self.activity_dict = {}
        self.weekend_activity_dict = {}

        #make an empty dictionary for each activity
        for i in self.activity_list:
            self.activity_dict[i]={}
        for j in self.weekend_activity_list:
            self.weekend_activity_dict[j]={}

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

        #set up bandmate dictionary structure
        self.bandmate_dict = {}

        #populate bandmate stats
        self.bandmate_dict["10"]= {}
        self.bandmate_dict["10"]["Name"]="Character 1"
        self.bandmate_dict["10"]["Creativity"]= {"Above":59}
        self.bandmate_dict["10"]["Technical Skill"]={"Above":50}
        self.bandmate_dict["10"]["Intelligence"] = {"Above":30}

        self.bandmate_dict["11"]= {}
        self.bandmate_dict["11"]["Name"]="Character 1A"
        self.bandmate_dict["11"]["Creativity"]= {"Above":50}

        self.bandmate_dict["12"]= {}
        self.bandmate_dict["12"]["Name"]="Character 1B"
        self.bandmate_dict["12"]["Technical Skill"]={"Above":40} 
        
        self.bandmate_dict["13"]= {}
        self.bandmate_dict["13"]["Name"]="Character 1C"
        self.bandmate_dict["13"]["Intelligence"]={"Above":25} 

        self.bandmate_dict["20"]={}
        self.bandmate_dict["20"]["Name"]="Character 2"
        self.bandmate_dict["20"]["Charisma"]= {"Above":40}
        self.bandmate_dict["20"]["Creativity"]={"Equal":0}
        self.bandmate_dict["20"]["Intelligence"] = {"Below":30} 

        self.bandmate_dict["21"]={}
        self.bandmate_dict["21"]["Name"]="Character 2A"
        self.bandmate_dict["21"]["Charisma"]= {"Above":40}

        self.bandmate_dict["22"]={}
        self.bandmate_dict["22"]["Name"]="Character 2B"
        self.bandmate_dict["22"]["Creativity"]={"Equal":0}

        self.bandmate_dict["23"]={}
        self.bandmate_dict["23"]["Name"]="Character 2C"
        self.bandmate_dict["23"]["Intelligence"]={"Above":25} 

        self.bandmate_dict["30"]= {}
        self.bandmate_dict["30"]["Name"]="Character 3"
        self.bandmate_dict["30"]["Vitality"]= {"Above":30}
        self.bandmate_dict["30"]["Street Cred"]={"Above":50}
        self.bandmate_dict["30"]["Intelligence"] = {"Below":20}

        self.bandmate_dict["31"]={}
        self.bandmate_dict["31"]["Name"]="Character 3A"
        self.bandmate_dict["31"]["Vitality"]= {"Above":40}

        self.bandmate_dict["32"]={}
        self.bandmate_dict["32"]["Name"]="Character 3B"
        self.bandmate_dict["32"]["Street Cred"]={"Above":40}

        self.bandmate_dict["40"]= {}
        self.bandmate_dict["40"]["Name"]="Character 4"
        self.bandmate_dict["40"]["Technical Skill"]= {"Below":30}
        self.bandmate_dict["40"]["Creativity"]={"Below":25}
        self.bandmate_dict["40"]["Energy"] = {"Above":55}

        self.bandmate_dict["41"]={}
        self.bandmate_dict["41"]["Name"]="Character 4A"
        self.bandmate_dict["41"]["Creativity"]= {"Below":20}

        self.bandmate_dict["42"]={}
        self.bandmate_dict["42"]["Name"]="Character 4B"
        self.bandmate_dict["42"]["Technical Skill"]={"Below":25}

        self.bandmate_dict["43"]={}
        self.bandmate_dict["43"]["Name"]="Character 4C"
        self.bandmate_dict["43"]["Energy"] = {"Above":50}

        self.bandmate_dict["50"]= {}
        self.bandmate_dict["50"]["Name"]="Character 5"
        self.bandmate_dict["50"]["Vitality"]= {"Above":50}
        self.bandmate_dict["50"]["Energy"] = {"Above":30}

        self.bandmate_dict["60"]= {}
        self.bandmate_dict["60"]["Name"]="Character 6"
        self.bandmate_dict["60"]["Charisma"]= {"Below":30}
        self.bandmate_dict["60"]["Intelligence"] = {"Above":55}
        self.bandmate_dict["60"]["Energy"] = {"Below":30}
        
        self.bandmate_dict["70"]= {}
        self.bandmate_dict["70"]["Name"]="Character 7"
        self.bandmate_dict["70"]["Charisma"]= {"Below":20}
        self.bandmate_dict["70"]["Creativity"] = {"Below":20}
        self.bandmate_dict["70"]["Technical Skill"] = {"Above":60}       

        self.bandmate_dict["71"]={}
        self.bandmate_dict["71"]["Name"]="Character 7A"
        self.bandmate_dict["71"]["Charisma"]= {"Below":25}

        self.bandmate_dict["72"]={}
        self.bandmate_dict["72"]["Name"]="Character 7B"
        self.bandmate_dict["72"]["Technical Skill"]={"Above":60}
        
        self.bandmate_dict["80"]= {}
        self.bandmate_dict["80"]["Name"]="Character 8"
        self.bandmate_dict["80"]["Charisma"]= {"Above":45}
        self.bandmate_dict["80"]["Technical Skill"] = {"Below":5}
        self.bandmate_dict["80"]["Street Cred"] = {"Below":5}          
        
        self.bandmate_dict["81"]={}
        self.bandmate_dict["81"]["Name"]="Character 8A"
        self.bandmate_dict["81"]["Technical Skill"]= {"Below":10}

        self.bandmate_dict["82"]={}
        self.bandmate_dict["82"]["Name"]="Character 8B"
        self.bandmate_dict["82"]["Street Cred"]={"Below":10}    

        self.bandmate_dict["90"]= {}
        self.bandmate_dict["90"]["Name"]="Character 9"
        self.bandmate_dict["90"]["Charisma"]= {"Above":40}
        self.bandmate_dict["90"]["Street Cred"] = {"Above":50}
        self.bandmate_dict["90"]["Energy"] = {"Above":40}   

        self.bandmate_dict["100"]= {}
        self.bandmate_dict["100"]["Name"]="Character 10"
        self.bandmate_dict["100"]["Vitality"]= {"Below":20}
        self.bandmate_dict["100"]["Street Cred"] = {"Below":20}         
        
    def get_primary_list(self):
        #returns a list of primary bandmates in the game
        primary_bandmate_list = []
        for i in self.bandmate_dict.keys():
            #the index's are set up so only the ones divisible by 10s are primary members
            if int(i) % 10 == 0:
                primary_bandmate_list.append(i)
        return primary_bandmate_list

    def get_secondary_list(self,primary_bandmate):
        #returns a list of secondary bandmates associated with the primary_bandmate passed in
        secondary_bandmate_list = []
        for i in self.bandmate_dict.keys():
            #the index's are set up so the secondary is between 1-9 above its primary
            if int(i) > int(primary_bandmate) and int(i) < (int(primary_bandmate)+10):
                secondary_bandmate_list.append(i)
        return secondary_bandmate_list

