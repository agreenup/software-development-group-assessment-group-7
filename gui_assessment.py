from tkinter import *
from tkinter import ttk 
import tkinter.messagebox as tmsg

class Manage_Expense(Tk):
    def __init__(self, width, height):
        super().__init__()
        pos_x = (self.winfo_screenwidth()//2) - (width//2)
        pos_y = (self.winfo_screenheight()//2)-(height//2)
        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        self.iconbitmap("logo.ico")
        self.resizable(False, False)
        # self.load_form()
        
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
        title = self.expense_title.get()
        expense = self.expense_used.get()
        category = self.expense_category.get()
        if len(title)!=0 and len(expense)!=0 and category!="Select Category":
            category = self.expense_category.get()
            with open("expense.txt", "a") as f:
                f.write(title+","+expense+","+category+"\n")
                f.close()
            tmsg.showinfo("Congratulations", "Expense has been added in the system")
            self.expense_title.set("")
            self.expense_used.set("")
            self.expense_category.set("Select Category")
        else:
            tmsg.showerror("Error", "Something is missing in the form")

    def openDashboard(self):
        self.destroy()
        open_dashboard()

    def load_history(self):
        self.title("All Expenses")
        
        Button(self, text="Dashboard", command=self.openDashboard).pack(pady=30)
        
        table = ttk.Treeview(self, columns=["Title","Expense","Category"], show="headings")
        # titles of all the columns
        table.heading("Title", text="Title")
        table.heading("Expense", text="Expense")
        table.heading("Category", text="Category")

        # width of all the columns
        table.column("Title", width=120)
        table.column("Expense", width=110)
        table.column("Category", width=170)

        self.expenses = self.load_expenses_from_file()
        
        # set data on the table
        for expense in self.expenses:
            table.insert("", END, values=expense)

        table.pack()

        

        

    def load_expenses_from_file(self):
        expenses_tuples = []
        with open("expense.txt", "r") as f:
            all_records = f.readlines()

            for record in all_records:
                arr = record.strip().split(',')
                expenses_tuples.append((arr[0], arr[1], arr[2]))

        return expenses_tuples

        
def open_add_new_expense_form():
    # closing the previous window
    dashboard.destroy()
    new_expense_form = Manage_Expense(400, 400)
    new_expense_form.load_form()
    new_expense_form.mainloop()

def open_history_of_expenses():
    dashboard.destroy()
    history_window = Manage_Expense(400, 400)
    history_window.load_history()
    history_window.mainloop()

def open_dashboard():
    global dashboard
    dashboard = Tk()
    dashboard_width=400
    dashboard_height=200
    pos_x = (dashboard.winfo_screenwidth()//2) - (dashboard_width//2)
    pos_y = (dashboard.winfo_screenheight()//2)-(dashboard_height//2)
    dashboard.geometry(f"{dashboard_width}x{dashboard_height}+{pos_x}+{pos_y}")
    dashboard.title("Dashboard")
    # dashboard.config(bg="lightblue")
    dashboard.iconbitmap("logo.ico")
    dashboard.resizable(False, False)

    # Frame is used to make the buttons horizontal on the window
    center_frame = Frame(dashboard)
    # center_frame.config(bg="lightblue")
    center_frame.pack(pady=80)

    # adding two buttons for navigation i.e. Add New Expense and View History
    btn_add_new_expense = Button(center_frame, text="Add New Expense", bg="red", command=open_add_new_expense_form)
    btn_add_new_expense.pack(side="left", padx=10)

    btn_view_history = Button(center_frame, text="View History", bg="red", command=open_history_of_expenses)
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
        
        fg="black",
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
   