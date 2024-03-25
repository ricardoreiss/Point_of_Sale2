import tkinter as tk
from tkinter import *

def RenderShortcuts(self):
    self.root_listAta = tk.Tk()
    self.root_listAta.title('Lista-de-Atalhos')

    #Lista
    self.atalhos = """Ctrl+Enter: Gerar Nota Fiscal
Delete: Deletar Tudo
Backspace: Deletar Produto
Enter: Adicionar Produto
Seta-Baixo e Cima: Selecionar Produto
Double_Shift: Tirar Seleção
Ctrl+-Direita e Esquerda: Selecionar Entrada"""

    #Inserindo Lista
    self.label_ata = tk.Label(master=self.root_listAta, text=self.atalhos, anchor=W)
    self.label_ata.pack()