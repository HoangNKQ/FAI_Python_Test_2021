#
# Github link: 
# https://github.com/HoangNKQ/FAI_Python_Test_2021
#

from tkinter import *
import psycopg2

def submit():
    name = nameVar.get()
    age = ageVar.get()
    address = addressVar.get()
    sex = sexVar.get()
    email = emailVar.get()
    phone = phoneVar.get()
    user = userVar.get()
    password = passVar.get()

    print(name, age, address, sex, email, phone, user, password, sep='\n')

    nameVar.set("")
    ageVar.set("")
    addressVar.set("")
    sexVar.set("")
    emailVar.set("")
    phoneVar.set("")
    userVar.set("")
    passVar.set("")

#Variables to store input data
root = Tk()
root.geometry("500x500")
root.title("Personal Information")
root.resizable(False,False)

#Tkinter Variables
nameVar = StringVar()
ageVar = IntVar()
addressVar = StringVar()
sexVar = StringVar()
emailVar = StringVar()
phoneVar = StringVar()
userVar = StringVar()
passVar = StringVar()

nameLabel = Label(root, text="Name", font=('calibre',10, 'bold'))
nameLabel.place(x=10, y=10)
ageLable = Label(root, text="Age", font=('calibre',10, 'bold'))
ageLable.place(x=10, y=60)
addressLabel = Label(root, text="Address", font=('calibre',10, 'bold'))
addressLabel.place(x=10, y=110)
sexLabel = Label(root, text="Sex", font=('calibre',10, 'bold'))
sexLabel.place(x=10, y=160)
emailLabel = Label(root, text="Email", font=('calibre',10, 'bold'))
emailLabel.place(x=10, y=210)
phoneLabel = Label(root, text="Phone Number", font=('calibre',10, 'bold'))
phoneLabel.place(x=10, y=260)
userLabel = Label(root, text="Username", font=('calibre',10, 'bold'))
userLabel.place(x=10, y=310)
passLabel = Label(root, text="Password", font=('calibre',10, 'bold'))
passLabel.place(x=10, y=360)

nameEntry = Entry(root, textvariable= nameVar, width= 80)
nameEntry.place(x=10, y=35)
ageEntry = Entry(root, textvariable= ageVar, width= 80)
ageEntry.place(x=10, y=85)
addressEntry = Entry(root, textvariable= addressVar, width= 80)
addressEntry.place(x=10, y=135)
sexEntry = Entry(root, textvariable= sexVar, width= 80)
sexEntry.place(x=10, y=185)
emailEntry = Entry(root, textvariable= emailVar, width= 80)
emailEntry.place(x=10, y=235)
phoneEntry = Entry(root, textvariable= phoneVar, width= 80)
phoneEntry.place(x=10, y=285)
userEntry = Entry(root, textvariable= userVar, width= 80)
userEntry.place(x=10, y=335)
passEntry = Entry(root, textvariable= passVar, show="*", width= 80)
passEntry.place(x=10, y=385)

submitButton = Button(root, text="SUBMIT",width=20, command=submit).place(x=10, y=445)

root.mainloop()