from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfWriter, PdfReader
import os

root = Tk()
root.title("Pdf Protector")
root.geometry("600x430+300+100")
root.resizable(False, False)


def browse():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select PDF File",
        filetype=(("PDF File", "*.pdf"), ("All Files", "*.*")),
    )
    entry1.delete(0, END)
    entry1.insert(END, filename)


def protect():
    mainfile = entry1.get()
    code = entry3.get()

    if mainfile == "" or code == "":
        messagebox.showerror("Invalid", "Please fill in all entries.")
    else:
        try:
            out = PdfWriter()
            file = PdfReader(mainfile)
            num = (len(file.pages))

            for idx in range(num):
                page = file.pages[idx]
                out.add_page(page)

            out.encrypt(code)

            with open(filename, "wb") as f:
                out.write(f)

            entry1.delete(0, END)
            entry3.delete(0, END)

            messagebox.showinfo("Success", "PDF file protected successfully!")
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "An error occurred while protecting PDF.")


image_icon = PhotoImage(file="e:/6th_sem/PWP/Microproject/Microproject/Images/icon.png")
root.iconphoto(False, image_icon)

Top_image = PhotoImage(file="e:/6th_sem/PWP/Microproject/Microproject/Images/main_image.png")
Label(root, image=Top_image).pack()

frame = Frame(root, width=580, height=290, bd=5, relief=GROOVE)
frame.place(x=10, y=130)

source = StringVar()
Label(frame, text="Source PDF File:", font="arial 10 bold", fg="#4c4541").place(
    x=30, y=50
)
entry1 = Entry(frame, width=30, textvariable=source, font="arial 15", bd=1)
entry1.place(x=150, y=48)

Button_icon=PhotoImage(file="e:/6th_sem/PWP/Microproject/Microproject/Images/button.png")
Button(
    frame,
    image=Button_icon,
    width=35,
    height=24,
    bg="#d3cdcd",
    command=browse
).place(x=500, y=47)

password = StringVar()
Label(
    frame,
    text="Set User Password:",
    font="arial 10 bold",
    fg="#4c4541"
).place(x=15, y=150)
entry3 = Entry(frame, width=30, textvariable=password, font="arial 15", bd=1)
entry3.place(x=150, y=150)

button_icon=PhotoImage(file="e:/6th_sem/PWP/Microproject/Microproject/Images/button image.png")
Button(
    root,
    text="Protect PDF File",
    compound=LEFT,
    image=button_icon,
    width=230,
    height=50,
    bg="#bfb9b9",
    font="arial 14 bold",
    command=protect
).pack(side=BOTTOM, pady=40)
root.mainloop()
