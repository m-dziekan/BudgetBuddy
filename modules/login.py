from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class Login(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x350")
        self.minsize(500, 350)
        self.title = "Login in to your account"
        self.frame = customtkinter.CTkFrame(master=self, width=1000, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.resizable(False, False)

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_rowconfigure(4, weight=1)

        self.frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.label = customtkinter.CTkLabel(master=self.frame, text="Budget Buddy", font=("Arial", 24, "normal"))
        self.label.grid(pady=12, padx=10, row=0, column=1)

        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Login")
        self.entry1.grid(pady=12, padx=10, row=1, column=1)

        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.entry2.grid(pady=12, padx=10, row=2, column=1)

        self.button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.login)
        self.button.grid(pady=12, padx=10, row=3, column=1)

        self.checkbox = customtkinter.CTkCheckBox(master=self.frame, text="Remember me")
        self.checkbox.grid(pady=12, padx=10, row=4, column=1)

    def login(self):
        print("Test")
