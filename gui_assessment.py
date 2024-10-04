from tkinter import *

def open_dashboard():
    dashboard = Tk()
    dashboard_width=400
    dashboard_height=400
    pos_x = (dashboard.winfo_screenwidth()//2) - (dashboard_width//2)
    pos_y = (dashboard.winfo_screenheight()//2)-(dashboard_height//2)
    dashboard.geometry(f"{dashboard_width}x{dashboard_height}+{pos_x}+{pos_y}")
    dashboard.title("Dashboard")
    dashboard.config(bg="lightblue")
    dashboard.iconbitmap("logo.ico")

    dashboard.mainloop()

def open_splash_screen():
    splash_screen = Tk()
    splash_screen_width = 400
    splash_screen_height = 400
    pos_x = (splash_screen.winfo_screenwidth()//2)-(splash_screen_width//2)
    pos_y = (splash_screen.winfo_screenheight()//2)-(splash_screen_height//2)
    splash_screen.title("Expense Management App")
    splash_screen.iconbitmap("logo.ico")
    title_label = Label(
        text="Expense Management\n\nLoading...", 
        bg="lightblue", 
        fg="white",
        padx=100,
        pady=300,
        font=("comicsansms", 19, "bold"),
        borderwidth=3,
        relief=SUNKEN
        )
    title_label.pack()
    
    splash_screen.geometry(f"{splash_screen_width}x{splash_screen_height}+{pos_x}+{pos_y}")
    splash_screen.after(3000, open_dashboard)
    splash_screen.after(3000, splash_screen.destroy)
    
    splash_screen.mainloop()

open_splash_screen()