import json
import customtkinter

from converter import Converter


class App(customtkinter.CTk):
    """Main class that manages the app."""

    def __init__(self, screen_height):
        super().__init__()

        # Base config
        self.geometry(f"{round(screen_height * 1.78)}x{screen_height}")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Variables
        self.mode = "json_to_csv"

        title = customtkinter.CTkLabel(self, text="JSV Converter", font=("Arial", 20), fg_color="transparent", pady=30)
        title.grid(row=0, column=0, columnspan=3)

        self.textbox_1 = customtkinter.CTkTextbox(self)
        self.textbox_1.grid(row=1, column=0, padx=(10, 5), sticky="nsew")
        self.textbox_2 = customtkinter.CTkTextbox(self)
        self.textbox_2.grid(row=1, column=1, padx=(5, 10), sticky="nsew")

        self.text_1 = customtkinter.CTkLabel(self, text="JSON", font=("Arial", 15), fg_color="transparent")
        self.text_1.grid(row=2, column=0)
        self.text_2 = customtkinter.CTkLabel(self, text="CSV", font=("Arial", 15), fg_color="transparent")
        self.text_2.grid(row=2, column=1)

        my_button_1 = customtkinter.CTkButton(self, text="<---\n--->", command=self.change_mode, width=38)
        my_button_1.grid(row=2, column=0, columnspan=3, pady=(10, 5))

        my_button_2 = customtkinter.CTkButton(self, text="CONVERT", command=self.convert, corner_radius=0)
        my_button_2.grid(row=3, column=0, columnspan=3, pady=(5, 0), sticky="ew")

    def change_mode(self):
        if self.mode == "json_to_csv":
            self.mode = "csv_to_json"
            self.text_1.configure(text="CSV")
            self.text_2.configure(text="JSON")
        else:
            self.mode = "json_to_csv"
            self.text_1.configure(text="JSON")
            self.text_2.configure(text="CSV")

    def convert(self):
        text = self.textbox_1.get("0.0", "end")
        self.textbox_2.delete("0.0", "end")

        if self.mode == "json_to_csv":
            content = Converter.text_json_to_csv(text)
        else:
            content = Converter.text_csv_to_json(text)

        self.textbox_2.insert("0.0", content)

if __name__ == "__main__":
    app = App(500)
    app.mainloop()