import tkinter as tk
from tkinter import PhotoImage
from fpdf import FPDF
import sqlite3
from datetime import datetime
from tkinter import *
from tkinter import ttk, messagebox
import os
import csv
import json
import sqlite3

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Rich Cat - Auxiliar Financeiro")
        self.root.geometry("1600x1000")
        
        try:
            root.iconbitmap("none.ico")
        except:
            pass

        self.conn = sqlite3.connect('platycon.db')
        self.c = self.conn.cursor()

        self.criar_widgets()

    def criar_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame para conteúdo principal (lado esquerdo)
        conteudo_frame = ttk.Frame(main_frame)
        conteudo_frame.pack(fill=tk.BOTH, expand=True, anchor=tk.NW)
        
        # Frame de botões alinhado à esquerda
        botoes_frame = ttk.Frame(conteudo_frame)
        botoes_frame.pack(side=tk.LEFT, padx=(0, 20), pady=30, anchor=tk.NW)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()