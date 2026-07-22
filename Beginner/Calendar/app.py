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

        self.cl = calendar.Calendar()

        self.rowconfigure(0, weight=0, minsize=75)
        self.rowconfigure(1, weight=1)

        self.columnconfigure(0, weight=1)

        self.months = ["January", "February", "March", "April",
                       "May", "June", "July", "August",
                       "September", "October", "November", "December"]
        self.month = date.today().month
        self.year = date.today().year
        self.today_date = f"{self.months[self.month - 1]} {self.year}"
        self.day_size = 70

        # Head
        self.head_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.head_frame.grid(row=0, column=0, sticky="nsew")
        self.head_frame.rowconfigure(0, weight=1)
        self.head_frame.columnconfigure((0, 1, 2), weight=1)

        self.month_year = customtkinter.CTkLabel(self.head_frame, text=self.today_date, font=("Arial", 22))
        self.month_year.grid(row=0, column=1)

        self.left_button = customtkinter.CTkButton(self.head_frame, text="<", command=self.minus_month)
        self.left_button.grid(row=0, column=0, sticky="w")
        self.right_button = customtkinter.CTkButton(self.head_frame, text=">", command=self.plus_month)
        self.right_button.grid(row=0, column=2, sticky="e")

        # Body
        self.body_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.body_frame.grid(row=1, column=0, sticky="nsew", pady=20)
        self.body_frame.columnconfigure(0, weight=1)
        self.body_frame.rowconfigure(0, weight=1)

        self.calendar_frame = customtkinter.CTkFrame(self.body_frame, fg_color="transparent")
        self.calendar_frame.grid(row=0, column=0)

        # Week days
        self.sun = customtkinter.CTkLabel(self.calendar_frame, fg_color="#C2C2C2", border_color="gray",
                                          border_width=1,
                                          text="Sunday", width=self.day_size, height=round(self.day_size / 4))
        self.sun.grid(row=0, column=0)

        self.mon = customtkinter.CTkLabel(self.calendar_frame, fg_color="#C2C2C2", border_color="gray",
                                          border_width=1,
                                          text="Monday", width=self.day_size, height=round(self.day_size / 4))
        self.mon.grid(row=0, column=1)

        self.tue = customtkinter.CTkLabel(self.calendar_frame, fg_color="#C2C2C2", border_color="gray",
                                          border_width=1,
                                          text="Tuesday", width=self.day_size, height=round(self.day_size / 4))
        self.tue.grid(row=0, column=2)

        self.wen = customtkinter.CTkLabel(self.calendar_frame, fg_color="#C2C2C2", border_color="gray",
                                          border_width=1,
                                          text="Wednesday", width=self.day_size, height=round(self.day_size / 4))
        self.wen.grid(row=0, column=3)

        self.thu = customtkinter.CTkLabel(self.calendar_frame, fg_color="#C2C2C2", border_color="gray",
                                          border_width=1,
                                          text="Thursday", width=self.day_size, height=round(self.day_size / 4))
        self.thu.grid(row=0, column=4)

        self.fri = customtkinter.CTkLabel(self.calendar_frame, fg_color="#C2C2C2", border_color="gray",
                                          border_width=1,
                                          text="Friday", width=self.day_size, height=round(self.day_size / 4))
        self.fri.grid(row=0, column=5)

        self.sat = customtkinter.CTkLabel(self.calendar_frame, fg_color="#C2C2C2", border_color="gray",
                                          border_width=1,
                                          text="Saturday", width=self.day_size, height=round(self.day_size / 4))
        self.sat.grid(row=0, column=6)

        # Days
        for count, week in enumerate(self.cl.monthdayscalendar(self.year, self.month)):
            for c, day in enumerate(week):
                button = DayBtn(self.calendar_frame, text=day, size=self.day_size)
                button.grid(row=count + 1, column=c, padx=(1, 1), pady=1)


    def generate_month(self):
        days = []
        for count, week in enumerate(self.cl.monthdayscalendar(self.year, self.month)):
            for c, day in enumerate(week):
                days.append(day)
        count = 0
        for widget in self.calendar_frame.winfo_children():
            if isinstance(widget, customtkinter.CTkFrame):
                for w in widget.winfo_children():
                    if isinstance(w, customtkinter.CTkLabel):
                        w.configure(text=f"{days[count]}")
                        count += 1


    def update_month_year(self):
        self.today_date = f"{self.months[self.month - 1]} {self.year}"
        self.month_year.configure(text=self.today_date)


    def minus_month(self):
        self.month -= 1
        if self.month <= 0:
            self.month = 12
            self.year -= 1
        self.update_month_year()
        self.generate_month()

    def plus_month(self):
        self.month += 1
        if self.month >= 13:
            self.month = 1
            self.year += 1
        self.update_month_year()
        self.generate_month()


class DayBtn(customtkinter.CTkFrame):
    
    def __init__(self, master, text, size):
        super().__init__(master)

        self.configure(width=size, height=size, border_width=1.5, fg_color="transparent", border_color="gray", corner_radius=0)
        self.grid_propagate(False)

        self.columnconfigure(0, weight=1)

        if text != 0:
            self.label = customtkinter.CTkLabel(self, text=text, fg_color="transparent", height=round(size / 5),
                                                font=("Arial", round(size / 6.5)))
            self.label.grid(row=0, column=0, sticky="e", padx=(0, 6), pady=4)
        else:
            self.label = customtkinter.CTkLabel(self, text="", fg_color="transparent", height=round(size / 5),
                                                font=("Arial", round(size / 6.5)))
            self.label.grid(row=0, column=0, sticky="e", padx=(0, 6), pady=4)


if __name__ == '__main__':
    app = App(550)
    app.mainloop()
