import customtkinter as CTK
from PIL import Image, ImageTk
import string
import tkinter
from password import generate_password


class App(CTK.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("800x600")
        self.title("PAROLKIN")
        self.resizable(False, False)
        CTK.set_default_color_theme("purple.json")

        # Header
        self.logo = CTK.CTkImage(dark_image=Image.open("dark_logo.png"), size=(500, 200))
        CTK.set_appearance_mode("Light")
        self.logo_label = CTK.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0, padx=(150, 50), pady=(20, 0))

        # Main
        self.password_frame = CTK.CTkFrame(master=self, fg_color="transparent", height=40)
        self.password_frame.grid(row=1, column=0, padx=(100, 0), pady=(10, 0), sticky="nsew")

        self.entry_password = CTK.CTkEntry(master=self.password_frame, width=450, height=35, 
                                           placeholder_text="The password will appear here", 
                                           state="normal", font=("Roboto", 16))
        self.entry_password.grid(row=0, column=0, padx=(20, 25))

        self.btn_generate = CTK.CTkButton(master=self.password_frame, text="Generate", width=80,
                                          command=self.set_password, height=35, font=("Roboto", 16))
        
        self.btn_generate.grid(row=0, column=1)

        self.settings_frame = CTK.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(100, 0), pady=(50, 0), sticky="nsew")

        self.password_length_slider = CTK.CTkSlider(master=self.settings_frame, from_=12, to=100, number_of_steps=100,
                                             command=self.slider_event)
        
        self.password_length_slider.grid(row=1, column=0, columnspan=3, padx=(150, 0), pady=(30, 20), sticky="ew")
        
        self.password_length_entry = CTK.CTkLabel(master=self.settings_frame, height=20, fg_color="#a394ca",
                                                  corner_radius=8, text_color="black", font=("Roboto", 14))
        self.password_length_entry.grid(row=1, column=3, padx=(50, 10), pady=(10, 0), sticky="we")

        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = CTK.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cb_digits_var,
                                         onvalue=string.digits, offvalue="")
        self.cb_digits.grid(row=3, column=0, padx=(100, 0), pady=(20,10))
        
        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = CTK.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var,
                                         onvalue=string.ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=3, column=1, pady=(20,10))
        
        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = CTK.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var,
                                         onvalue=string.ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=3, column=2, pady=(20,10))

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = CTK.CTkCheckBox(master=self.settings_frame, text="@#$%..", variable=self.cb_symbol_var,
                                         onvalue=string.punctuation, offvalue="")
        self.cb_symbol.grid(row=3, column=3, pady=(8,0))
        
        self.appearance_mode_option_menu = CTK.CTkOptionMenu(master=self.settings_frame,
                                                             values=["Light", "Dark"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=4, column=0, columnspan=4, padx=(50, 0), pady=(40, 10))


        self.password_length_slider.set(12)
        self.password_length_entry.configure(text="12")
        self.appearance_mode_option_menu.set("Light")

        self.cb_digits_var.trace('w', self.validate_selection)
        self.cb_lower_var.trace('w', self.validate_selection)
        self.cb_upper_var.trace('w', self.validate_selection)
        self.cb_symbol_var.trace('w', self.validate_selection)


    def validate_selection(self, *args):
        chars = "".join([
            self.cb_digits_var.get(),
            self.cb_lower_var.get(),
            self.cb_upper_var.get(),
            self.cb_symbol_var.get()
        ])
        
        if chars:
            self.hide_error()
        else:
            self.show_error("Please select at least one character type!")

            
    def show_error(self, message):
        if not hasattr(self, 'error_label'):
            self.error_label = CTK.CTkLabel(
                master=self.settings_frame, 
                text_color="red",
                fg_color="transparent",
                font=("Roboto", 18),
                text=message
            )
            self.error_label.grid(row=2, column=0, columnspan=4, pady=(10, 10), padx=(100, 0))
        else:
            self.error_label.configure(text=message)
            self.error_label.grid()

    def hide_error(self):
        if hasattr(self, 'error_label'):
            self.error_label.grid_remove()
        
    
    def change_appearance_mode_event(self, new_apperance_mode):
        CTK.set_appearance_mode(new_apperance_mode)
        if new_apperance_mode == "Dark":
            logo_path = "light_logo.png"
        else:
            logo_path = "dark_logo.png"
        self.logo = CTK.CTkImage(dark_image=Image.open(logo_path), size=(500, 200))
        self.logo_label.configure(image=self.logo)


    def slider_event(self, value):
        self.password_length_entry.configure(text="")
        self.password_length_entry.configure(text=int(value))

    
    def get_characters(self):
        chars = "".join([
            self.cb_digits_var.get(),
            self.cb_lower_var.get(), 
            self.cb_upper_var.get(),
            self.cb_symbol_var.get()
        ])
        if chars:
            self.hide_error()
            return chars
        else:
            self.show_error("Please select at least one character type!")
            return None


    def set_password(self):
        if self.get_characters():
            self.entry_password.delete(0, "end")
            self.entry_password.insert(0, generate_password(length=int(self.password_length_slider.get()),
                                                        characters=self.get_characters()))
        else:
            return

if __name__=="__main__":

    app = App()

    app.mainloop()
