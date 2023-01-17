import customtkinter
import tkinter

import user

import sql

class MainApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")

        self.geometry("500x600")
        self.title("App")

        tab_view = customtkinter.CTkTabview(master=self, width=250)
        tab_view.pack(padx=60, pady=20, fill="both", expand=True)

        tab_view.add("Clicker")
        tab_view.add("Leaderboard")

        if user.admin:
            tab_view.add("Admin Panel")

        button = customtkinter.CTkButton(tab_view.tab("Clicker"), text="Click Me!", width = 300, height = 500)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)




class LoginScreen(customtkinter.CTk):

    def register_window(self):
        new_window = customtkinter.CTkToplevel(self)
        new_window.title("Register")
        new_window.geometry("400x500")

        main_frame = customtkinter.CTkFrame(master=new_window)
        main_frame.pack(padx=60, pady=20, fill="both", expand=True)

        pad_canvas = customtkinter.CTkCanvas(master=main_frame, height=40, bg='#2b2b2b')
        pad_canvas.configure(highlightthickness=0)
        pad_canvas.pack(pady=3)

        user_label = customtkinter.CTkLabel(master=main_frame, justify=tkinter.LEFT, text="Username")
        user_label.pack()

        user_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text="Type here...")
        user_entry.pack()

        pad_canvas1 = customtkinter.CTkCanvas(master=main_frame, height=40, bg='#2b2b2b')
        pad_canvas1.configure(highlightthickness=0)
        pad_canvas1.pack(pady=3)

        pass_label = customtkinter.CTkLabel(master=main_frame, justify=tkinter.LEFT, text="Password")
        pass_label.pack()

        pass_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text="Type here...")
        pass_entry.pack()

        pad_canvas1 = customtkinter.CTkCanvas(master=main_frame, height=40, bg='#2b2b2b')
        pad_canvas1.configure(highlightthickness=0)
        pad_canvas1.pack(pady=3)

        email_label = customtkinter.CTkLabel(master=main_frame, justify=tkinter.LEFT, text="Email Address")
        email_label.pack()

        email_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text="Type here...")
        email_entry.pack()

        pad_canvas1 = customtkinter.CTkCanvas(master=main_frame, height=40, bg='#2b2b2b')
        pad_canvas1.configure(highlightthickness=0)
        pad_canvas1.pack(pady=3)

        license_label = customtkinter.CTkLabel(master=main_frame, justify=tkinter.LEFT, text="License Key")
        license_label.pack()

        license_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text="Type here...")
        license_entry.pack()

        register_button = customtkinter.CTkButton(master=main_frame, text="Register")
        register_button.pack(pady=30)

    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")

        self.geometry("400x500")
        self.title("Welcome")

        main_frame = customtkinter.CTkFrame(master=self)
        main_frame.pack(padx=60,pady=20, fill="both", expand=True)

        pad_canvas = customtkinter.CTkCanvas(master=main_frame, height=40, bg='#2b2b2b')
        pad_canvas.configure(highlightthickness=0)
        pad_canvas.pack(pady=10)

        user_label = customtkinter.CTkLabel(master=main_frame, justify=tkinter.LEFT, text="Username")
        user_label.pack()

        user_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text="Type here...")
        user_entry.pack()

        pad_canvas1 = customtkinter.CTkCanvas(master=main_frame, height=40, bg='#2b2b2b')
        pad_canvas1.configure(highlightthickness=0)
        pad_canvas1.pack(pady=10)

        pass_label = customtkinter.CTkLabel(master=main_frame, justify=tkinter.LEFT, text="Password")
        pass_label.pack()

        pass_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text="Type here...")
        pass_entry.pack()

        def login_routine():
            # status = sql.login(user_entry.get(), pass_entry.get())

            self.destroy()

            app = MainApp()
            app.mainloop()

        button = customtkinter.CTkButton(master=main_frame, text="Login", command=login_routine)
        button.place(relx = 0.5, rely = 0.8, anchor=tkinter.CENTER)

        register_button = customtkinter.CTkButton(master=main_frame, text="Don't have an account?", command=self.register_window)
        register_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)