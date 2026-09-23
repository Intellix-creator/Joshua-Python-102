import tkinter as tk
from tkinter import messagebox
import tkinter
window = tk.Tk()
window.geometry("500x500")
window.title("Enter Password you want to unlock the information")
window.config(bg="light blue")

def onClick():
    global PASSWORD  
    password = myEntry.get()
    number = "123456789"
    Lcase = "abcdefghijklmnopqrstuvwxyz"
    Ucase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "!@#$%^&*()_+"
    hasnumber = False
    hasLcase = False
    hasUcase = False
    hasSpecial = False
    for i in password:
        if i in number:
            hasnumber = True
        elif i in Lcase:
            hasLcase = True
        elif i in Ucase:
            hasUcase = True
        elif i in special:
            hasSpecial = True

    if len(password) < 8:
        myText.insert(tkinter.END, "Password is too short. It must be at least 8 characters long.\n")
    elif not hasnumber:
        myText.insert(tkinter.END, "Password must contain at least one number.\n")
    elif not hasLcase:
        myText.insert(tkinter.END, "Password must contain at least one lowercase letter.\n")
    elif not hasUcase:
        myText.insert(tkinter.END, "Password must contain at least one uppercase letter.\n")
    elif not hasSpecial:
        myText.insert(tkinter.END, "Password must contain at least one special character.\n")
    else:
        myText.insert(tkinter.END, "Password is strong.\n")
        PASSWORD = password



#we're creating a label widget and setting the text
myLabel = tkinter.Label(window,text= "Make Your password")
myLabel.pack ()
#this allows the label to be displayed in the window
myEntry = tkinter.Entry(window,width=20,bg="Light Green")
myEntry.pack()
#we're creating and entry setting and setting the
#bg coulour
myButton = tkinter.Button(window,width=13,bg = "Blue",
                          text = " ENTER Password",command =onClick) 
myButton.pack()
#we're creating a button widget and setting with the colour and the text
myText  = tkinter.Text(window,width=15,height = 7,bg= "Red")
myText.pack()





person_information = """
PERSONAL INFORMATION

Name: JOSH AGBAJE
Age: 14
Address: Manchester, UK

Status: PRIVATE INFORMATION
"""

def check_password():
    entered_password = password_entry.get()

    if entered_password == PASSWORD:
        login_frame.pack_forget()

        information_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        password_entry.delete(0, tk.END)

    else:
        messagebox.showerror(
            "Access Denied",
            "Incorrect password."
        )

        password_entry.delete(0, tk.END)

def lock_information():
    information_frame.pack_forget()

    login_frame.pack(
        fill="both",
        expand=True
    )

    password_entry.focus()

window = tk.Tk()

window.title("Private Information")
window.geometry("600x450")
window.resizable(False, False)

login_frame = tk.Frame(window)

login_frame.pack(
    fill="both",
    expand=True
)

title = tk.Label(
    login_frame,
    text="PRIVATE INFORMATION",
    font=("Arial", 24, "bold")
)

title.pack(pady=(70, 20))

instruction = tk.Label(
    login_frame,
    text="Enter your password to unlock the information",
    font=("Arial", 12)
)

instruction.pack(pady=10)

password_entry = tk.Entry(
    login_frame,
    font=("Arial", 16),
    show="*",
    width=25
)

password_entry.pack(pady=15)
password_entry.focus()

unlock_button = tk.Button(
    login_frame,
    text="UNLOCK",
    font=("Arial", 14, "bold"),
    width=15,
    command=check_password
)

unlock_button.pack(pady=15)

password_entry.bind(
    "<Return>",
    lambda event: check_password()
)

information_frame = tk.Frame(window)

information_title = tk.Label(
    information_frame,
    text="Information Unlocked",
    font=("Arial", 22, "bold")
)

information_title.pack(pady=20)

information_label = tk.Label(
    information_frame,
    text=person_information,
    font=("Arial", 13),
    justify="left"
)

information_label.pack(
    padx=40,
    pady=20
)

lock_button = tk.Button(
    information_frame,
    text="LOCK",
    font=("Arial", 13, "bold"),
    width=15,
    command=lock_information
)

lock_button.pack(pady=20)

window.mainloop()




window.mainloop()





































































