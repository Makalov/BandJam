# coding=utf-8

import json
from tkinter import *
import tkinter as tk
from tkinter import ttk
from settings import *
import random
import functools

class GameDesignUtility:
    
    def __init__(self, master):
        #setup output
        self.output = []
        self.setting = Settings()

        #setup csv file output
        self.csv_output = []
        self.csv_output.append("Day,Activity,Charisma,Creativity,Vitality,Technical SKill,Street Cred,Intelligence,Energy,Note")

        #setup variable to keep track of game date
        self.day_count = 0

        # Add the base frame. Two frames sits aon this base frame, the left input frame and the right output frame
        self.master = master
        self.master.title("Game Design Utility")
        self.mainframe = Frame(master)
        self.mainframe.pack(pady = 20, padx = 20)

        #set up input frame on the left
        self.left_frame = Frame(self.mainframe, width=400)
        self.left_frame.pack(side=LEFT,padx=8,pady=8)
        self.input_frame = Frame(self.left_frame, width = 400)
        self.input_frame.grid(column=0,row=0, sticky=(N,W,E,S))
        self.input_frame.columnconfigure(0, weight = 1)
        self.input_frame.rowconfigure(0, weight = 1)
        self.input_frame.pack(side = TOP, fill = X, pady = 20, padx = 20)

        #setup output frame on the right
        self.output_frame = tk.LabelFrame(self.mainframe, text="output", bd = 5)
        self.output_frame.pack(side = RIGHT, padx = 8, pady = 8)
        self.output_scrollbar = tk.Scrollbar(self.output_frame)
        self.output_textbox = tk.Text(self.output_frame, width= 75)
        self.output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output_textbox.pack(side=tk.LEFT, fill=tk.Y)
        self.output_scrollbar.config(command=self.output_textbox.yview)
        self.output_textbox.config(yscrollcommand=self.output_scrollbar.set)

        # Create a Tkinter variable for activity drop down items
        self.activity = StringVar(master)
        self.activity.set("Activity Z")

        #set up stat dictionary with initial stat values
        self.stat = {}
        for i in self.setting.stat_list:
            self.stat[i] = {}
            self.stat[i]["Value"] = 30

        #set up array to store bandmates and a dictionary to store popup windows
        self.current_primary_bandmates = []
        self.current_secondary_bandmates = []
        self.primary_bandmate_to_quit = []
        self.secondary_bandmate_to_quit = []
        self.bandmate_popups = {}
            
        # set up row number variable to increment to easily insert a row
        rownum = 1

        # Add buttons to load bandmates
        self.add_bandmate_button = Button(self.input_frame, text = "Add Primary Bandmate", command=self.add_primary_bandmate)
        self.add_bandmate_button.grid(row = rownum, column = 1)

        self.add_bandmate_button = Button(self.input_frame, text = "Add Secondary Bandmate", command=self.add_secondary_bandmate)
        self.add_bandmate_button.grid(row = rownum, column = 2)

        # Add button to check for flags
        self.check_bandmate_button = Button(self.input_frame, text = "Check flags", command=self.check_bandmate_flag)
        self.check_bandmate_button.grid(row = rownum, column = 3)

        # Add button for end of month
        self.check_bandmate_button = Button(self.input_frame, text = "End of Month", command=self.end_of_month)
        self.check_bandmate_button.grid(row = rownum, column = 4)
        rownum += 1

        # Put Activity drop down on GUI
        self.event_menu = OptionMenu(self.input_frame, self.activity, *self.setting.activity_list)
        Label(self.input_frame, text="Choose activity").grid(row = rownum, column = 1)
        self.event_menu.grid(row = rownum, column = 2)

        # Add button to perform activity
        self.activity_button = Button(self.input_frame, text = "Perform Activity", command=self.do_activity)
        self.activity_button.grid(row = rownum, column = 3)
        rownum += 1

        # Add the stats boxes and the set stat buttons and populate with value
        for i in self.stat:
            Label(self.input_frame, text = i).grid(row = rownum, column = 1)
            self.stat[i]["Entrybox"] = tk.Entry(self.input_frame)
            self.stat[i]["Entrybox"].grid(row = rownum, column = 2)
            self.stat[i]["Entrybox"].insert(END, self.stat[i]["Value"])
            rownum += 1

        # Add a field for Day
        Label(self.input_frame, text = "Day #"). grid(row = rownum, column = 1)
        self.date_entrybox = tk.Entry(self.input_frame)
        self.date_entrybox.grid(row = rownum, column = 2)
        self.date_entrybox.insert(END, self.day_count)
        rownum += 1

        # Add textbox for notes
        self.notes_textbox = tk.Text(self.input_frame, width = 28, height=5)
        Label(self.input_frame, text = "Notes"). grid(row = rownum, column = 1)
        self.notes_textbox.grid(row=rownum, column = 2, columnspan = 2)
        self.notes_scrollbar = tk.Scrollbar(self.input_frame, command=self.notes_textbox.yview)
        self.notes_scrollbar.grid(row=rownum, column = 4, sticky='nsew')
        self.notes_textbox.config(yscrollcommand=self.notes_scrollbar.set)
        rownum += 1

        # Add button to save date and time
        self.set_button = Button(self.input_frame, text = "Set date and stats", command = self.set_all)
        self.set_button.grid(row=rownum, column = 2)

        self.reset_button = Button(self.input_frame, text = "Reset Game", command = self.reset)
        self.reset_button.grid(row = rownum, column = 3)
        rownum +=1

        # Add a field for File Name
        Label(self.input_frame, text = "File Name"). grid(row = rownum, column = 1)
        self.filename_entrybox = tk.Entry(self.input_frame)
        self.filename_entrybox.grid(row = rownum, column = 2)
        self.save_button = Button(self.input_frame, text = "Save to file", command = self.save_to_file)
        self.save_button.grid(row = rownum, column = 3)

        #initialize the 2 primary and 2 secondary bandmates
        self.add_primary_bandmate()
        self.add_primary_bandmate()
        self.add_secondary_bandmate()
        self.add_secondary_bandmate()


    def create_bandmate_window(self, bandmate_index):
        #draws the popup window for the bandmate
        self.bandmate_popups[bandmate_index] = Tk()
        self.bandmate_popups[bandmate_index].wm_title(bandmate_index)
        Label(self.bandmate_popups[bandmate_index], text="Band Member Name").grid(row = 1, column = 1)
        bandmate_rownum = 2
        for stat in self.setting.bandmate_dict[bandmate_index].keys():
            #print out all the stat conditions to be met for the character
            Label(self.bandmate_popups[bandmate_index], text=stat).grid(row=bandmate_rownum, column = 1)
            stat_cond = str(self.setting.bandmate_dict[bandmate_index][stat])
            Label(self.bandmate_popups[bandmate_index], text=stat_cond).grid(row=bandmate_rownum, column = 2)
            bandmate_rownum +=1
        Button(self.bandmate_popups[bandmate_index], text="Kill", command = lambda:self.remove_bandmate(bandmate_index)).grid(row = bandmate_rownum, column = 1)


    def add_primary_bandmate(self):

        if len(self.current_primary_bandmates) == 2:
            print("error, max primary bandmates reached")
            return
        
        new_bandmate_index = -1
        #repeat until we find a primary bandmate stat that's not already there
        if len(self.current_primary_bandmates) <2:
            while new_bandmate_index not in self.current_primary_bandmates:
                #grab a stat from the list
                new_bandmate_index = random.choice(self.setting.get_primary_list())
                #add stat if not there
                if new_bandmate_index not in self.current_primary_bandmates:
                    self.current_primary_bandmates.append(new_bandmate_index)
                    self.create_bandmate_window(new_bandmate_index)
                else: #else repeat the loop
                    new_bandmate_index = -1


    def add_secondary_bandmate(self):
        #create available secondary bandmate list based on current primary bandmates
        secondary_list = []
        for i in self.current_primary_bandmates:
            secondary_list += self.setting.get_secondary_list(i)
    
        #check if there is secondary bandmates available to add
        if secondary_list == []:
            print("error, no secondary bandmate available to add")
            return
        if set(secondary_list).issubset(set(self.current_secondary_bandmates)):
            print("error, no secondary bandmate available to add")
            return
        if len(self.current_secondary_bandmates) == 3:
            print("error, max secondary bandmates reached")
            return

        new_bandmate_index = -1
        #repeat until we find a primary bandmate stat that's not already there
        if len(self.current_secondary_bandmates) <3:
            while new_bandmate_index not in self.current_secondary_bandmates:
                #grab a stat from the list
                new_bandmate_index = random.choice(secondary_list)
                #add stat if not there
                if new_bandmate_index not in self.current_secondary_bandmates:
                    self.current_secondary_bandmates.append(new_bandmate_index)
                    self.create_bandmate_window(new_bandmate_index)
                else: #else repeat the loop
                    new_bandmate_index = -1 


    def check_bandmate_flag(self):
        #this function goes through each bandmate in the list and each of their attributes and check if their stats matches with their conditions
        current_bandmates = self.current_primary_bandmates + self.current_secondary_bandmates
        for i in current_bandmates:
            bandmate_flag = True
            #this following loops goes through each stat to see if they match, if any of them do not match they do not quit
            for stat in self.setting.bandmate_dict[i].keys():
                for condition in self.setting.bandmate_dict[i][stat].keys():
                    if condition == "Above":
                        if self.stat[stat]["Value"] <= self.setting.bandmate_dict[i][stat][condition]:
                            bandmate_flag = False
                    elif condition == "Equal":
                        if self.stat[stat]["Value"] < self.setting.bandmate_dict[i][stat][condition]:
                            bandmate_flag = False
                        elif self.stat[stat]["Value"] > self.setting.bandmate_dict[i][stat][condition]:
                            bandmate_flag = False
                    elif condition == "Below":
                        if self.stat[stat]["Value"] >= self.setting.bandmate_dict[i][stat][condition]:
                            bandmate_flag = False
            if bandmate_flag == True:
                if i in self.current_primary_bandmates:
                    if i not in self.primary_bandmate_to_quit:
                        self.primary_bandmate_to_quit.append(i)
                elif i not in self.secondary_bandmate_to_quit:
                    self.secondary_bandmate_to_quit.append(i)


    def remove_bandmate(self, bandmate_index):
        #remove the bandmate from list and close window
        self.bandmate_popups[bandmate_index].destroy()
        #delete the window object
        del self.bandmate_popups[bandmate_index]
        #remove the bandmate from the list of current bandmates
        if (int(bandmate_index) %10)== 0:
            self.current_primary_bandmates.remove(bandmate_index)
        else:
            self.current_secondary_bandmates.remove(bandmate_index)
 

    def do_activity(self):
        #figure out what activity to do by looking at what's selected in the drop down list
        today_activity = self.activity.get()

        for repeat_activity in range(5):
            #cycle through the stat increases in the activity and add it to the stat but also check if they are out of bound
            for i in self.setting.activity_dict[today_activity]:
                self.stat[i]["Value"] += self.setting.activity_dict[today_activity][i]

                #check if the values are maxed out or below minimum
                if self.stat[i]["Value"] >= self.setting.stat_dict[i]["Max"]:
                    self.stat[i]["Value"] = self.setting.stat_dict[i]["Max"]
                elif self.stat[i]["Value"] <= self.setting.stat_dict[i]["Min"]:
                    self.stat[i]["Value"] = self.setting.stat_dict[i]["Min"]
            
                #write the new value into the box
                self.stat[i]["Entrybox"].delete(0,'end')
                self.stat[i]["Entrybox"].insert(END, self.stat[i]["Value"])
        
            #increment the day count
            self.day_count += 1
            self.date_entrybox.delete(0,'end')
            self.date_entrybox.insert(END, self.day_count)

            #update flags
            self.check_bandmate_flag()

            #if the date passes the 28 mark do end of month tasks
            if (self.day_count % 28) == 0:
                self.end_of_month()

            #create a line that adds to the bottom of the output
            csv_line = '{},{}'.format(self.day_count, today_activity)
            output_line = 'Day:'+csv_line
            for i in self.setting.stat_list:
                output_line += ", {}:{} ".format(i, self.stat[i]["Value"])
                csv_line += ",{}".format(self.stat[i]["Value"])
            output_line +=", Primary Bandmates:{}, Secondary Bandmates: {}".format(self.current_primary_bandmates, self.current_secondary_bandmates)

            self.csv_output.append(csv_line)
            self.output.append(output_line)
            self.output_textbox.insert(tk.END, output_line+"\n")


    def end_of_month(self):
        #this function checks whether there is anybody flagged. If flagged then they quit, otherwise add another bandmate

        #add a bandmate if nobody quits, we can combine these but then it gets hard to read
        if len(self.primary_bandmate_to_quit) == 0 and len(self.secondary_bandmate_to_quit) == 0:
            #if there's no primary bandmates left
            if len(self.current_primary_bandmates) == 0:
                self.add_primary_bandmate()
            #if there's one primary bandmate and less than 2 secondary bandmate
            elif len(self.current_primary_bandmates) == 1 and len(self.current_secondary_bandmates) < 2:
                self.add_secondary_bandmate()
            #if there's one primary bandmate and 2 secondary bandmate
            elif len(self.current_primary_bandmates) == 1 and len(self.current_secondary_bandmates) == 2:
                self.add_primary_bandmate()
            #if there're two primary bandmates and less than 3 secondary bandmate
            elif len(self.current_primary_bandmates) == 2 and len(self.current_secondary_bandmates) < 3:
                self.add_secondary_bandmate()
        #if somebody quits then we remove that person
        else:
            for i in self.primary_bandmate_to_quit:
                self.remove_bandmate(i)
            for i in self.secondary_bandmate_to_quit:
                self.remove_bandmate(i)
        self.primary_bandmate_to_quit.clear()
        self.secondary_bandmate_to_quit.clear()

    def set_all(self):
        #this function sets everything
        
        #grab all the values from the boxes and save it to the game variables
        for i in self.setting.stat_list:
            self.stat[i]["Value"] = int(self.stat[i]["Entrybox"].get())
            self.day_count = int(self.date_entrybox.get())

        #create a line that adds to the bottom of the output
        output_line = 'Day: {}, manual set'.format(self.day_count)
        csv_line = '{},Manual Set'.format(self.day_count)
        for i in self.setting.stat_list:
            output_line += ", Stat {}:{} ".format(i, self.stat[i]["Value"])
            csv_line += ",{}".format(self.stat[i]["Value"])
        output_line += ", Note: {}".format(self.notes_textbox.get("1.0", END))  
        csv_line += ", {}".format(self.notes_textbox.get("1.0", END))  

        self.csv_output.append(csv_line)
        self.output.append(output_line)
        self.output_textbox.insert(tk.END, output_line+"\n")
        #print(self.output)


    def save_to_file(self):
        if self.filename_entrybox.get() == "":
            output_filename = "sample_output.csv"
        else:
            output_filename = (self.filename_entrybox.get() + ".csv")
        f = open(output_filename, "w")
        for i in self.csv_output:
            f.write(i+'\n')


    def reset(self):
        for i in self.setting.stat_list:
            self.stat[i]["Value"] = self.setting.stat_dict[i]["Default"]
            self.stat[i]["Entrybox"].delete(0,'end')
            self.stat[i]["Entrybox"].insert(END, self.stat[i]["Value"])
            self.day_count = 0
            self.date_entrybox.delete(0,'end')
            self.date_entrybox.insert(END, self.day_count)
        self.output = []
        self.output_textbox.delete(1.0,END)


if __name__ == "__main__":
    root = Tk()
    Test1 = GameDesignUtility(root)
    def on_closing():
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()
