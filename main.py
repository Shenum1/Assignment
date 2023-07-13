from tkinter import *
import locale

# Set the locale for Nigerian Naira
locale.setlocale(locale.LC_ALL, 'en_NG')

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance

def deposit_money():
    amount = float(deposit_entry.get())
    current_balance = account.get_balance()
    account.deposit(amount)
    updated_balance_label.config(text="Updated Balance: %s" % format_currency(account.get_balance()))

def withdraw_money():
    amount = float(withdraw_entry.get())
    current_balance = account.get_balance()
    if current_balance >= amount:
        account.withdraw(amount)
        updated_balance_label.config(text="Updated Balance: %s" % format_currency(account.get_balance()))
    else:
        messagebox.showwarning("Error", "Insufficient balance.")

def format_currency(amount):
    return locale.currency(amount, grouping=True)

# Create a bank account
account = BankAccount("John Doe", "12345678", 1000.00)

# Create a Tkinter window
window = Tk()
window.title("Banking System")

# Create labels and entry fields
account_name_label = Label(window, text="Account Name:")
account_name_label.pack()
account_name = Label(window, text=account.name)
account_name.pack()

account_number_label = Label(window, text="Account Number:")
account_number_label.pack()
account_number = Label(window, text=account.account_number)
account_number.pack()

current_balance_label = Label(window, text="Current Balance: %s" % format_currency(account.get_balance()))
current_balance_label.pack()

deposit_label = Label(window, text="Deposit Amount:")
deposit_label.pack()
deposit_entry = Entry(window)
deposit_entry.pack()

withdraw_label = Label(window, text="Withdraw Amount:")
withdraw_label.pack()
withdraw_entry = Entry(window)
withdraw_entry.pack()

# Create buttons
deposit_button = Button(window, text="Deposit", command=deposit_money)
deposit_button.pack()

withdraw_button = Button(window, text="Withdraw", command=withdraw_money)
withdraw_button.pack()

updated_balance_label = Label(window, text="Updated Balance: %s" % format_currency(account.get_balance()))
updated_balance_label.pack()

# Run the GUI
window.mainloop()
