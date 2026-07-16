import customtkinter


class App(customtkinter.CTk):
    """Main class that manages the GUI interface."""
    
    def __init__(self, screen_width):
        super().__init__()

        self.geometry(f"{screen_width}x{round(screen_width * 1.60)}")
        self.columnconfigure(0, weight=1)

        self.result = customtkinter.CTkLabel(self, text="0", fg_color="transparent", font=("Arial", 28), anchor="w")
        self.result.grid(row=0, column=0)

        self.button_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.button_frame.grid(row=1, column=0, sticky="nsew")

        self.division_button = customtkinter.CTkButton(self.button_frame, text="÷")
        self.division_button.grid(row=0, column=0, sticky="nsew")
        self.ce_button = customtkinter.CTkButton(self.button_frame, text="CE")
        self.ce_button.grid(row=0, column=1, sticky="nsew")
        self.c_button = customtkinter.CTkButton(self.button_frame, text="C")
        self.c_button.grid(row=0, column=2, sticky="nsew")
        self.delete_button = customtkinter.CTkButton(self.button_frame, text="<--")
        self.delete_button.grid(row=0, column=3, sticky="nsew")


if __name__ == "__main__":
    app = App(300)
    app.mainloop()