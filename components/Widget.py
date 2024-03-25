import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import json
import os

def Widget(self):
    self.master.configure(bg="#2d2d2d")

    def addm(*args):
        mdo = self.entry_var.get()
        if not mdo:
            mdo = 0
        self.maodeobra = mdo
        self.add_bbtc()

    def validar_numeros(char):
        # Permite apenas caracteres numéricos
        r = char.isdigit() or char == "" or char in ".,"
        return r
    self.validacao_numeros = self.register(validar_numeros)

    #Título
    self.label_titulo = tk.Label(self.master, text='REISCAR - MECÂNICA AUTOMOTIVA', font=('Calibri', 40), bg='#c51c1d', anchor='w')
    self.label_titulo.grid(row=0, column=0, columnspan=10, sticky='nswe')

    #Data de Hoje
    self.label_datahoje = tk.Label(self.master, text=f'Data: {self.data} ', font=('Calibri', 20),bg='#c51c1d'	, anchor='e', width=16)
    self.label_datahoje.grid(row=0, column=7, columnspan=10, sticky='nswe')

    #Lista Atalhos
    self.label_listaatalhos = tk.Label(self.master, text='Acessar Atalhos:Ctrl+Tab', bg='#c51c1d', anchor='s')
    self.label_listaatalhos.grid(row=0, column=8, columnspan=10, sticky='s')
    self.master.bind('<Control-Tab>', self.render_shortcuts)

    #Entry Data
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    self.enter_date = DateEntry(self.master, font=('Calibri', 20), width=9, bg='#DCDCDC', locale='pt_BR', state="readonly")
    self.enter_date.grid(row=1, column=2, columnspan=2, pady=0, sticky='e')
    self.enter_date.set_date(self.servico.data)

    #Texto Cliente
    self.label_ncliente = tk.Label(self.master, text=' Cliente:', font=('Calibri', 20), anchor='w', width=9)
    self.label_ncliente.grid(row=2, column=0, columnspan=4, sticky='w')

    #Entry Cliente
    self.enter_ncliente = tk.Entry(self.master, font=('Calibri', 20), width=30, bg='#DCDCDC')
    self.enter_ncliente.grid(row=2, column=0, columnspan=4, pady=0, sticky='e')

    #Texto Telefone
    self.label_telefone = tk.Label(self.master, text=' Telefone:', font=('Calibri', 20), anchor='w', width=8)
    self.label_telefone.grid(row=3, column=0, columnspan=4, sticky='w')

    #Entry Telefone
    self.enter_telefone = tk.Entry(self.master, font=('Calibri', 20), width=16, bg='#DCDCDC', validate="key")
    self.enter_telefone['validatecommand'] = (self.enter_telefone.register(self.testVal),'%P','%d')
    self.enter_telefone.grid(row=3, column=0, columnspan=4, pady=0, sticky='w', padx=112)

    #Texto Placa
    self.label_placa = tk.Label(self.master, text=' PLACA DO VEÍCULO:', font=('Calibri', 20), anchor='w')
    self.label_placa.grid(row=4, column=0, columnspan=2, sticky='w')

    
    def placaexists(*args):
        placa = self.enter_placa.get()
        nomes_arquivos = os.listdir()
        print(placa)
        for nome_arquivo in nomes_arquivos:
            if '.json' in nome_arquivo and nome_arquivo != 'orderserver.json':
                with open(nome_arquivo, "r") as arquivo_json:
                    datas_for_placa = json.load(arquivo_json)

                    if placa == "" or (placa == datas_for_placa['placa'] != ""): 
                        self.enter_ncliente.delete(0, 'end')
                        self.enter_telefone.delete(0, 'end')
                        self.enter_marca.delete(0, 'end')
                        self.enter_modelo.delete(0, 'end')
                        self.enter_cor.delete(0, 'end')
                        self.enter_ano.set('') 

                        if placa == datas_for_placa['placa'] != "":
                            self.enter_ncliente.insert(0, datas_for_placa['ncliente'])
                            self.enter_telefone.insert(0, datas_for_placa['telefone'])
                            self.enter_marca.insert(0, datas_for_placa['marca'])
                            self.enter_modelo.insert(0, datas_for_placa['modelo'])
                            self.enter_cor.insert(0, datas_for_placa['cor'])
                            self.enter_ano.set(datas_for_placa['ano'])       
                    

    #Entry Placa           
    self.enter_placa = tk.Entry(self.master, font=('Calibri', 20), width=20, bg='#DCDCDC', validatecommand=(self.validacao_numeros, "%S"))
    self.enter_placa.grid(row=4, column=1, columnspan=3, pady=0, sticky='e')

    #Texto Placa
    self.label_branco = tk.Label(self.master, text='         ', font=('Calibri', 20), anchor='e')
    self.label_branco.grid(row=4, column=0, columnspan=4, sticky='e')

    #Botão Search For Placa
    self.botao_searchplaca = tk.Button(self.master, text='🔍', font=('Calibri', 17), bg='#6a88b5', command=placaexists)
    self.botao_searchplaca.grid(row=4, rowspan=1, column=3, padx=10, sticky='e')

    #Texto Marca
    self.label_marca = tk.Label(self.master, text=' MARCA:', font=('Calibri', 20), anchor='w')
    self.label_marca.grid(row=5, column=0, columnspan=1, sticky='w')

    #Entry Marca
    self.enter_marca = tk.Entry(self.master, font=('Calibri', 20), width=8, bg='#DCDCDC')
    self.enter_marca.grid(row=6, column=0, columnspan=1, pady=0, sticky='w', padx=10)

    #Texto Modelo
    self.label_modelo = tk.Label(self.master, text='MODELO:', font=('Calibri', 20), anchor='w')
    self.label_modelo.grid(row=5, column=1, columnspan=1, sticky='w')

    #Entry Modelo
    self.enter_modelo = tk.Entry(self.master, font=('Calibri', 20), width=9, bg='#DCDCDC')
    self.enter_modelo.grid(row=6, column=1, columnspan=1, pady=0, sticky='w', padx=0)

    #Texto Cor
    self.label_cor = tk.Label(self.master, text=' COR:', font=('Calibri', 20), anchor='w')
    self.label_cor.grid(row=5, column=2, columnspan=1, sticky='w')

    #Entry Cor
    self.enter_cor = tk.Entry(self.master, font=('Calibri', 20), width=8, bg='#DCDCDC')
    self.enter_cor.grid(row=6, column=2, columnspan=1, pady=0, sticky='w', padx=10)

    #Texto Ano
    self.label_ano = tk.Label(self.master, text='ANO:', font=('Calibri', 20), anchor='w')
    self.label_ano.grid(row=5, column=3, columnspan=1, sticky='w')

    #Entry Ano
    anos = [str(ano) for ano in range(int(self.data[6:])+1, 1979, -1)]
    self.enter_ano = ttk.Combobox(self.master, font=('Calibri', 20), width=7, values=anos, state="readonly")
    self.enter_ano.grid(row=6, column=3, columnspan=1, pady=0, sticky='w', padx=0)
    ttk.Style().configure("TCombobox", fieldbackground="#DCDCDC")

    #Texto Km Atual
    self.label_kmatual = tk.Label(self.master, text=' KM ATUAL:', font=('Calibri', 20), anchor='w')
    self.label_kmatual.grid(row=7, column=0, columnspan=4, sticky='w')

    #Entry Km Atual
    self.enter_kmatual = tk.Entry(self.master, font=('Calibri', 20), width=15, bg='#DCDCDC')
    self.enter_kmatual.grid(row=7, column=1, columnspan=3, pady=0, sticky='w', padx=0)

    #Texto Observacoes
    self.label_observacoes = tk.Label(self.master, text=' Observações Gerais:', font=('Calibri', 20), anchor='w')
    self.label_observacoes.grid(row=8, column=0, columnspan=4, sticky='w')

    #Entry Observacoes
    text_frame = Frame(self.master)
    text_frame.grid(row=9, column=0, columnspan=4, pady=0, sticky='e', padx=0)
    text_scroll = Scrollbar(text_frame)
    text_scroll.pack(side=RIGHT, fill=Y)
    self.my_text = tk.Text(text_frame, yscrollcommand=text_scroll.set, width=54, bg='#DCDCDC', font=(10), height=8)
    self.my_text.pack()
    text_scroll.config(command=self.my_text.yview)

    #Texto Mao de Obra
    self.label_maodeobra = tk.Label(self.master, text=' Mão de Obra: R$', font=('Calibri', 20), anchor='w')
    self.label_maodeobra.grid(row=10, column=0, columnspan=4, sticky='w')

    #Entry Mao de Obra
    self.entry_var = tk.StringVar()
    self.enter_maodeobra = tk.Entry(self.master, font=('Calibri', 20), width=14, bg='#DCDCDC', validate="key", validatecommand=(self.validacao_numeros, "%S"), textvariable=self.entry_var)
    self.enter_maodeobra.grid(row=10, column=1, columnspan=2, pady=5, sticky='e', padx=0)
    

    #Frame Botões
    but_frame = Frame(self.master, bg="#2d2d2d")
    but_frame.grid(row=1, rowspan=1, pady=0, padx=0, column=5, columnspan=5)

    #Botão Limpar
    self.botao_limpar = tk.Button(but_frame, text='Deletar Peças', font=('Calibri', 17), bg='red', command=self.restart)
    self.botao_limpar.grid(row=0, rowspan=1, pady=0, padx=0, column=0)
    self.master.bind('<Delete>', self.chamado_restart)

    #Botão Deletar Item
    self.botao_delprod = tk.Button(but_frame, text='Deletar Peça', font=('Calibri', 17), bg='red', command=self.deletar_prod)
    self.botao_delprod.grid(row=0, rowspan=1, pady=0, padx=40, column=1)
    self.master.bind('<BackSpace>', self.chamado_deletar)

    #Botão Salvar Dados
    self.botao_nota = tk.Button(but_frame, text='Salvar Dados', font=('Calibri', 17), bg='#6a88b5', command=self.chamado_save_data)
    self.botao_nota.grid(row=0, rowspan=1, column=2, pady=0 , padx=0)
    self.master.bind('<Control-Return>', self.chamado_save_data)

    #Botão Nota Fiscal
    self.botao_nota = tk.Button(but_frame, text='Gerar Nota', font=('Calibri', 17), bg='#6a88b5', command=self.salvar_pdf)
    self.botao_nota.grid(row=0, rowspan=1, column=3, pady=0 , padx=40)
    self.master.bind('<Control-Return>', self.chamado_nota)

    #Espaço
    self.espaco = tk.Label(self.master, text=' ')
    self.espaco.grid(row=1, rowspan=10, column=4)

    #Espaço entry
    self.background = tk.Label(self.master, bg='#c51c1d', font=('Calibri', 20), width=37, height=3)
    self.background.grid(row=11, column=0, columnspan=4, rowspan=2, sticky='sne')


    #Espaço entry
    self.background = tk.Label(self.master, bg='#b1b3b2', font=('Calibri', 20), width=59, height=3)
    self.background.grid(row=11, column=5, columnspan=5, rowspan=2, sticky='sn')

    #Descrição
    self.descricao_itm = tk.Label(self.master, text='Descrição', font=('Calibri', 20), bg='#b1b3b2', width=36, anchor='w')
    self.descricao_itm.grid(row=11, column=5, columnspan=2)

    self.enter_desc = tk.Entry(self.master, font=('Calibri', 20), width=36)
    self.enter_desc.grid(row=12, column=5, columnspan=2, padx=5)

    #Val.Unit
    self.valUnit_itm = tk.Label(self.master, text='Val.Unit', font=('Calibri', 20), bg='#b1b3b2', width=8)
    self.valUnit_itm.grid(row=11, column=7)

    self.real = tk.Label(self.master, text='R$', font=('Calibri', 19), bg='#b1b3b2')
    self.real.grid(row=12, column=7, sticky='w')

    self.enter_valUnit = tk.Entry(self.master, font=('Calibri', 20), width=6, validate="key", validatecommand=(self.validacao_numeros, "%S"))
    self.enter_valUnit.grid(row=12, column=7, sticky='e')

    #Qtd
    self.Qtd_itm = tk.Label(self.master, text='Qtd', font=('Calibri', 20), bg='#b1b3b2', width=5)
    self.Qtd_itm.grid(row=11, column=8)

    self.enter_Qtd = tk.Entry(self.master, font=('Calibri', 20), width=4, validate="key")
    self.enter_Qtd['validatecommand'] = (self.enter_Qtd.register(self.testVal),'%P','%d')
    self.enter_Qtd.grid(row=12, column=8)

    # Botão Adicionar Produto
    self.botao_addprod = tk.Button(self.master, text='Adicionar\nPeça', font=('Calibri', 15), command=self.add_bbtc)
    self.botao_addprod.grid(row=11, rowspan=2, column=9, pady=7)
    self.master.bind('<Return>', self.chamado_add)
    self.master.bind('<Control-Left>', self.voltar_entrada)
    self.master.bind('<Control-Right>', self.avancar_entrada)

    #Setas Selecionar
    self.master.bind('<Up>', self.selecao)
    self.master.bind('<Down>', self.selecao)

    self.master.bind("<ButtonRelease-1>", self.not_selec)
    self.master.bind('<Shift_L>', self.not_selec)
    
    for widget in self.master.winfo_children():
        if isinstance(widget, tk.Label):
            if widget.cget("bg") == "SystemButtonFace":
                widget.config(bg="#2d2d2d", fg="white")

    self.entry_var.trace_add("write", addm)

    self.insert_entrys()