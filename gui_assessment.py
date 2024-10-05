from tkinter import *

def open_dashboard():
    dashboard = Tk()
    dashboard_width=400
    dashboard_height=200
    pos_x = (dashboard.winfo_screenwidth()//2) - (dashboard_width//2)
    pos_y = (dashboard.winfo_screenheight()//2)-(dashboard_height//2)
    dashboard.geometry(f"{dashboard_width}x{dashboard_height}+{pos_x}+{pos_y}")
    dashboard.title("Dashboard")
    dashboard.config(bg="lightblue")
    dashboard.iconbitmap("logo.ico")
    dashboard.resizable(False, False)

    # adding two buttons for navigation i.e. Add New Expense and View History
    center_frame = Frame(dashboard)
    center_frame.config(bg="lightblue")
    center_frame.pack(pady=80)

    btn_add_new_expense = Button(center_frame, text="Add New Expense", bg="red")
    btn_add_new_expense.pack(side="left", padx=10)

    btn_view_history = Button(center_frame, text="View History", bg="red")
    btn_view_history.pack(side="left", padx=10)

    dashboard.mainloop()

def open_splash_screen():
    splash_screen = Tk()
    splash_screen_width = 400
    splash_screen_height = 400
    pos_x = (splash_screen.winfo_screenwidth()//2)-(splash_screen_width//2)
    pos_y = (splash_screen.winfo_screenheight()//2)-(splash_screen_height//2)
    splash_screen.title("Expense Management App")
    splash_screen.iconbitmap("logo.ico")
    splash_screen.geometry(f"{splash_screen_width}x{splash_screen_height}+{pos_x}+{pos_y}")
    splash_screen.resizable(False, False)
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
    
    
    splash_screen.after(3000, open_dashboard)
    splash_screen.after(3000, splash_screen.destroy)
    
    splash_screen.mainloop()

if __name__ == "__main__":
    open_splash_screen()