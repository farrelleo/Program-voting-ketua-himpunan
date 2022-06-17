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

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    
    def updateVoteData(self):
        df = pd.read_csv("Data Voting.csv", sep=";", names=["NIM", "Nama", "Vote"])
        a = df["Vote"].str.contains('1').astype('int').sum()
        b = df["Vote"].str.contains('2').astype('int').sum()
        self.calon1.set(a)
        self.calon2.set(b)
        print(self.calon1.get())
        
    def showBar(self):
        vote_calon1 = self.calon1.get()
        vote_calon2 = self.calon2.get()
        vote_data = {'Farrell':vote_calon1, 'Fari':vote_calon2}
        courses = list(vote_data.keys())
        values = list(vote_data.values())
        
        fig = plt.figure(figsize=(4.5,4.5))
        fig.canvas.manager.set_window_title('Vote Pemilihan KAHIM HMTI 2023')
        # fig.patch.set_facecolor('#051536')
        barlist = plt.bar(courses, values,
                width = 0.3)
        
        
        barlist[0].set_color('red')
        barlist[1].set_color('blue')
        
        plt.xlabel("Calon")
        plt.ylabel("Jumlah Vote")
        plt.title("Vote Pemilihan KAHIM HMTI 2023")
        plt.show()
    
    def isVoted(self, nim, nama):
        try:
            df = pd.read_csv("Data Voting.csv", sep=";", names=["NIM", "Nama", "Vote"])
            print(df)
            if df['NIM'].str.contains(str(nim).upper()).any() or df['Nama'].str.contains(str(nama).capitalize()).any():
                messagebox.showerror("Gagal Voting", "Maaf User Dengan Nama Atau NIM Ini Sudah Melakukan Voting")
                return True
            else:
                print("This user not vote yet")
                return False
        except FileNotFoundError:
            data = {
                'NIM': ['NIM'],
                'Nama': ['Nama'],
                'Vote': ['Vote']
            }
            df = pd.DataFrame(data)
            df.to_csv('Data Voting.csv', mode='a', header=False, index=False, sep=";")
            print("File not found.")
            return True
        except pd.errors.EmptyDataError:
            data = {
                'NIM': ['NIM'],
                'Nama': ['Nama'],
                'Vote': ['Vote']
            }
            df = pd.DataFrame(data)
            df.to_csv('Data Voting.csv', mode='a', header=False, index=False, sep=";")
            print("No data")
            return True
        
    def voting(self, nama, nim, pil, con):
        voted = self.isVoted(nim, nama)
        if(not voted):
            data = {
                'NIM': [str(nim).upper()],
                'Nama': [str(nama).capitalize()],
                'Vote': [pil]
            }
            df = pd.DataFrame(data)
            df.to_csv('Data Voting.csv', mode='a', header=False, index=False, sep=";")
            self.updateVoteData()
            messagebox.showinfo("Berhasil Voting", "Terimakasih Atas Voting Anda")
            self.show_frame("StartPage")


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        controller.updateVoteData()
        self.config(bg="#051536")
        label = tk.Label(self, text="SELAMAT DATANG DI PROGRAM\nPEMILIHAN KAHIM HMTI 2023", font=controller.title_font, bg="#051536", fg="white")
        label.pack(side="top", fill="x", pady=70)

        button1 = tk.Button(self, text="Melakukan Voting",
                            command=lambda: [controller.show_frame("VotePage")])
        button2 = tk.Button(self, padx=16 , text="Hasil Voting",
                            command=lambda: [controller.showBar()])
        button1.pack(pady=5)
        button2.pack(pady=5)


class VotePage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="#051536")
        pil = IntVar()
        nama = StringVar()
        nim = StringVar()
        pil.set(1)
        label_input = tk.Label(self, text='Masukkan Nama Lengkap Anda : ', font=tkfont.Font(family='Helvetica', size=12, weight="bold"), bg="#051536", fg="white")
        input_nama = tk.Entry(self, textvariable=nama,width=50)
        label_input.pack(pady=40)
        input_nama.pack(padx=10, pady=10, ipady=7)
        label_input2 = tk.Label(self, text='Masukkan NIM Anda : ', font=tkfont.Font(family='Helvetica', size=12, weight="bold"), bg="#051536", fg="white")
        input_nim = tk.Entry(self,textvariable=nim,width=50)
        label_input2.pack()
        input_nim.pack(padx=10, pady=10, ipady=7)
        values = {"1. Farrell / 2021" : "1",
                "2. Fari / 2021" : "2"}
        
        for (text, value) in values.items():
            Radiobutton(self, text = text, variable = pil, value = value, bg="#051536", fg="white", selectcolor="#051536",font=tkfont.Font(family='Helvetica', size=11, weight="bold")).pack(side = TOP, ipady = 5)
        btn_submit = tk.Button(self, padx=20, text="Vote", background="#32a852", foreground="#fff",
                           command=lambda: [controller.voting(getNama(),getNIM(),getPil(),self),clearInput()])
        btn_submit.pack(pady=5)
        button = tk.Button(self, padx=8, text="Kembali", background="#ff0000", foreground="#fff",
                           command=lambda: [controller.show_frame("StartPage")])
        button.pack(pady=10)
        def getNama():
            return input_nama.get()
        def getNIM():
            return input_nim.get()
        def getPil():
            print(pil.get(),getNama(),getNIM())
            return pil.get()
        def clearInput():
            nama.set("")
            nim.set("")
        

if __name__ == "__main__":
    app = Vote()
    app.mainloop()
