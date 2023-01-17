import customtkinter
import tkinter

class App(customtkinter.CTk):
    def register_window(self):
        new_window = customtkinter.CTkToplevel(self)
        new_window.title("Register")
        new_window.geometry("400x500")

        main_frame = customtkinter.CTkFrame(master=new_window)
        main_frame.pack(padx=60, pady=20, fill="both", expand=True)

        pad_canvas = customtkinter.CTkCanvas(master=main_frame, height=40, bg='#2b2b2b')
        pad_canvas.configure(highlightthickness=0)
        pad_canvas.pack(pady=10)

    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")

        self.geometry("400x500")
        self.title("App")

        main_frame = customtkinter.CTkFrame(master=self)
        main_frame.pack(padx=60,pady=20, fill="both", expand=True)

        pad_canvas = customtkinter.CTkCanvas(master=main_frame, height=40, bg='#2b2b2b')
        pad_canvas.configure(highlightthickness=0)
        pad_canvas.pack(pady=10)

        user_label = customtkinter.CTkLabel(master=main_frame, justify=tkinter.LEFT, text="Username")
        user_label.pack()

        user_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text="Type here...")
        user_entry.pack()

        def print_entry():
            print(user_entry.get())

        pad_canvas1 = customtkinter.CTkCanvas(master=main_frame, height=40, bg='#2b2b2b')
        pad_canvas1.configure(highlightthickness=0)
        pad_canvas1.pack(pady=10)

        pass_label = customtkinter.CTkLabel(master=main_frame, justify=tkinter.LEFT, text="Password")
        pass_label.pack()

        pass_entry = customtkinter.CTkEntry(master=main_frame, placeholder_text="Type here...")
        pass_entry.pack()

        button = customtkinter.CTkButton(master=main_frame, text="Login", command=print_entry)
        button.place(relx = 0.5, rely = 0.8, anchor=tkinter.CENTER)

        register_button = customtkinter.CTkButton(master=main_frame, text="Don't have an account?", command=self.register_window)
        register_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)