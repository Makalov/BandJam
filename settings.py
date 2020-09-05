
class Settings:
    def __init__(self):
        self.activity_list = ["Activity Z", "Activity Y", "Activity X", "Activity W", "Activity V", "Activity U", "Activity T", "Activity S"]
        self.stat_list = ["A", "B", "C", "D", "E", "F", "G"]

        #set up activity dictionary structure
        self.activity_dict = {}

        #make an empty dictionary for each activity
        for i in self.activity_list:
            self.activity_dict[i]={}

        #fill out the activity actions
        self.activity_dict["Activity Z"]= {"A":2, "F":-2}
        self.activity_dict["Activity Y"]= {"A":-2, "B":2, "D":1}
        self.activity_dict["Activity X"]= {"B":-2, "G":2, "C":-1}
        self.activity_dict["Activity W"]= {"C": 2, "G":2, "A":-1}
        self.activity_dict["Activity V"]= {"D": 2, "F":2, "A":-1}
        self.activity_dict["Activity U"]= {"D": -2, "E":-2, "G":1}
        self.activity_dict["Activity T"]= {"F":2, "G":2, "C":-1}
        self.activity_dict["Activity S"]= {"A":1, "C":-2, "E":2, "F":-1}