# coding=utf-8

import json
from tkinter import *
import tkinter as tk
from tkinter import ttk

class GameDesignUtility:
    
    def __init__(self, master):
        #setup output
        self.output = []

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

        # Create an activity and a stat list, will load from file later
        self.activity_list = ["Activity Z", "Activity Y", "Activity X", "Activity W", "Activity V", "Activity U", "Activity T"]
        self.stat_list = ["A", "B", "C", "D", "E", "F", "G"]

        #set up stat dictionary with initial stat values
        self.stat = {}
        for i in self.stat_list:
            self.stat[i] = {}
            self.stat[i]["Value"] = 30

        #set up activity dictionary with what they do, will load from file later
        self.activity_dict = {}
        for i in self.activity_list:
            self.activity_dict[i]={}
        self.activity_dict["Activity Z"]= {"A":2, "F":-2}
        self.activity_dict["Activity Y"]= {"A":-2, "B":2, "D":1}
        self.activity_dict["Activity X"]= {"B":-2, "G":2, "C":-1}
        self.activity_dict["Activity W"]= {"C": 2, "G":2, "A":-1}
        self.activity_dict["Activity V"]= {"D": 2, "F":2, "A":-1}
        self.activity_dict["Activity U"]= {"D": -2, "E":-2, "G":1}
        self.activity_dict["Activity T"]= {"F":2, "G":2, "C":-1}

        # Put Activity drop down on GUI
        self.event_menu = OptionMenu(self.input_frame, self.activity, *self.activity_list)
        Label(self.input_frame, text="Choose activity").grid(row = 1, column = 1)
        self.event_menu.grid(row = 1, column = 2)

        # Add button to perform activity
        self.activity_button = Button(self.input_frame, text = "Perform Activity", command=self.do_activity)
        self.activity_button.grid(row = 1, column = 3)
       
        # Add the stats boxes and the set stat buttons and populate with value
        rownum = 2
        for i in self.stat:
            Label(self.input_frame, text = i).grid(row = rownum, column = 1)
            self.stat[i]["Entrybox"] = tk.Entry(self.input_frame)
            self.stat[i]["Entrybox"].grid(row = rownum, column = 2)
            self.stat[i]["Entrybox"].insert(END, self.stat[i]["Value"])
        
            self.stat[i]["Set Button"] = Button(self.input_frame, text = "Set", command = self.set_stat)
            self.stat[i]["Set Button"].grid(row = rownum, column = 3)

            rownum += 1

        self.reset_button = Button(self.input_frame, text = "Reset Game", command = self.reset)
        self.reset_button.grid(row = rownum, column = 2)

        self.save_button = Button(self.input_frame, text = "Save to file", command = self.save_to_file)
        self.save_button.grid(row = rownum, column = 3)
        

    def do_activity(self):
        #figure out what activity to do by looking at what's selected in the drop down list
        today_activity = self.activity.get()
        #cycle through the stat increases in the activity and add it to the stat
        for i in self.activity_dict[today_activity]:
            self.stat[i]["Value"] += self.activity_dict[today_activity][i]
            self.stat[i]["Entrybox"].delete(0,'end')
            self.stat[i]["Entrybox"].insert(END, self.stat[i]["Value"])
        
        #increment the day count
        self.day_count += 1

        #create a line that adds to the bottom of the output
        output_line = 'Day: {}, {}'.format(self.day_count, today_activity)
        for i in self.stat_list:
            output_line += ", Stat {}:{} ".format(i, self.stat[i]["Value"])

        self.output.append(output_line)
        self.output_textbox.insert(tk.END, output_line+"\n")
        print(self.output)


    def set_stat(self):
        pass


    def save_to_file(self):
        pass


    def reset(self):
        for i in self.stat_list:
            self.stat[i] = {}
            self.stat[i]["Value"] = 30
            self.stat[i]["Entrybox"].grid(row = rownum, column = 2)
            self.stat[i]["Entrybox"].insert(END, self.stat[i]["Value"])
        self.output = {}
        self.output_textbox.delete(1.0,END)


if __name__ == "__main__":
    root = Tk()
    Test1 = GameDesignUtility(root)
    root.mainloop()
