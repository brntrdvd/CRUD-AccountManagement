from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

id = 199999

def selectData(onClickRowTreeview):
    try:
        data = tv.selection()[0]

        eFirstname.delete(0, "end")
        eLastname.delete(0, "end")
        eUsername.delete(0, "end")
        ePassword.delete(0, "end")

        eFirstname.insert(0, tv.item(data)["values"][0])
        eLastname.insert(0, tv.item(data)["values"][1])
        eUsername.insert(0, tv.item(data)["values"][2])
        ePassword.insert(0, tv.item(data)["values"][3])
    except IndexError:
        messagebox.showinfo("No selection", "No specified row data.")

def addData():
    if eFirstname.get() == "" and eLastname.get() == "" and eUsername.get() == "" and ePassword.get() == "":
        messagebox.showinfo("Empty fields", "You cannot leave the fields empty.")
    elif eFirstname.get() == "":
        messagebox.showinfo("No firstname", "Please enter your firstname.")
    elif eLastname.get() == "":
        messagebox.showinfo("No lastname", "Please enter your lastname.")
    elif eUsername.get() == "":
        messagebox.showinfo("No username", "Please enter your username.")
    elif ePassword.get() == "":
        messagebox.showinfo("No password", "Please enter your password.")
    else:
        firstname = eFirstname.get().title()
        lastname = eLastname.get().title()
        username = eUsername.get()
        password = ePassword.get()

        if not re.search("[a-z]", password):
            messagebox.showinfo("Invalid password", "Password must contain lowercase, uppercase and numbers.")
        elif not re.search("[A-Z]", password):
            messagebox.showinfo("Invalid password", "Password must contain lowercase, uppercase and numbers.")
        elif not re.search("[0-9]", password):
            messagebox.showinfo("Invalid password", "Password must contain lowercase, uppercase and numbers.")
        else:
            global id
            id += 1

            tv.insert("", "end", text=id, values=(firstname, lastname, username, password))

            eFirstname.delete(0, "end")
            eLastname.delete(0, "end")
            eUsername.delete(0, "end")
            ePassword.delete(0, "end")

            for item in tv.selection():
                tv.selection_remove(item)

            messagebox.showinfo("Added", "Successfully added!")


def updateData():
    if eFirstname.get() == "" and eLastname.get() == "" and eUsername.get() == "" and ePassword.get() == "":
        messagebox.showinfo("No data", "Select an account to update.")
    elif eFirstname.get() == "":
        messagebox.showinfo("No firstname", "Please enter your firstname.")
    elif eLastname.get() == "":
        messagebox.showinfo("No lastname", "Please enter your lastname.")
    elif eUsername.get() == "":
        messagebox.showinfo("No username", "Please enter your username.")
    elif ePassword.get() == "":
        messagebox.showinfo("No password", "Please enter your password.")
    else:
        firstname = eFirstname.get().title()
        lastname = eLastname.get().title()
        username = eUsername.get()
        password = ePassword.get()

        data = tv.selection()[0]

        if firstname == tv.item(data)["values"][0] and lastname == tv.item(data)["values"][1] and username == tv.item(data)["values"][2] and password == tv.item(data)["values"][3]:
            messagebox.showinfo("No changes", "Data did not changed.")
        elif not re.search("[a-z]", password):
            messagebox.showinfo("Invalid password", "Password must contain lowercase, uppercase and numbers.")
        elif not re.search("[A-Z]", password):
            messagebox.showinfo("Invalid password", "Password must contain lowercase, uppercase and numbers.")
        elif not re.search("[0-9]", password):
            messagebox.showinfo("Invalid password", "Password must contain lowercase, uppercase and numbers.")
        else:
            tv.item(data, values=(firstname, lastname, username, password))

            eFirstname.delete(0, "end")
            eLastname.delete(0, "end")
            eUsername.delete(0, "end")
            ePassword.delete(0, "end")

            for item in tv.selection():
                tv.selection_remove(item)

            messagebox.showinfo("Updated", "Successfully updated!")

def deleteData():
    if eFirstname.get() == "" and eLastname.get() == "" and eUsername.get() == "" and ePassword.get() == "":
        messagebox.showinfo("No data", "Select an account to delete.")
    else:
        confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this account?")
        if confirm == 1:
            data = tv.selection()[0]
            tv.delete(data)

            eFirstname.delete(0, "end")
            eLastname.delete(0, "end")
            eUsername.delete(0, "end")
            ePassword.delete(0, "end")
        else:
            print("Cancelled delete.")

def clearData():
    if eFirstname.get() == "" and eLastname.get() == "" and eUsername.get() == "" and ePassword.get() == "":
        messagebox.showinfo("No data", "The fields are already empty.")
    else:
        eFirstname.delete(0, "end")
        eLastname.delete(0, "end")
        eUsername.delete(0, "end")
        ePassword.delete(0, "end")

        for item in tv.selection():
            tv.selection_remove(item)

def systemExit():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm == 1:
        sys.exit()
    else:
        print("Cancelled exit.")

#WINDOW
window = Tk()
window.title("Account Management")
windowWidth = 1096
windowHeight = 480
screenWidth = window.winfo_screenwidth()
x = (screenWidth/2) - (windowWidth/2)
window.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, x, 260))
window.resizable(0, 0)

#FRAME
topFrame = Frame(window)
topFrame.pack()

leftFrame = Frame(window)
leftFrame.pack(side=LEFT)

rightFrame = Frame(window)
rightFrame.pack(side=TOP)

#HEADER/TITLE
lblTitle = Label(topFrame, text="ACCOUNT MANAGEMENT")
lblTitle.config(font=("tahoma", 15, "bold"))
lblTitle.pack(pady=(10, 0))

#USER INPUT

lblFirstname = Label(leftFrame, text="Firstname")
lblFirstname.config(font=("tahoma", 10, "bold"))
lblFirstname.pack()

eFirstname = Entry(leftFrame, width=30)
eFirstname.pack(padx=10)

lblLastname = Label(leftFrame, text="Lastname")
lblLastname.config(font=("tahoma", 10, "bold"))
lblLastname.pack()

eLastname = Entry(leftFrame, width=30)
eLastname.pack()

lblUsername = Label(leftFrame, text="Username")
lblUsername.config(font=("tahoma", 10, "bold"))
lblUsername.pack()

eUsername = Entry(leftFrame, width=30)
eUsername.pack()

lblPassword = Label(leftFrame, text="Password")
lblPassword.config(font=("tahoma", 10, "bold"))
lblPassword.pack()

ePassword = Entry(leftFrame, width=30)
ePassword.pack(pady=(0, 25))

#BUTTON
btnAdd = Button(leftFrame, text="Add", width=22, command=addData)
btnAdd.config(font=("tahoma", 10, "bold"))
btnAdd.pack(pady=(25, 5))

btnUpdate = Button(leftFrame, text="Update", width=22, command=updateData)
btnUpdate.config(font=("tahoma", 10, "bold"))
btnUpdate.pack(pady=5)

btnDelete = Button(leftFrame, text="Delete", width=22, command=deleteData)
btnDelete.config(font=("tahoma", 10, "bold"))
btnDelete.pack(pady=5)

btnClear = Button(leftFrame, text="Clear", width=22, command=clearData)
btnClear.config(font=("tahoma", 10, "bold"))
btnClear.pack(pady=5)

btnExit = Button(leftFrame, text="Exit", width=22, command=systemExit)
btnExit.config(font=("tahoma", 10, "bold"))
btnExit.pack(pady=5)

#TREEVIEW
tv = ttk.Treeview(rightFrame, column=("Firstname", "Lastname", "Username", "Password"))
tv.heading("#0", text="Account ID")
tv.heading("#1", text="Firstname")
tv.heading("#2", text="Lastname")
tv.heading("#3", text="Username")
tv.heading("#4", text="Password")
tv.column("#0", width=80)
tv.bind('<ButtonRelease-1>', selectData)
tv.config(height=20)
tv.pack(padx=(0, 10), pady=10)

window.mainloop()