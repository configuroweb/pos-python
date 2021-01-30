from tkinter import *
import random
import os
import sys
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#fd7e1b")
        self.root.title("Sistema POS ConfiguroWeb")
        title = Label(self.root, text="Sistema POS ConfiguroWeb", bd=12, relief=RIDGE, font=(
            "Arial Black", 20), bg="#3891c8", fg="white").pack(fill=X)
        # ===================================variables=======================================================================================
        self.cocosete = IntVar()
        self.supercoco = IntVar()
        self.nucita = IntVar()
        self.oreo = IntVar()
        self.chocomilk = IntVar()
        self.chekechoko = IntVar()
        self.chocojet = IntVar()
        self.arroz = IntVar()
        self.pasta = IntVar()
        self.frijol = IntVar()
        self.aceite = IntVar()
        self.azucar = IntVar()
        self.papa = IntVar()
        self.harina = IntVar()
        self.jabon = IntVar()
        self.shampoo = IntVar()
        self.locion = IntVar()
        self.crema = IntVar()
        self.espuma = IntVar()
        self.mascara = IntVar()
        self.jabonmanos = IntVar()
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.phone = StringVar()
        # ==========================================customer details label frame=================================================
        details = LabelFrame(self.root, text="Detalles del Cliente", font=(
            "Arial Black", 12), bg="#3891c8", fg="white", relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        cust_name = Label(details, text="Nombre del Cliente", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=0, padx=15)

        cust_entry = Entry(details, borderwidth=4, width=30,
                           textvariable=self.c_name).grid(row=0, column=1, padx=8)

        contact_name = Label(details, text="No Contacto", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=2, padx=10)

        contact_entry = Entry(details, borderwidth=4, width=30,
                              textvariable=self.phone).grid(row=0, column=3, padx=8)

        bill_name = Label(details, text="No de Factura", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=4, padx=10)

        bill_entry = Entry(details, borderwidth=4, width=30,
                           textvariable=self.bill_no).grid(row=0, column=5, padx=8)
        # =======================================snacks label frame=================================================================
        snacks = LabelFrame(self.root, text="Dulces 5%", font=(
            "Arial Black", 12), bg="#3891c8", fg="#ffffff", relief=GROOVE, bd=10)
        snacks.place(x=5, y=180, height=380, width=325)

        item1 = Label(snacks, text="Cocosete", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=0, column=0, pady=11)
        item1_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.cocosete).grid(row=0, column=1, padx=10)

        item2 = Label(snacks, text="Supercoco", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item2_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.supercoco).grid(row=1, column=1, padx=10)

        item3 = Label(snacks, text="Nucita", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=2, column=0, pady=11)
        item3_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.nucita).grid(row=2, column=1, padx=10)

        item4 = Label(snacks, text="Oreo", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)
        item4_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.oreo).grid(row=3, column=1, padx=10)

        item5 = Label(snacks, text="ChocoMilk", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=4, column=0, pady=11)
        item5_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.chocomilk).grid(row=4, column=1, padx=10)

        item6 = Label(snacks, text="ChekeChoko", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
        item6_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.chekechoko).grid(row=5, column=1, padx=10)

        item7 = Label(snacks, text="ChocoJet", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item7_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.chocojet).grid(row=6, column=1, padx=10)
        # ===================================GROCERY=====================================================================================
        grocery = LabelFrame(self.root, text="Comestibles 10%", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="#ffffff")
        grocery.place(x=340, y=180, height=380, width=325)

        item8 = Label(grocery, text="Arroz", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=0, column=0, pady=11)
        item8_entry = Entry(grocery, borderwidth=2, width=15,
                            textvariable=self.arroz).grid(row=0, column=1, padx=10)

        item9 = Label(grocery, text="Pasta", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item9_entry = Entry(grocery, borderwidth=2, width=15,
                            textvariable=self.pasta).grid(row=1, column=1, padx=10)

        item10 = Label(grocery, text="Frijol", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=2, column=0, pady=11)
        item10_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.frijol).grid(row=2, column=1, padx=10)

        item11 = Label(grocery, text="Aceite", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)
        item11_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.aceite).grid(row=3, column=1, padx=10)

        item12 = Label(grocery, text="Azucar", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=4, column=0, pady=11)
        item12_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.azucar).grid(row=4, column=1, padx=10)

        item13 = Label(grocery, text="Papa", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
        item13_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.papa).grid(row=5, column=1, padx=10)

        item14 = Label(grocery, text="Harina", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item14_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.harina).grid(row=6, column=1, padx=10)
        # ========================================beauty and hygine===============================================================================
        hygine = LabelFrame(self.root, text="Belleza e Higiene 7%", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="#ffffff")
        hygine.place(x=677, y=180, height=380, width=325)

        item15 = Label(hygine, text="Jabón", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=0, column=0, pady=11)
        item15_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.jabon).grid(row=0, column=1, padx=10)

        item16 = Label(hygine, text="Shampoo", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item16_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.shampoo).grid(row=1, column=1, padx=10)

        item17 = Label(hygine, text="Loción-Corporal", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=2, column=0, pady=11)
        item17_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.locion).grid(row=2, column=1, padx=10)

        item18 = Label(hygine, text="Crema-Cuerpo", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)
        item18_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.crema).grid(row=3, column=1, padx=10)

        item19 = Label(hygine, text="Espuma-Afeitar", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=4, column=0, pady=11)
        item19_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.espuma).grid(row=4, column=1, padx=10)

        item20 = Label(hygine, text="Máscara-Facial", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
        item20_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.mascara).grid(row=5, column=1, padx=10)

        item21 = Label(hygine, text="Jabón-Manos", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item21_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.jabonmanos).grid(row=6, column=1, padx=10)
        # =====================================================billarea==============================================================================
        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#3891c8")
        billarea.place(x=1010, y=188, width=330, height=372)

        bill_title = Label(billarea, text="Área de Facturación", font=(
            "Arial Black", 17), bd=7, relief=GROOVE, bg="#3891c8", fg="#ffffff").pack(fill=X)

        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        # =================================================billing menu=========================================================================================
        billing_menu = LabelFrame(self.root, text="Resumen de facturación", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        total_snacks = Label(billing_menu, text="Precio Total Dulces", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=0, column=0)
        total_snacks_entry = Entry(billing_menu, width=30, borderwidth=2,
                                   textvariable=self.total_sna).grid(row=0, column=1, padx=10, pady=7)

        total_grocery = Label(billing_menu, text="Precio Total Comestibles", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=1, column=0)
        total_grocery_entry = Entry(billing_menu, width=30, borderwidth=2,
                                    textvariable=self.total_gro).grid(row=1, column=1, padx=10, pady=7)

        total_hygine = Label(billing_menu, text="Precio Total Belleza e Higiene", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=2, column=0)
        total_hygine_entry = Entry(billing_menu, width=30, borderwidth=2,
                                   textvariable=self.total_hyg).grid(row=2, column=1, padx=10, pady=7)

        tax_snacks = Label(billing_menu, text="Impuesto Dulces", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=0, column=2)
        tax_snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.a).grid(
            row=0, column=3, padx=10, pady=7)

        tax_grocery = Label(billing_menu, text="Impuesto Comestibles", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=1, column=2)
        tax_grocery_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.b).grid(
            row=1, column=3, padx=10, pady=7)

        tax_hygine = Label(billing_menu, text="Impuesto Belleza e Higiene", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=2, column=2)
        tax_hygine_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.c).grid(
            row=2, column=3, padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#fd7e1b")
        button_frame.place(x=830, width=500, height=95)

        button_total = Button(button_frame, text="Total Facturado", font=("Arial Black", 15), pady=10,
                              bg="#3891c8", fg="#ffffff", command=lambda: total(self)).grid(row=0, column=0, padx=12)
        button_clear = Button(button_frame, text="Resetear", font=("Arial Black", 15), pady=10,
                              bg="#3891c8", fg="#ffffff", command=lambda: clear(self)).grid(row=0, column=1, padx=10, pady=6)
        button_exit = Button(button_frame, text="Salir", font=("Arial Black", 15), pady=10, bg="#3891c8",
                             fg="#ffffff", width=8, command=lambda: exit1(self)).grid(row=0, column=2, padx=10, pady=6)
        intro(self)


def total(self):
    if (self.c_name.get == "" or self.phone.get() == ""):
        messagebox.showerror("Error", "Complete los datos del cliente!!")
    self.nu = self.cocosete.get()*12000
    self.no = self.supercoco.get()*4000
    self.la = self.nucita.get()*1000
    self.ore = self.oreo.get()*2000
    self.mu = self.chocomilk.get()*3500
    self.si = self.chekechoko.get()*6050
    self.na = self.chocojet.get()*1500
    total_snacks_price = (
        self.nu +
        self.no +
        self.la +
        self.ore +
        self.mu +
        self.si +
        self.na)
    self.total_sna.set(str(total_snacks_price)+" COP")
    self.a.set(str(round(total_snacks_price*0.05, 3))+" COP")

    self.at = self.arroz.get()*4200
    self.pa = self.pasta.get()*12050
    self.oi = self.aceite.get()*11300
    self.ri = self.frijol.get()*160050
    self.su = self.azucar.get()*5550
    self.te = self.harina.get()*4800
    self.da = self.papa.get()*7665
    total_grocery_price = (
        self.at +
        self.pa +
        self.oi +
        self.ri +
        self.su +
        self.te +
        self.da)

    self.total_gro.set(str(total_grocery_price)+" COP")
    self.b.set(str(round(total_grocery_price*0.01, 3))+" COP")

    self.so = self.jabon.get()*3000
    self.sh = self.shampoo.get()*18000
    self.cr = self.crema.get()*130000
    self.lo = self.locion.get()*50000
    self.fo = self.espuma.get()*8500
    self.ma = self.mascara.get()*10000
    self.sa = self.jabonmanos.get()*2005

    total_hygine_price = (
        self.so +
        self.sh +
        self.cr +
        self.lo +
        self.fo +
        self.ma +
        self.sa)

    self.total_hyg.set(str(total_hygine_price)+" COP")
    self.c.set(str(round(total_hygine_price*0.07, 3))+" COP")
    self.total_all_bill = (total_snacks_price +
                           total_grocery_price +
                           total_hygine_price +
                           (round(total_grocery_price*0.01, 3)) +
                           (round(total_hygine_price*0.07, 3)) +
                           (round(total_snacks_price*0.05, 3)))
    self.total_all_bil = str(self.total_all_bill)+" COP"
    billarea(self)


def intro(self):
    self.txtarea.delete(1.0, END)
    self.txtarea.insert(
        END, "\tBienvenid@ a tu Tienda\n\tTeléfono +57 316 243 00 81")
    self.txtarea.insert(END, f"\n\nFactura Número. : {self.bill_no.get()}")
    self.txtarea.insert(END, f"\nNombre Cliente : {self.c_name.get()}")
    self.txtarea.insert(END, f"\nTeléfono No. : {self.phone.get()}")
    self.txtarea.insert(END, "\n====================================\n")
    self.txtarea.insert(END, "\nProducto\t\tCant\tPrecio\n")
    self.txtarea.insert(END, "\n====================================\n")


def billarea(self):
    intro(self)
    if self.cocosete.get() != 0:
        self.txtarea.insert(
            END, f"CocoSete\t\t {self.cocosete.get()}\t{self.nu}\n")
    if self.supercoco.get() != 0:
        self.txtarea.insert(
            END, f"SuperCoco\t\t {self.supercoco.get()}\t{self.no}\n")
    if self.nucita.get() != 0:
        self.txtarea.insert(
            END, f"Nucita\t\t {self.nucita.get()}\t{self.la}\n")
    if self.oreo.get() != 0:
        self.txtarea.insert(END, f"Oreo\t\t {self.oreo.get()}\t{self.ore}\n")
    if self.chocomilk.get() != 0:
        self.txtarea.insert(
            END, f"Chocomilks\t\t {self.chocomilk.get()}\t{self.mu}\n")
    if self.chekechoko.get() != 0:
        self.txtarea.insert(
            END, f"Chekechoko\t\t {self.chekechoko.get()}\t{self.si}\n")
    if self.chocojet.get() != 0:
        self.txtarea.insert(
            END, f"Chocojet\t\t {self.chocojet.get()}\t{self.na}\n")
    if self.arroz.get() != 0:
        self.txtarea.insert(END, f"Arroz\t\t {self.arroz.get()}\t{self.at}\n")
    if self.pasta.get() != 0:
        self.txtarea.insert(END, f"Pasta\t\t {self.pasta.get()}\t{self.pa}\n")
    if self.frijol.get() != 0:
        self.txtarea.insert(
            END, f"Frijol\t\t {self.frijol.get()}\t{self.ri}\n")
    if self.aceite.get() != 0:
        self.txtarea.insert(
            END, f"Aceite\t\t {self.aceite.get()}\t{self.oi}\n")
    if self.azucar.get() != 0:
        self.txtarea.insert(
            END, f"Azucar\t\t {self.azucar.get()}\t{self.su}\n")
    if self.papa.get() != 0:
        self.txtarea.insert(
            END, f"Papa\t\t {self.papa.get()}\t{self.da}\n")
    if self.harina.get() != 0:
        self.txtarea.insert(
            END, f"Harina\t\t {self.harina.get()}\t{self.te}\n")
    if self.jabon.get() != 0:
        self.txtarea.insert(END, f"Jabón\t\t {self.jabon.get()}\t{self.so}\n")
    if self.shampoo.get() != 0:
        self.txtarea.insert(
            END, f"Shampoo\t\t {self.shampoo.get()}\t{self.sh}\n")
    if self.locion.get() != 0:
        self.txtarea.insert(
            END, f"Loción-Cuerpo\t\t {self.locion.get()}\t{self.lo}\n")
    if self.crema.get() != 0:
        self.txtarea.insert(
            END, f"Crema-Cuerpo\t\t {self.crema.get()}\t{self.cr}\n")
    if self.espuma.get() != 0:
        self.txtarea.insert(
            END, f"Espuma-Afeitar\t\t {self.espuma.get()}\t{self.fo}\n")
    if self.mascara.get() != 0:
        self.txtarea.insert(
            END, f"Máscara-Facial\t\t {self.mascara.get()}\t{self.ma}\n")
    if self.jabonmanos.get() != 0:
        self.txtarea.insert(
            END, f"Jabón-Manos\t\t {self.jabonmanos.get()}\t{self.sa}\n")

    self.txtarea.insert(END, f"------------------------------------\n")
    if self.a.get() != "0.0 COP":
        self.txtarea.insert(END, f"Total Imp Dulces: {self.a.get()}\n")
    if self.b.get() != "0.0 COP":
        self.txtarea.insert(
            END, f"Total Imp Comestibles: {self.b.get()}\n")
    if self.c.get() != "0.0 COP":
        self.txtarea.insert(
            END, f"Total Imp Belleza e Higiene: {self.c.get()}\n")
    self.txtarea.insert(END, f"Monto total facturado : {self.total_all_bil}\n")
    self.txtarea.insert(END, f"------------------------------------\n")


def clear(self):
    self.txtarea.delete(1.0, END)
    self.cocosete.set(0)
    self.supercoco.set(0)
    self.nucita.set(0)
    self.oreo.set(0)
    self.chocomilk.set(0)
    self.chekechoko.set(0)
    self.chocojet.set(0)
    self.arroz.set(0)
    self.pasta.set(0)
    self.frijol.set(0)
    self.aceite.set(0)
    self.azucar.set(0)
    self.papa.set(0)
    self.harina.set(0)
    self.jabon.set(0)
    self.shampoo.set(0)
    self.locion.set(0)
    self.crema.set(0)
    self.espuma.set(0)
    self.mascara.set(0)
    self.jabonmanos.set(0)
    self.total_sna.set(0)
    self.total_gro.set(0)
    self.total_hyg.set(0)
    self.a.set(0)
    self.b.set(0)
    self.c.set(0)
    self.c_name.set(0)
    self.bill_no.set(0)
    self.bill_no.set(0)
    self.phone.set(0)


def exit1(self):
    self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
