import customtkinter


class App(customtkinter.CTk):
    """Main class that manages the app."""

    def __init__(self, screen_height):
        super().__init__()

        self.geometry(f"{round(screen_height * 1.78)}x{screen_height}")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        title = customtkinter.CTkLabel(self, text="JSV Converter", font=("Arial", 20), fg_color="transparent", pady=30)
        title.grid(row=0, column=0, columnspan=3)

        textbox_1 = customtkinter.CTkTextbox(self)
        textbox_1.grid(row=1, column=0, padx=(10, 5), sticky="nsew")
        textbox_2 = customtkinter.CTkTextbox(self)
        textbox_2.grid(row=1, column=1, padx=(5, 10), sticky="nsew")

        text_1 = customtkinter.CTkLabel(self, text="JSON", font=("Arial", 15), fg_color="transparent")
        text_1.grid(row=2, column=0)
        text_2 = customtkinter.CTkLabel(self, text="CSV", font=("Arial", 15), fg_color="transparent")
        text_2.grid(row=2, column=1)

        my_button_1 = customtkinter.CTkButton(self, text="<-=-\n-=->", width=40)
        my_button_1.grid(row=2, column=0, columnspan=3, pady=(10, 5))

        my_button_2 = customtkinter.CTkButton(self, text="My Button!")
        my_button_2.grid(row=3, column=0, columnspan=3, padx=(5, 5), pady=(5, 0), sticky="ew")


if __name__ == "__main__":
    app = App(500)
    app.mainloop()