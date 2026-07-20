import calendar
from datetime import date

import customtkinter


class App(customtkinter.CTk):
    """Class that manages the calendar."""
    
    def __init__(self, screen_height):
        super().__init__()

        self.title("Calendar")
        self.iconbitmap("calendar.ico")
        self.geometry(f"{round(screen_height * 1.55)}x{screen_height}")

        # self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        months = ["January", "February", "March", "May",
                       "April", "June", "July", "August",
                       "September", "October", "November", "December"]
        self.today_date = f"{months[date.today().month - 1]} {date.today().year}"

        # Head
        self.head_frame = customtkinter.CTkFrame(self)
        self.head_frame.grid(row=0, column=0, sticky="nsew")
        self.head_frame.columnconfigure((0, 1), weight=1)

        self.month_year = customtkinter.CTkLabel(self.head_frame, text=self.today_date, font=("Arial", 22))
        self.month_year.grid(row=0, column=1)

        self.left_button = customtkinter.CTkButton(self.head_frame, text="<")
        self.left_button.grid(row=0, column=0)


if __name__ == '__main__':
    app = App(550)
    app.mainloop()