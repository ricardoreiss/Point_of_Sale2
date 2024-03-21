from tkinter import *
import tkinter as tk

def ServicePage(self):
        self.label_s.destroy()
        self.label_img.destroy()
        self.botao_create.destroy()
        self.label_select.destroy()
        self.enter_data.destroy()
        self.botao_open.destroy()
        self.__init__(master=self.master, data=self.data)
        self.create_widgets()
        self.add_bbtc()
        
def clean_ent(self):
    self.enter_desc.delete(0, 'end')
    self.enter_Qtd.destroy()
    self.enter_valUnit.destroy()
    self.enter_valUnit = tk.Entry(self.master, font=('Calibri', 20), width=6, validate="key", validatecommand=(self.validacao_numeros, "%S"))
    self.enter_valUnit.grid(row=12, column=7, sticky='e')
    self.enter_Qtd = tk.Entry(self.master, font=('Calibri', 20), width=4, validate="key")
    self.enter_Qtd['validatecommand'] = (self.enter_Qtd.register(self.testVal),'%P','%d')
    self.enter_Qtd.grid(row=12, column=8)