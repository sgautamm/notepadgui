import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font
import os
root=tk.Tk()
root.title("Untitled - Notepad")
root.geometry("644x400")




    



def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()      


def exit():
    root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad")

def size():
    pass

def style():
    pass



TextArea = Text(root)
file = None
TextArea.pack(expand=True, fill=BOTH)



menubar=tk.Menu(root)

filemenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Exit",command=exit)


editmenu=tk.Menu(menubar,tearoff=0)

menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label = "Cut", command=cut)
editmenu.add_command(label = "Copy", command=copy)
editmenu.add_command(label = "Paste", command=paste)
editmenu.add_command(label="Font_size",command=size)
editmenu.add_command(label="Font_Style",command=style)


helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)

helpmenu.add_command(label = "About Notepad", command=about)


root.config(menu=menubar)




Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()







