from tkinter import *
from tkinter import ttk

class Add_Expense(Tk):
    def __init__(self, width, height):
        super().__init__()
        pos_x = (self.winfo_screenwidth()//2) - (width//2)
        pos_y = (self.winfo_screenheight()//2)-(height//2)
        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        self.iconbitmap("logo.ico")
        self.resizable(False, False)
        self.load_form()
        
    def load_form(self):

        # using grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1)

        Label(
            self, 
            text="Add New Expense From Here", 
            font="comicsansms 16 bold"
            ).grid(row=0, column=0, columnspan=4)
        self.expense_title_label = Label(self, text="Title : ")
        self.expense_used_label = Label(self, text="Expense : ")
        self.expense_category_label = Label(self, text="Category : ")
        self.expense_title_label.grid(row=2, column=1, sticky="e")
        self.expense_used_label.grid(row=3, column=1, sticky="e")
        self.expense_category_label.grid(row=4, column=1, sticky="e")
        # need to add here a dropdown
        self.expense_title = StringVar()
        self.expense_used = StringVar()

        self.expense_title_entry = Entry(self, textvariable=self.expense_title)
        self.expense_used_entry = Entry(self, textvariable=self.expense_used)
        self.categories = ["Food & Groceries", "Transportation", "Housing", "Utilities & Bills", "Healthcare",
                            "Entertainment & Leisure", "Education", "Clothing & Personal", "Insurance", "Saving & Investment",
                            "Debt Repayment","Miscellaneous","Gifts & Donations","Travel","Bussiness",
                            "Family and Childcare","Taxes"]
        self.expense_category = ttk.Combobox(self, values=self.categories)
        self.expense_title_entry.grid(row=2, column=2, sticky="w", padx=20, pady=3, ipady=3, ipadx=10)
        self.expense_used_entry.grid(row=3, column=2, sticky="w", padx=20, pady=3, ipady=3, ipadx=10)
        self.expense_category.grid(row=4, column=2, sticky="w", padx=20, pady=3, ipady=3)
        self.expense_category.set("Select Category")

        # add buttons
        self.frame = Frame(self)
        self.frame.grid(row=5, column=2, sticky="w")

        btnCancel = Button(self.frame, text="Cancel", command=self.openDashboard)
        btnCancel.pack(side="left", ipady=5, padx=15)
        btnAdd = Button(self.frame, text="Add Expense", command=self.saveExpenseInFile)
        btnAdd.pack(side="left", ipady=5, padx=5)
        

        

    def saveExpenseInFile(self):
        pass

    def openDashboard(self):
        pass
        
def open_add_new_expense_form():
    # closing the previous window
    dashboard.destroy()
    new_expense_form = Add_Expense(400, 400)
    new_expense_form.mainloop()

def open_dashboard():
    global dashboard
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

    # Frame is used to make the buttons horizontal on the window
    center_frame = Frame(dashboard)
    center_frame.config(bg="lightblue")
    center_frame.pack(pady=80)

    # adding two buttons for navigation i.e. Add New Expense and View History
    btn_add_new_expense = Button(center_frame, text="Add New Expense", bg="red", command=open_add_new_expense_form)
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
    #open_splash_screen()
    test = Add_Expense(410, 400)
    test.mainloop()