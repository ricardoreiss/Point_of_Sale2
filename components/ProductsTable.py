from tkinter import *
from tkinter import ttk

def ProductsTable(self, my_tree, travel_tabel):
    if travel_tabel:
        my_tree.destroy()

    style = ttk.Style()
    style.theme_use("alt")
    # Pick a theme
    style.configure("Treeview", background="#DCDCDC", fieldbackground="#DCDCDC")
    style.configure('Treeview.Heading', background='#b1b3b2', foreground="black", font=('Calibri', 20))

    # Change selected color
    style.map('Treeview', background=[('selected', 'blue')])

    # Define Our Columns
    my_tree['columns'] = ("N°", "Desc", "ValUnit", "Qtd", "ValTot")

    # Formate Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("N°", anchor=CENTER, width=40)
    my_tree.column("Desc", anchor=W, width=400)
    my_tree.column("ValUnit", anchor=W, width=150)
    my_tree.column("Qtd", anchor=CENTER, width=75)
    my_tree.column("ValTot", anchor=W, width=150)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("N°", text="N°", anchor=CENTER)
    my_tree.heading("Desc", text="Descrição", anchor=W)
    my_tree.heading("ValUnit", text="Val.Unit", anchor=CENTER)
    my_tree.heading("Qtd", text="Qtd", anchor=CENTER)
    my_tree.heading("ValTot", text="Val.Total", anchor=CENTER)

    for record in range(len(self.produtos)):
        my_tree.insert(
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