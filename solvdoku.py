# Sudoku Solved
# 	Author: drzacek
#	Date: 13.11.2022
#	Description:
#		A simple tool for solving sudoku games
#
version="1.0"
#	Changes:
#
#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#	#


# Imports
#import sys
#import os.path
#from os import path
#import re
#from datetime import datetime
#import statistics
import tkinter as tk
#import subprocess
import time
from PIL import Image
from PIL import ImageTk
#import webbrowser

# Variables
BUTTON_H = 3
BUTTON_W = 10
BUTTON_Hpx = 64
BUTTON_Wpx = 72


RES_PATH = r'./'
PROJECT_NAME = r'SUDOKU SOLVER'



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.update()
        
    def printcon(self, text):
        self.console.delete('1.0', tk.END)
        self.console.insert(tk.END, text)
        
    def printconlist(self, list):
        # In longer outputs, clear everything before printing
        self.console.delete('1.0', tk.END)
        
        for entry in list:
            self.console.insert(tk.END, entry)
        
    def create_widgets(self):
        # Frames, aka "panels" or grouping widgets
        self.panel_1 = tk.Frame(self)
        self.panel_1.pack(side="top")
        self.label1 = tk.Label(self.panel_1, text="MENU")
        self.label1.pack(side="top")
        
        # Second row of useful programs
        self.panel_2 = tk.Frame(self)
        self.panel_2.pack(side="top")
        
        # SUDOKU GRID
        self.panel_3 = tk.Frame(self)
        self.panel_3.pack(side="top")
        
        self.panel_sudoku = [0 for a in range(9)]
        
        for i in range(9):
            self.panel_sudoku[i] = tk.Frame(self.panel_3)
            self.panel_sudoku[i].pack(side="top")
        
        self.cells = [[0 for a in range(9)] for b in range(9)] 
        for y in range(9):
            for x in range(9):
                    self.cells[x][y] = tk.Entry(self.panel_sudoku[y], width=2, font=("Courier", 30), justify="center", validate="all", validateCommand=self.validateCell())
                    self.cells[x][y].pack(side="left")

        # CONSOLE / EXIT
        self.panel_4 = tk.Frame(self)
        self.panel_4.pack(side="top")
        self.label4 = tk.Label(self.panel_3, text="Console")
        self.label4.pack(side="top")
        
        
        
    # Menu Buttons
        pilimg1 = Image.open(RES_PATH+"logo.png").resize((48, 48), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(pilimg1)
        self.button1 = tk.Button(self.panel_2, text="New", height=BUTTON_Hpx, width=BUTTON_Wpx, image=self.img1, compound="top")
        self.button1["command"] = self.cmd_button1
        self.button1.pack(side="left")
        
        pilimg1 = Image.open(RES_PATH+"logo.png").resize((48, 48), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(pilimg1)
        self.button2 = tk.Button(self.panel_2, text="Open", height=BUTTON_Hpx, width=BUTTON_Wpx, image=self.img2, compound="top")
        self.button2["command"] = self.cmd_button2
        self.button2.pack(side="left")
        
        pilimg1 = Image.open(RES_PATH+"logo.png").resize((48, 48), Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(pilimg1)
        self.button3 = tk.Button(self.panel_2, text="Revert", height=BUTTON_Hpx, width=BUTTON_Wpx, image=self.img2, compound="top")
        self.button3["command"] = self.cmd_button3
        self.button3.pack(side="left")

    # Sudoku Grid

    # Quit + Time button 
        self.quit = tk.Button(self.panel_3, text="EXIT\n", fg="green",
                              command=self.master.destroy, height=BUTTON_H, width=BUTTON_W*5)
        self.quit.pack(side="bottom")
        
        self.console = tk.Text(self.panel_3, height=4, width=40)
        self.console.pack(side="bottom")
        

    # Functions
    def update(self):
        now = time.strftime("EXIT\n" + "%H:%M:%S")
        self.quit["text"] = now
        self.after(1000, self.update)

        
    def cmd_button1(self):
        self.printcon("New game - enter the initial digits")
        #subprocess.Popen(['pythonw3', r'F:\\bin\\fajrant.pyw'])
    
    def cmd_button2(self):
        self.printcon("Open game from text file (check FAQ and README for the proper file format)")
        #subprocess.Popen(['pythonw3', r'F:\\bin\\fajrant.pyw'])
    
    def cmd_button3(self):
        self.printcon("Revert grid to the initial state")
        #subprocess.Popen(['pythonw3', r'F:\\bin\\fajrant.pyw'])

    def validateCell(self):
        print("ghu")
        #self.printcon("Validating cell...")


root = tk.Tk()
root.iconbitmap("logo.ico")
app = Application(master=root)
root.title(PROJECT_NAME + version)
root.update()
app.mainloop()