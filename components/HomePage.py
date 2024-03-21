import tkinter as tk
from tkinter import *
from tkinter import ttk

import os


def HomePage(self):
        #Texto 
        self.label_s = tk.Label(self.master, text='', font=('Calibri', 100))
        self.label_s.grid(row=0, column=0, columnspan=2)

        self.image = PhotoImage(file="assets/banner_reiscar.png")

        #Texto 
        self.label_img = tk.Label(self.master, image=self.image, font=('Calibri', 13))
        self.label_img.grid(row=0, column=0, columnspan=2, rowspan=15)

        #Botão Criar Novo
        self.botao_create = tk.Button(self.master, text='Criar Novo Serviço', font=('Calibri', 13), bg='#6a88b5', command=self.new_server, width=45)
        self.botao_create.grid(row=1, rowspan=1, pady=5, padx=5, column=0, columnspan=2)

        #Entry Serviço
        datas = []
        nomes_arquivos = os.listdir()
        for nome_arquivo in nomes_arquivos:
            if '.json' in nome_arquivo:
                datas.append(nome_arquivo[:-5])
        datas = datas[:-1]

        def listar_sus(*args):
            new_datas = []
            for data1 in datas:
                if (self.enter_data.get()).upper() in data1:
                    new_datas.append(data1)
            if self.enter_data == '':
                new_datas = datas

            self.enter_data.config(values=new_datas)

        #Texto
        self.label_select = tk.Label(self.master, text='OU SELECIONE UM JÁ EXISTENTE', font=('Calibri', 13), bg="black", fg="white")
        self.label_select.grid(row=2, column=0, columnspan=2)

        #Entry Data
        self.entry_var_data = tk.StringVar()
        self.enter_data = ttk.Combobox(self.master, font=('Calibri', 13), width=36, values=datas, textvariable=self.entry_var_data, validate = "key")
        self.enter_data.grid(row=3, column=0,pady=0, padx=5)
        ttk.Style().configure("TCombobox", fieldbackground="#DCDCDC")

        #Botão Criar Novo
        self.botao_open = tk.Button(self.master, text='Abrir', font=('Calibri', 13), bg='#6a88b5', command=self.open_server, width=7)
        self.botao_open.grid(row=3, rowspan=1, pady=0, padx=0, column=1, columnspan=1)

        self.entry_var_data.trace_add("write", listar_sus)