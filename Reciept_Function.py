from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

from tkinter import filedialog

import pickle

import sys

import os


class Reciept:

    def __init__(self, root):

        self.root = root
        self.root.title("Book Store and Management System")

        self.root.withdraw()

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 100
        y = (self.root.winfo_screenheight() -
             self.root.winfo_reqheight()) / 250
        self.root.geometry("1340x680+%d+%d" % (x, y))
        self.root.resizable(False, False)


        global l
        l=[]

        # Title Head
        self.lbl_title = Label(
            self.root, text="Book Store and Management System", bd=4, relief=RIDGE,  bg="#004040", fg="#ffffff", font=("roboto sans-serif", 23), pady=14)
        self.lbl_title.pack(side=TOP, fill=X)

        # Form Frame
        self.form_frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="#004040")
        self.form_frame.place(x=0, y=65, width=1340, height=617)



        # Space to be Center lahat ng input build
        self.fname_label = Label(self.form_frame, text='',
                                font=('bold', 24), bg="#004040", fg="white", padx=20).grid(row=2, column=2, sticky=W)

        # Username
        # Book Number
        self.book_number = StringVar()
        self.book_number_label = Label(self.form_frame, text='Book Number :',
                                  font=('bold', 15), padx=14, bg="#004040", fg="white").grid(row=3, column=0, sticky=W)
        self.book_number_entry = Entry(
            self.form_frame, textvariable=self.book_number, width=15, bd=3, font=("bold", 16))
        self.book_number_entry.grid(row=3, column=1)

        # Customer Name
        self.c_name = StringVar()
        self.c_name_label = Label(self.form_frame, text='Customer Name :',
                                  font=('bold', 15), padx=14, bg="#004040", fg="white").grid(row=4, column=0, sticky=W, pady=10)
        self.c_name_entry = Entry(
            self.form_frame, textvariable=self.c_name, width=15, bd=3, font=("bold", 16))
        self.c_name_entry.grid(row=4, column=1)

        # Phone Number
        self.phone = StringVar()
        self.phone_label = Label(self.form_frame, text='Phone Number :',
                                  font=('bold', 15), padx=14, pady=10,bg="#004040", fg="white").grid(row=5, column=0, sticky=W)
        self.phone_entry = Entry(
            self.form_frame, textvariable=self.phone, width=15, bd=3, font=("bold", 16))
        self.phone_entry.grid(row=5, column=1)

        # Book Name
        self.book_name = StringVar()
        self.book_name_label = Label(self.form_frame, text='Book Name :', font=(
            'bold', 15), padx=12, pady=10, bg="#004040", fg="white").grid(row=6, column=0, sticky=W)
        self.book_name_entry = Entry(self.form_frame, textvariable=self.book_name,
                                   width=15, bd=3, font=("bold", 16))
        self.book_name_entry.grid(row=6, column=1)

        # Author Name
        self.author_name = StringVar()
        self.author_name_label = Label(self.form_frame, text='Author Name :', font=(
            'bold', 15), padx=12, pady=10, bg="#004040", fg="white").grid(row=7, column=0, sticky=W)
        self.author_name_entry = Entry(self.form_frame, textvariable=self.author_name,
                                   width=15, bd=3, font=("bold", 16))
        self.author_name_entry.grid(row=7, column=1)

        # Date Name
        self.date = StringVar()
        self.date_label = Label(self.form_frame, text='Transact Date :', font=(
            'bold', 15), padx=12, pady=10, bg="#004040", fg="white").grid(row=8, column=0, sticky=W)
        self.date_entry = Entry(self.form_frame, textvariable=self.date,
                                   width=15, bd=3, font=("bold", 16))
        self.date_entry.grid(row=8, column=1)

        # Quantity
        self.quantity = IntVar()
        self.quantity_label = Label(self.form_frame, text='Quantity Item :', font=(
            'bold', 15), padx=10, bg="#004040", fg="white").grid(row=3, column=4, sticky=W, pady=10)
        self.quantity_entry = Entry(self.form_frame, textvariable=self.quantity,
                                   width=15, bd=3, font=("bold", 16))
        self.quantity_entry.grid(row=3, column=5)

        # Price Book
        self.price = IntVar()
        self.price_label = Label(self.form_frame, text='Price Product :', font=(
            'bold', 15),bg="#004040", fg="white").grid(row=4, column=4, sticky=W)
        self.price_entry = Entry(self.form_frame, textvariable=self.price,
                                   width=15, bd=3, font=("bold", 16))
        self.price_entry.grid(row=4, column=5)

        # Total Price Amount
        self.totalprice = IntVar()
        self.total_price_label = Label(self.form_frame, text='Total Price :', font=(
            'bold', 15),bg="#004040", fg="white").grid(row=5, column=4, padx=10, sticky=W)
        self.total_price_entry = Entry(self.form_frame, textvariable=self.totalprice,
                                   width=15, bd=3, font=("bold", 16))
        self.total_price_entry.grid(row=5, column=5)

        # Total Amount
        self.totalamount = IntVar()
        self.total_amount_label = Label(self.form_frame, text='Total Amount :', font=(
            'bold', 15),bg="#004040", fg="white").grid(row=6, column=4, padx=15, sticky=W)
        self.total_amount_entry = Entry(self.form_frame, textvariable=self.totalamount,
                                   width=15, bd=3, font=("bold", 16))
        self.total_amount_entry.grid(row=6, column=5)

        # Total Change
        self.totalchange = IntVar()
        self.total_change_label = Label(self.form_frame, text='Total Change :', font=(
            'bold', 15),bg="#004040", fg="white").grid(row=7, column=4, padx=10, sticky=W)
        self.total_change_entry = Entry(self.form_frame, textvariable=self.totalchange,
                                   width=15, bd=3, font=("bold", 16))
        self.total_change_entry.grid(row=7, column=5)


        # Bill Frame
        self.bill_frame = Frame(self.root, relief=GROOVE, bd=10)
        self.bill_frame.place(x=833, y=70, width=500, height=605)

        # Bill Area
        self.bill_title = Label(self.bill_frame, text='Bill Area', bg="#004040", fg='white',font=("roboto san-serif", 14), relief=GROOVE, bd=7).pack(fill=X)
        self.scroll_y = Scrollbar(self.bill_frame, orient=VERTICAL)
        self.textarea = Text(self.bill_frame, yscrollcommand=self.scroll_y)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.textarea.yview)
        self.textarea.pack()


        # Frame for Buttons
        self.btn_frame = Frame(
            self.form_frame, bd=2, relief=RIDGE, bg="#004040")
        self.btn_frame.place(x=5, y=365, width=815, height=240)


        # Clear Button
        self.save_btn = Button(self.btn_frame, text='Clear Field', width=25, height=2, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                font=("roboto sans-serif", 11, "bold"), command=self.clear)
        self.save_btn.grid(row=2, column=3, pady=15, padx=18)

        # Save Button
        self.save_btn = Button(self.btn_frame, text='Save Database', width=25, height=2, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                font=("roboto sans-serif", 11, "bold"), command=self.reciept_func)
        self.save_btn.grid(row=2, column=4, pady=15, padx=18)

        # Save Button
        self.print_btn = Button(self.btn_frame, text='Save Receipt', width=25, height=2, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                font=("roboto sans-serif", 11, "bold"), command=self.print_reciept)
        self.print_btn.grid(row=2, column=5, pady=15, padx=18)

        # Recipt Button
        self.reciept_btn = Button(self.btn_frame, text='Generate Reciept', width=25, height=2, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                font=("roboto sans-serif", 11, "bold"), command=self.reciept_func)
        self.reciept_btn.grid(row=3, column=3, pady=10, padx=18)

        # Add 
        self.add_btn = Button(self.btn_frame, text='Add Item', width=25, height=2, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                font=("roboto sans-serif", 11, "bold"), command=self.add)
        self.add_btn.grid(row=3, column=4, pady=5, padx=10)

        # Total
        self.total_btn = Button(self.btn_frame, text='Generate Bill', width=25, height=2, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                font=("roboto sans-serif", 11, "bold"),command=self.total)
        self.total_btn.grid(row=3, column=5, pady=5, padx=10)

        # Change Button
        self.change_btn = Button(self.btn_frame, text='Compute Change', width=25, height=2, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                font=("roboto sans-serif", 11, "bold"),command=self.change)
        self.change_btn.grid(row=4, column=3, pady=20, padx=10)

        # Compute Button
        self.change_btn = Button(self.btn_frame, text='Compute Item', width=25, height=2, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                font=("roboto sans-serif", 11, "bold"),command=self.compute)
        self.change_btn.grid(row=4, column=4, pady=20, padx=10)

        # Close Button
        self.close_btn = Button(self.btn_frame, text='Close System', width=25, height=2, bd=2, relief=FLAT, bg="#005A5A", fg="white",
                                   font=("roboto sans-serif", 11, "bold"), command=self.close_system)
        self.close_btn.grid(row=4, column=5, padx=10)


    def print_reciept(self):

        file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text file", ".txt")])
        filetext = str(self.textarea.get(1.0, END))
        file.write(filetext)
        file.close()

        

    def change(self):
        self.totalchange_entry = (self.totalamount.get() - sum(l))
        self.totalchange.set(self.totalchange_entry)

    def compute(self):
        self.totalprice_entry = (self.price.get() * self.quantity.get())
        self.totalprice.set(self.totalprice_entry)

    def welcome(self):
        self.textarea.insert(END, f"\n\t       Welcome to Book Store Management System")
        self.textarea.insert(END, f'\n\n Book Number :\t\t{self.book_number.get()}')
        self.textarea.insert(END, f'\n Customer Name :\t\t{self.c_name.get()}')
        self.textarea.insert(END, f'\n Transaction Date :\t\t{self.date.get()}')
        self.textarea.insert(END, f'\n Phone Number :\t\t{self.phone.get()}')
        self.textarea.insert(END, f"\n ==================================================")
        self.textarea.insert(END, f'\n Product\t\t\t QTY\t\tPrice')
        self.textarea.insert(END, f"\n ==================================================")
        self.textarea.configure(font=("roboto san-serif", 11))

    def reciept_func(self):
        self.welcome()

    def add(self):
        n=self.price.get()
        m=self.quantity.get()*n
        l.append(m)
        self.textarea.insert(END, f'\n\n{self.book_name.get()}\t\t\t{self.quantity.get()}\t\t{m}')

    def total(self):
        self.textarea.insert(END, f"\n\n ==================================================")
        self.textarea.insert(END, f"\nTotal Paybill Amount :\t\t\t\t\t{sum(l)}")
        self.textarea.insert(END, f"\n ==================================================")
        self.textarea.insert(END, f"\nTotal Client Amount :\t\t\t\t\t{self.totalamount.get()}")
        self.textarea.insert(END, f"\n ==================================================")
        self.textarea.insert(END, f"\nTotal Change Amount :\t\t\t\t\t{self.totalchange.get()}")
        self.textarea.insert(END, f"\n ==================================================")

    def close_system(self):
        self.root.destroy()

    def clear(self):
        
        self.book_number_entry.delete(0, END)
        self.c_name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.book_name_entry.delete(0, END)

        self.quantity.set(0)
        self.price.set(0)

        self.totalprice.set(0)
        self.totalamount.set(0)
        self.totalchange.set(0)

        self.author_name_entry.delete(0, END)
        self.date_entry.delete(0, END)

        self.textarea.delete(1.0, END)

        l.clear
        
        


root = Tk()
obj = Reciept(root)
root.deiconify()
root.mainloop()
