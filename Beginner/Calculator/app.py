import customtkinter


class App(customtkinter.CTk):
    """Main class that manages the GUI interface."""
    
    def __init__(self, screen_width):
        super().__init__()

        self.geometry(f"{screen_width}x{round(screen_width * 1.60)}")
        self.columnconfigure(0, weight=0)

        self.result = customtkinter.CTkLabel(self, text="0", fg_color="transparent", font=("Arial", 42), anchor="e", height=100)
        self.result.grid(row=0, column=0, sticky="ew", padx=(0, 5), pady=3.5)

        self.button_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.button_frame.grid(row=1, column=0, sticky="nsew", padx=1.5)

        buttons_size = 75

        number_fg_color = "#ABABAB"
        number_hover_color = "#A3A3A3"

        others_fg_color = "#9C9C9C"
        others_hover_color = "#8C8C8C"

        # First button row
        self.division_button = customtkinter.CTkButton(self.button_frame, text="÷", width=buttons_size, height=buttons_size, fg_color=others_fg_color, text_color="black", hover_color=others_hover_color)
        self.division_button.grid(row=0, column=0)
        self.ce_button = customtkinter.CTkButton(self.button_frame, text="CE", width=buttons_size, height=buttons_size, fg_color=others_fg_color, text_color="black", hover_color="#969696")
        self.ce_button.grid(row=0, column=1)
        self.c_button = customtkinter.CTkButton(self.button_frame, text="C", width=buttons_size, height=buttons_size, fg_color=others_fg_color, text_color="black", hover_color="#969696")
        self.c_button.grid(row=0, column=2)
        self.delete_button = customtkinter.CTkButton(self.button_frame, text="<—", width=buttons_size, height=buttons_size, fg_color=others_fg_color, text_color="black", hover_color="#969696")
        self.delete_button.grid(row=0, column=3)

        # Second button row
        self.one_button = customtkinter.CTkButton(self.button_frame, text="1", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.one_button.grid(row=1, column=0)
        self.two_button = customtkinter.CTkButton(self.button_frame, text="2", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.two_button.grid(row=1, column=1)
        self.three_button = customtkinter.CTkButton(self.button_frame, text="3", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.three_button.grid(row=1, column=2)
        self.times_button = customtkinter.CTkButton(self.button_frame, text="×", width=buttons_size, height=buttons_size, fg_color=others_fg_color, text_color="black", hover_color="#969696")
        self.times_button.grid(row=1, column=3)

        # Third button row
        self.four_button = customtkinter.CTkButton(self.button_frame, text="4", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.four_button.grid(row=2, column=0)
        self.five_button = customtkinter.CTkButton(self.button_frame, text="5", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.five_button.grid(row=2, column=1)
        self.six_button = customtkinter.CTkButton(self.button_frame, text="6", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.six_button.grid(row=2, column=2)
        self.minus_button = customtkinter.CTkButton(self.button_frame, text="-", width=buttons_size, height=buttons_size, fg_color=others_fg_color, text_color="black", hover_color="#969696")
        self.minus_button.grid(row=2, column=3)

        # Fourth button row
        self.seven_button = customtkinter.CTkButton(self.button_frame, text="7", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.seven_button.grid(row=3, column=0)
        self.eight_button = customtkinter.CTkButton(self.button_frame, text="8", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.eight_button.grid(row=3, column=1)
        self.nine_button = customtkinter.CTkButton(self.button_frame, text="9", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.nine_button.grid(row=3, column=2)
        self.plus_button = customtkinter.CTkButton(self.button_frame, text="+", width=buttons_size, height=buttons_size, fg_color=others_fg_color, text_color="black", hover_color="#969696")
        self.plus_button.grid(row=3, column=3)

        # Fifth button row
        self.invert_button = customtkinter.CTkButton(self.button_frame, text="+/-", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.invert_button.grid(row=4, column=0)
        self.zero_button = customtkinter.CTkButton(self.button_frame, text="0", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.zero_button.grid(row=4, column=1)
        self.comma_button = customtkinter.CTkButton(self.button_frame, text=",", width=buttons_size, height=buttons_size, fg_color=number_fg_color, text_color="black", hover_color=number_hover_color)
        self.comma_button.grid(row=4, column=2)
        self.equals_button = customtkinter.CTkButton(self.button_frame, text="=", width=buttons_size, height=buttons_size)
        self.equals_button.grid(row=4, column=3)


if __name__ == "__main__":
    app = App(300)
    app.mainloop()