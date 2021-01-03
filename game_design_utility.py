# coding=utf-8

import json
from tkinter import *
import tkinter as tk
from tkinter import ttk
from settings import *
import random

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
            
        # set up row number variable to increment to easily insert a row
        rownum = 1

        # Add buttons to load bandmates
        Label(self.input_frame, text="Add Primary Bandmate").grid(row = rownum, column = 1)
        self.add_bandmate_button = Button(self.input_frame, text = "Add Primary Bandmate", command=self.add_primary_bandmate)
        self.add_bandmate_button.grid(row = rownum, column = 2)

        Label(self.input_frame, text="Add Secondary Bandmate").grid(row = rownum, column = 1)
        self.add_bandmate_button = Button(self.input_frame, text = "Add Secondary Bandmate", command=self.add_secondary_bandmate)
        self.add_bandmate_button.grid(row = rownum, column = 3)
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
        
    def add_primary_bandmate(self):
        #grab all primary bandmate's indexes and put them in a list
        primary_list = []
        for i in self.setting.bandmate_dict.keys():
            #the index's are set up so only the ones divisible by 10s are primary members
            if int(i) % 10 == 0:
                primary_list.append(i)

        #grab a random index
        bandmate_index = random.choice(primary_list)

        #create a new window with the band_member's stats
        popup = Tk()
        popup.wm_title(bandmate_index)
        Label(popup, text="Band Member Name").grid(row = 1, column = 1)
        bandmate_rownum = 2
        for stat in self.setting.bandmate_dict[bandmate_index].keys():
            Label(popup, text=stat).grid(row=bandmate_rownum, column = 1)
            stat_limit = str(self.setting.bandmate_dict[bandmate_index][stat])
            Label(popup, text=stat_limit).grid(row=bandmate_rownum, column = 2)
            bandmate_rownum +=1
        Button(popup, text="Kill", command = popup.destroy).grid(row = bandmate_rownum, column = 1)
        popup.mainloop()

    def add_secondary_bandmate(self):
        #grab all primary bandmate's indexes
        primary_list = []
        print(self.setting.bandmate_dict.keys())
        for i in self.setting.bandmate_dict.keys():
            print(i)
            if i % 10 == 0:
                primary_list.append(i)
        print(primary_list)


        print(random.choice(foo))
        popup = Tk()
        popup.wm_title("!")
        msg = "boo"
        label = ttk.Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Kill", command = popup.destroy)
        B1.pack()
        popup.mainloop()

    def do_activity(self):
        #figure out what activity to do by looking at what's selected in the drop down list
        today_activity = self.activity.get()

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

        #create a line that adds to the bottom of the output
        csv_line = '{},{}'.format(self.day_count, today_activity)
        output_line = 'Day:'+csv_line
        for i in self.setting.stat_list:
            output_line += ", {}:{} ".format(i, self.stat[i]["Value"])
            csv_line += ",{}".format(self.stat[i]["Value"])

        self.csv_output.append(csv_line)
        self.output.append(output_line)
        self.output_textbox.insert(tk.END, output_line+"\n")
        #print(self.output)


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
    root.mainloop()
