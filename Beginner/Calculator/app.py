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

        # First button row
        self.division_button = customtkinter.CTkButton(self.button_frame, text="÷", width=75, height=75)
        self.division_button.grid(row=0, column=0)
        self.ce_button = customtkinter.CTkButton(self.button_frame, text="CE", width=75, height=75)
        self.ce_button.grid(row=0, column=1)
        self.c_button = customtkinter.CTkButton(self.button_frame, text="C", width=75, height=75)
        self.c_button.grid(row=0, column=2)
        self.delete_button = customtkinter.CTkButton(self.button_frame, text="<--", width=75, height=75)
        self.delete_button.grid(row=0, column=3)

        # Second button row
        self.one_button = customtkinter.CTkButton(self.button_frame, text="1", width=75, height=75)
        self.one_button.grid(row=1, column=0)
        self.two_button = customtkinter.CTkButton(self.button_frame, text="2", width=75, height=75)
        self.two_button.grid(row=1, column=1)
        self.three_button = customtkinter.CTkButton(self.button_frame, text="3", width=75, height=75)
        self.three_button.grid(row=1, column=2)
        self.times_button = customtkinter.CTkButton(self.button_frame, text="x", width=75, height=75)
        self.times_button.grid(row=1, column=3)

        # Third button row
        self.four_button = customtkinter.CTkButton(self.button_frame, text="4", width=75, height=75)
        self.four_button.grid(row=2, column=0)
        self.five_button = customtkinter.CTkButton(self.button_frame, text="5", width=75, height=75)
        self.five_button.grid(row=2, column=1)
        self.six_button = customtkinter.CTkButton(self.button_frame, text="6", width=75, height=75)
        self.six_button.grid(row=2, column=2)
        self.minus_button = customtkinter.CTkButton(self.button_frame, text="-", width=75, height=75)
        self.minus_button.grid(row=2, column=3)

        # Fourth button row
        self.seven_button = customtkinter.CTkButton(self.button_frame, text="7", width=75, height=75)
        self.seven_button.grid(row=3, column=0)
        self.eight_button = customtkinter.CTkButton(self.button_frame, text="8", width=75, height=75)
        self.eight_button.grid(row=3, column=1)
        self.nine_button = customtkinter.CTkButton(self.button_frame, text="9", width=75, height=75)
        self.nine_button.grid(row=3, column=2)
        self.plus_button = customtkinter.CTkButton(self.button_frame, text="+", width=75, height=75)
        self.plus_button.grid(row=3, column=3)

        # Fifth button row
        # self.division_button = customtkinter.CTkButton(self.button_frame, text="÷", width=75, height=75)
        # self.division_button.grid(row=4, column=0)
        self.zero_button = customtkinter.CTkButton(self.button_frame, text="0", width=75, height=75)
        self.zero_button.grid(row=4, column=1)
        self.comma_button = customtkinter.CTkButton(self.button_frame, text=",", width=75, height=75)
        self.comma_button.grid(row=4, column=2)
        self.equals_button = customtkinter.CTkButton(self.button_frame, text="=", width=75, height=75)
        self.equals_button.grid(row=4, column=3)


if __name__ == "__main__":
    app = App(300)
    app.mainloop()