import pyshorteners
from tkinter import *
win=Tk()
win.geometry("400x270")
win.configure(bg="pink")

def short():
    url=entry1.get()
    s=pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)

Label(win,text="Enter your url link",font='impact 17 bold',bg='black',fg='white').pack(fill="x")

entry1= Entry(win,font="10",bd=3,width=30)
entry1.pack(pady=30)
Button(win,text="Click Me",font="impact 12 ",bg="black",fg="white",width=14,command=short).pack()
entry2=Entry(win,font="impact 16 bold",bg='pink',width=24)
entry2.pack(pady=30)
win.mainloop()