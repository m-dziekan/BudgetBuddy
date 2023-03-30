import tkinter
from tkinter import *
import customtkinter
from PIL import ImageTk
from modules.database import database_connect
from tkinter import messagebox
from modules.budget import Budget


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class AddExpense(customtkinter.CTk):
    def __init__(self, user_id):
        self.id = user_id
        super().__init__()
        self.geometry("800x600")
        self.title("Add new expense")
        self.frame = customtkinter.CTkFrame(master=self, width=800, height=600)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.resizable(False, False)
        self.window_flag = 1

        self.label = customtkinter.CTkLabel(master=self.frame, text="Add new expense", font=("Arial", 35, "normal"))
        self.label.grid(row=0, column=0, padx=20, pady=10)

        self.name_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Name", justify=CENTER)
        self.name_entry.grid(pady=20, padx=10, row=1, column=0, sticky="ew")

        self.desc_text = customtkinter.CTkTextbox(master=self.frame, width=200, fg_color='#343638', border_color='#565b5e', border_width=2, text_color='#8e9e8f')
        self.desc_text.grid(pady=10, padx=10, row=2, column=0, sticky='ew')
        self.desc_text.insert(1.0, 'Description')


        def on_click(event):
            current_text = self.desc_text.get("1.0", "end-1c")
            if current_text == 'Description':
                self.desc_text.delete("1.0", "end")
                self.desc_text.configure(text_color='#dce4ee')


        self.desc_text.bind("<Button-1>", on_click)

        self.amount_entry = customtkinter.CTkEntry(master=self.frame, placeholder_text='Amount', justify=CENTER)
        self.amount_entry.grid(pady=10, padx=10, row=3, column=0, sticky='ew')

        db = database_connect.DatabaseConnector()
        query = 'SELECT name FROM categories'
        results = db.select_data(query)
        categories = [r[0] for r in results]

        self.category = customtkinter.CTkOptionMenu(master=self.frame, values=categories)
        self.category.grid(pady=20, padx=10, row=4, column=0, sticky="ew")

        self.addbtn = customtkinter.CTkButton(master=self.frame, text='Add new expense', command = self.add_new_expense, font=('Arial', 25, 'normal'))
        self.addbtn.grid(padx=20, pady=10, row=5, column=0, sticky='ew')


    def add_new_expense(self):
        name = self.name_entry.get()
        desc = self.desc_text.get("1.0",END)
        amount = self.amount_entry.get()
        category = str(self.category.get())

        if name != '' and self.isfloat(amount) and float(amount) > 0:
            budget = Budget(self.id)
            cat_id = budget.get_category_id(category)
            budget.add_expense(name, desc, float(amount), cat_id)
            messagebox.showinfo('Success', 'You successfully added new expense!')
            self.destroy()
        else:
            messagebox.showerror("Error","Please enter valid data.")

    
    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
            