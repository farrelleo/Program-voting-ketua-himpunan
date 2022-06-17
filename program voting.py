import csv
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt


class Vote(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.calon1 = IntVar()
        self.calon2 = IntVar()
        self.title("VOTING")
        self.title_font = tkfont.Font(family='Helvetica', size=15, weight="bold")
        self.geometry("500x500")
        self.resizable(False, False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, VotePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")