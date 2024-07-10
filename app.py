import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel
from tkcalendar import DateEntry
from tkinter import filedialog
import json
import os

from components.ServiceClass import Service
from components.HomePage import HomePage
from components.ServicePage import ServicePage
from components.ServicePage import clean_ent
from components.CreateServiceNote import CreateServiceNote
from components.RenderShortcuts import RenderShortcuts
from components.Widget import Widget

# Abrir o arquivo JSON e carregar os dados
with open("orderserver.json", "r") as file_json:
    val_orderserver = json.load(file_json)

old_service = ''
def def_address(address):
    global old_service
    address
    old_service = False
    if address:
        with open(address + ".json", "r") as file_json:
            old_service = json.load(file_json)

class Application(tk.Frame):
    def __init__(self, master = None, data = None):
        super().__init__(master)
        self.master = master
        self.val_orderserver = val_orderserver
        self.servico = Service(f"{(val_orderserver['ordem de servico'][-1] + 1):06d}", '', '', data, '', '', '', '', '', '', '', '', [])
        self.old_service = old_service
        if old_service:
            self.servico = Service(old_service['ordem'], old_service['ncliente'], old_service['telefone'], old_service['data'], old_service['placa'], old_service['marca'], old_service['modelo'], old_service['cor'], old_service['ano'], old_service['kmatual'], old_service['observacoes'], old_service['maodeobra'], old_service['pecas'])
        self.grid()
        self.data = data
        self.produtos = self.servico.pecas
        self.valTot = 0
        self.aut = 0
        self.clic = ''
        self.posi_desc = 0
        self.posi_valUnit = 1
        self.posi_qtd = 2
        self.posi_valTot = 3
        self.travel_selecao = ''
        self.values = ''
        self.travel_tabel = ''
        self.point_click = ''
        self.enter_foc = ''
        self.d_f =[]
        self.travel_ValQtd = []
        self.label_TotServ = ''
        self.maodeobra = ''
        if old_service == '':
            self.create()

    def create(self):
        HomePage(self)

    def new_server(self):
        def_address('')
        self.create_page()

    def open_server(self):
        def_address(self.enter_data.get())
        self.create_page()
    
    def create_page(self):
        ServicePage(self)

    def clean_ent(self):
        clean_ent(self)

    def tabel(self):  
        if self.travel_tabel:
            self.my_tree.destroy()

        style = ttk.Style()
        style.theme_use("alt")
        # Pick a theme
        style.configure("Treeview", background="#DCDCDC", fieldbackground="#DCDCDC")
        style.configure('Treeview.Heading', background='#b1b3b2', foreground="black", font=('Calibri', 20))

        # Change selected color
        style.map('Treeview', background=[('selected', 'blue')])

        # Create Treeview Frame
        tree_frame = Frame(self.master)
        tree_frame.grid(row=2, rowspan=9, column=5, columnspan=5, sticky='wn', pady=5)

        # Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create Treeview
        self.my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height=21)
        # Pack to the screen
        self.my_tree.pack()

        # Configure the scrollbar
        tree_scroll.config(command=self.my_tree.yview)

        # Define Our Columns
        self.my_tree['columns'] = ("N°", "Desc", "ValUnit", "Qtd", "ValTot")

        # Formate Our Columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("N°", anchor=CENTER, width=40)
        self.my_tree.column("Desc", anchor=W, width=400)
        self.my_tree.column("ValUnit", anchor=W, width=150)
        self.my_tree.column("Qtd", anchor=CENTER, width=75)
        self.my_tree.column("ValTot", anchor=W, width=150)

        # Create Headings
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("N°", text="N°", anchor=CENTER)
        self.my_tree.heading("Desc", text="Descrição", anchor=W)
        self.my_tree.heading("ValUnit", text="Val.Unit", anchor=CENTER)
        self.my_tree.heading("Qtd", text="Qtd", anchor=CENTER)
        self.my_tree.heading("ValTot", text="Val.Total", anchor=CENTER)

        for record in range(len(self.produtos)):
            self.my_tree.insert(
                parent='', index='end', text="", values=(record+1, (self.produtos[record])[0], f'R${(self.produtos[record])[1]:.2f}', (self.produtos[record])[2], f'R${(self.produtos[record])[3]:.2f}'))

        self.travel_tabel = 1
        
    def chamado_add(self, e):
        self.entrada_op = str(self.master.focus_get())
        print(self.entrada_op)
        if self.entrada_op == '.':
            self.enter_foc = self.enter_desc

        elif self.entrada_op == '.!entry9':
            self.enter_foc = self.enter_valUnit

        elif self.entrada_op == str(self.enter_valUnit):
            self.enter_foc = self.enter_Qtd

        elif self.entrada_op == str(self.enter_Qtd):
            self.enter_foc = self.enter_desc
            self.add_bbtc()

        self.enter_foc.focus_set()

    def voltar_entrada(self,e):
        self.entrada_op = str(self.master.focus_get())
        if '.!entry' in self.entrada_op:

            if self.entrada_op == '.!entry2':
                self.enter_foc = self.enter_desc

            elif self.entrada_op == '.!entry3':
                self.enter_foc = self.enter_valUnit

            if self.enter_foc:
                self.enter_foc.focus_set()

    def avancar_entrada(self,e):
        self.entrada_op = str(self.master.focus_get())
        if '.!entry' in self.entrada_op:

            if self.entrada_op == '.!entry':
                self.enter_foc = self.enter_valUnit

            elif self.entrada_op == '.!entry2':
                self.enter_foc = self.enter_Qtd

            if self.enter_foc:
                self.enter_foc.focus_set()

    def add_bbtc(self):
        #Inserindo Valores
        self.desc = (str(self.enter_desc.get())).upper()
        self.val_unit = str(self.enter_valUnit.get())
        if self.val_unit:
            if ',' in self.val_unit:
                self.val_unit = (self.val_unit).replace(',','.')

            if not self.val_unit[0].isalpha():
                self.val_unit = float(self.val_unit)


                self.qtd = self.enter_Qtd.get()
                if self.qtd:
                    self.qtd = int(self.enter_Qtd.get())
                    self.val_tot = self.val_unit * self.qtd

                    #Colocando os Valores dentro da Biblioteca
                    if self.qtd > 0 and self.desc and self.val_unit >= 0:
                        self.produtos.append([self.desc, self.val_unit, self.qtd, self.val_tot])

        #Quardando Valor Total
        self.valTot = 0
        for c in self.produtos:
            self.valTot += c[self.posi_valTot]

        #Inserido Vals Tot Qtd
        if self.travel_ValQtd:
            self.label_ValTot.destroy()
            self.label_TotServ.destroy()

        #Valor Mão de Obra
        self.maodeobra = self.enter_maodeobra.get()
        if ',' in self.maodeobra:
            self.maodeobra = (self.maodeobra).replace(',','.')
        if self.maodeobra == '':
            self.maodeobra = 0
        self.maodeobra = float(self.maodeobra)

        #Inserindo Ordem de Serviço
        self.label_ValTot = tk.Label(self.master, text=f' Ordem de Serviço: {self.servico.ordem}  Data:', font=('Calibri', 20), fg='white', anchor='w', bg="#2d2d2d")
        self.label_ValTot.grid(row=1, rowspan=1, column=0,columnspan=3, pady=10, sticky='w')

        #Inserindo Total Peças
        valtot = ' Total Peças:R${:.2f}'.format(self.valTot)
        self.label_ValTot = tk.Label(self.master, text=valtot[:29], font=('Calibri', 26), bg='#c51c1d', anchor='w')
        self.label_ValTot.grid(row=11, rowspan=1, column=0, columnspan=4, pady=0, sticky='w')

        #Inserindo Total Serviço
        valtots = f' Valor Total:R${(self.valTot + self.maodeobra):.2f}'
        self.label_TotServ = tk.Label(self.master, text=valtots[:31], font=('Calibri', 26), bg='#c51c1d', anchor='w')
        self.label_TotServ.grid(row=12, rowspan=1, column=0, columnspan=4, pady=0, sticky='w')

        self.travel_ValQtd = 1

        # Limpando Entradas
        self.clean_ent()

        #Colocando Tabela
        self.tabel()

    def chamado_nota(self,e):
        self.salvar_pdf()

    def salvar_pdf(self):
        if self.valTot >= 0:
            
            nome_nota = (filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], initialfile=self.save_data())).upper()
            if nome_nota:
                CreateServiceNote(nome_nota, self.servico, self.valTot)

    def chamado_save_data(self):
        self.save_data()

    def save_data(self):
        servico_old = self.old_service
        val = askokcancel("Salvar-Serviço", "Salvar serviço?")
        if val:
            val_orderserver = self.val_orderserver
            self.servico = Service(self.servico.ordem, self.enter_ncliente.get(), self.enter_telefone.get(), self.enter_date.get(), self.enter_placa.get(), self.enter_marca.get(), self.enter_modelo.get(), self.enter_cor.get(), self.enter_ano.get(), self.enter_kmatual.get(), self.my_text.get("1.0", "end-1c"), self.maodeobra, self.produtos)

            nomes_arquivos = os.listdir()
            for nome_arquivo in nomes_arquivos:
                if self.servico.ordem in nome_arquivo and ".json" in nome_arquivo:
                    os.remove(nome_arquivo)

            if not servico_old:
                # Abrir o arquivo JSON e carregar os dados
                with open("orderserver.json", "r") as arquivo_json:
                    val_orderserver = json.load(arquivo_json)
                self.servico.ordem = f"{(val_orderserver['ordem de servico'][-1] + 1):06d}"

            # Converter a instância em um dicionário
            dados = {
                "ordem": self.servico.ordem,
                "ncliente": self.servico.ncliente,
                "telefone": self.servico.telefone,
                "data": self.servico.data,
                "placa": self.servico.placa,
                "marca": self.servico.marca,
                "modelo": self.servico.modelo,
                "cor": self.servico.cor,
                "ano": self.servico.ano,
                "kmatual": self.servico.kmatual,
                "observacoes": self.servico.observacoes,
                "maodeobra": self.servico.maodeobra,
                "pecas": self.servico.pecas
            }

            nm = f"{self.servico.ordem}_{self.servico.placa}_{self.servico.ncliente}".upper()
            nome_json = f"{nm}.json"
            with open(nome_json, "w") as arquivo_json:
                json.dump(dados, arquivo_json, indent=4)

            # Listar todos os arquivos na pasta
            nomes_arquivos = os.listdir()
            for nome_arquivo in nomes_arquivos:
                if self.servico.ordem in nome_arquivo and ".json" in nome_arquivo:
                    if not int(self.servico.ordem) in val_orderserver["ordem de servico"]:
                        val_orderserver["ordem de servico"].append(int(self.servico.ordem))
                    print(val_orderserver)
                    novo_json = json.dumps(val_orderserver)
                    with open("orderserver.json", "w") as arquivo_json:
                        arquivo_json.write(novo_json)

            self.val_orderserver = val_orderserver
            self.old_service = nome_json
            self.add_bbtc()

            return nome_json[:-5]

    def chamado_jaend(self,e):
        self.janela_end()

    def janela_end(self):
        self.root_notaFiscal.destroy()
        self.clic = ''

    def chamado_restart(self,e):
        self.restart()

    def restart(self):
        val = askokcancel("Deletar-Peças", "Deletar todas as peças do serviço?")
        if val:
            self.produtos = []
            self.add_bbtc()

            # Espaço
            for record in self.my_tree.get_children():
                self.my_tree.delete(record)

    def chamado_deletar(self,e):
        if '.!treeview' in str(self.master.focus_get()):
            self.deletar_prod()

    def deletar_prod(self):
        if self.values:
            self.clean_ent()
            self.prod = self.my_tree.selection()[0]
            self.my_tree.delete(self.prod)

            posi_values = self.produtos.index(self.values)
            self.produtos.pop(posi_values)

            self.add_bbtc()

    def select_record(self,e):
        # Clear entry boxes
        self.clean_ent()

        # Grab record number
        selected = self.my_tree.focus()
        # Grab record values
        self.values = self.my_tree.item(selected, 'values')
        if self.values:
            self.values = [self.values[1], self.values[2], self.values[3], self.values[4]]
            self.values[1] = float(str(self.values[1]).replace('R$',''))
            self.values[2] = int(self.values[2])
            self.values[3] = float(str(self.values[3]).replace('R$',''))

            # output to entry boxes
            self.enter_desc.insert(0, self.values[0])
            self.enter_valUnit.insert(0, self.values[1])
            self.enter_Qtd.insert(0, self.values[2])

            self.travel_selecao = 1

    def selecao(self,e):

        self.select_record('')
        if not self.values:
            # Já deixar um item selecionado
            list = self.my_tree.get_children()
            if list:
                self.my_tree.selection_set(list[0])
                self.my_tree.focus(list[0])
                self.my_tree.focus_force()

        self.select_record('')

    def travel_d(self,e):
        self.select_record('')

    def not_selec(self,e):
        self.my_tree.bind("<ButtonRelease-1>", self.travel_d)

        if self.travel_selecao and self.point_click == '':
            self.my_tree.selection_set()
            self.my_tree.focus()
            self.my_tree.focus_force()
            self.travel_selecao = ''
            self.point_click = ''
            self.clean_ent()

        self.point_click = ''

    def render_shortcuts(self,e):
        RenderShortcuts(self)
        
    def insert_entrys(self):
        self.enter_ncliente.insert(0, self.servico.ncliente)
        self.enter_telefone.insert(0, self.servico.telefone)
        self.enter_placa.insert(0, self.servico.placa)
        self.enter_marca.insert(0, self.servico.marca)
        self.enter_modelo.insert(0, self.servico.modelo)
        self.enter_cor.insert(0, self.servico.cor)
        self.enter_ano.set(self.servico.ano)
        self.enter_kmatual.insert(0, self.servico.kmatual)
        self.my_text.insert('1.0', self.servico.observacoes)
        if self.servico.maodeobra:
            self.entry_var.set(self.servico.maodeobra)
    
    # Função de validação para a entrada de números
    def testVal(self, inStr, acttyp):
                if acttyp == '1':
                    if not inStr.isdigit():
                        return False
                return True
    
    def create_widgets(self):
        Widget(self)
