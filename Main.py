from tkinter import *
import tkinter.messagebox

root = Tk()

CurrentCount = 0
CurrentCountText = StringVar(root, value="0")

def CloseProgram():
    root.destroy()

def UpdateCounter():
    CurrentCount = int(CurrentCountText.get())
    CurrentCount += 1
    CurrentCountText.set(str(CurrentCount))
    #tkinter.messagebox.showinfo( "Hello Python", "Hello World")

if __name__ == '__main__':   # vores "main" program
    root.title("Tkinter Example Branch LTPE -> Master")
    root.geometry("1024x768")

    lblHead = Label(root,
               text="Counter",
               fg="black",
               font="Helvetica 24 bold").place(x=40, y=100)

    lblCounter = Label(root,
                   text="Current Count: ",
                   fg="black",
                   font="Helvetica 16 bold").place(x=40, y=150)

    txtCounter = Entry(root,
                    textvariable = CurrentCountText,
                    font="Helvetica 16 bold",
                    fg = "black").place(x = 200, y = 150)

    btnCounter = Button(root,
                        command = UpdateCounter,
                        text = "Click me",
                        fg = "white",
                        bg = "blue",
                        font="Helvetica 16 bold").place(x = 40, y = 220)

    btnExit = Button(root,
                     command = CloseProgram,
                     text = "Exit",
                     fg = "white",
                     bg = "blue",
                     font="Helvetica 16 bold").place(x = 400, y = 500)

    root.mainloop()