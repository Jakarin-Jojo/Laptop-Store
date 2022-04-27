from tkinter import *
from utilities.session import LaptopDB

session = LaptopDB()
window = Tk()
window.title("Laptop Store")


def all_customer():
    message = Message(text=session.customer().get_all_customer(), width=1000)
    message.pack()


def all_laptop():
    message = Message(text=session.laptop().get_all_laptop(), width=1000)
    message.pack()


Button(text="All Customer", command=all_customer).pack()
Button(text="All Laptop", command=all_laptop).pack()

h = Scrollbar(window, orient='horizontal')
h.pack(side=BOTTOM, fill=X)
v = Scrollbar(window)
v.pack(side=RIGHT, fill=Y)

window.geometry("800x800")
window.resizable()
window.mainloop()
