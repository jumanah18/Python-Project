import tkinter as tk

# assign the balance variable
balance = 2950
# creating the main window
root = tk.Tk()

# setting the window title and size
root.title("Password Entry")
root.geometry("450x300")


# create class that display our names
class Student:
    def display_names(self):
        frame1 = tk.Frame(root, bg="lightblue", padx=10, pady=10)
        frame1.pack(side=tk.BOTTOM, fill=tk.X, expand=True)
        l1 = tk.Label(frame1, text='Student names: \nJumanah Alhareth CF10', bg='lightblue', width=30, font='times')
        l1.pack()
        l2 = tk.Label(frame1, text='Habiba Alsubiani CF10', bg='lightblue', width=30, font='times')
        l2.pack()
        l3 = tk.Label(frame1, text='Raneem Alhajri CF10', bg='lightblue', width=30, font='times')
        l3.pack()
        l4 = tk.Label(frame1, text='Maha Alsuhayan CF10', bg='lightblue', width=30, font='times')
        l4.pack()
        l5 = tk.Label(frame1, text='Rahaf Bin Libdah CF10', bg='lightblue', width=30, font='times')
        l5.pack()


x = Student()
x.display_names()  # display the function


# defining the password function
def check_password():
    password = password_entry.get()
    #add a while loop
    while True:
        if password == "password123":
            root.destroy()
            # creating the new window for tax calculation
            new_window = tk.Tk()
            new_window.title("Tax Calculator")
            new_window.geometry("450x300")

            # create class that holds user information
            class info:
                def action(self):
                    frame2 = tk.Frame(new_window, bg='lightpink', padx=10, pady=10)
                    frame2.pack(fill=tk.X, side=tk.BOTTOM, expand=True)
                    label_4 = tk.Label(frame2, text='The user information: ', bg='pink', width=30, font='times')
                    label_4.pack()
                    label_5 = tk.Label(frame2, text='Username: Mohammad Abdulaziz \nUser Id: 1124569512',
                                       bg='lightpink', width=30, font='times')
                    label_5.pack()
                    label_6 = tk.Label(frame2,
                                       text='Last Deposit: +1000 \nLast Withdraw: -50 \nCurrent Balance: 2950SR',
                                       bg='lightpink', width=30, font='times')
                    label_6.pack()

            y = info()
            y.action()  # display the function

            # defining the tax calculation function
            def calculate_tax():
                value = float(value_entry.get())
                tax = value * 0.15
                result_label.config(text="Tax to be paid: " + str(tax))

            # adding the value entry field and tax calculation button
            value_label = tk.Label(new_window, text="Enter value:", width=50)
            value_label.pack(pady=10)
            value_entry = tk.Entry(new_window, width=20)
            value_entry.pack()
            calculate_button = tk.Button(new_window, text="Calculate Tax", command=calculate_tax, width=20, bg='beige')
            calculate_button.pack(pady=10)

            # adding the result label
            result_label = tk.Label(new_window, text="")
            result_label.pack()

            # define a function for depositing money
            def deposit():
                global balance
                amount = int(e1.get())
                balance = balance + amount
                balance_label.config(text="Balance: " + str(balance))

            # define a function for withdrawing money
            def withdraw():
                global balance
                amount = int(e1.get())
                if balance >= amount:
                    balance = balance - amount
                    balance_label.config(text="Balance: " + str(balance))

                else:
                    balance_label.config(text="Insufficient funds")

            # entry for the withdraw and deposit function
            e1 = tk.Entry(new_window, width=20)
            e1.pack(pady=10)
            balance_label = tk.Label(new_window, text='Balance: 2950')  # label
            balance_label.pack(pady=10)

            # buttons for the deposit and withdraw
            b1 = tk.Button(new_window, text='Deposit', bg='lightgreen', width=20, command=deposit)
            b1.pack()
            b2 = tk.Button(new_window, text='Withdraw', bg='lightgreen', width=20, command=withdraw)
            b2.pack()
        else:
            access_denied_label.config(text="Access Denied, Try again!")
        break

# adding the password entry field and submit button
password_label = tk.Label(root, text="Enter password:", width=50)
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*", width=20)
password_entry.pack()
submit_button = tk.Button(root, text="Submit", command=check_password, width=20, bg='beige')
submit_button.pack(pady=10)

# adding the access denied label
access_denied_label = tk.Label(root, text="", width=30)
access_denied_label.pack()

# displaying a welcome message
new_label = tk.Label(root, text="Welcome to ProBank!!", bg='lightblue', width=30, font='times')
new_label.pack(pady=30)

# create a frame to hold the contact info
frame = tk.Frame(root, bg="lightpink", padx=10, pady=10)
frame.pack(fill=tk.X)

# define the contact info using tuples and a dictionary
contactinfo = ('Contact us if you need help:')
thebanknumber = ('Number:\n0553662523')
thebankemail = {"email": "Email:\nprobank@hotmail.com"}

# create labels to display the contact info
contact_label = tk.Label(frame, bg="pink", text=contactinfo, width=50, font='times')
number_label = tk.Label(frame, bg="lightpink", text=thebanknumber, width=50, font='times')
email_label = tk.Label(frame, bg="lightpink", text=thebankemail["email"], width=50, font='times')

# pack the labels into the frame
contact_label.pack()
number_label.pack()
email_label.pack()

# running the main loop
root.mainloop()