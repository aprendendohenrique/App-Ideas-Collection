import customtkinter


def button_callback():
    print("Button pressed")


app = customtkinter.CTk()
app.title("my app")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="My Button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
app.grid_columnconfigure(0, weight=1)

app.mainloop()