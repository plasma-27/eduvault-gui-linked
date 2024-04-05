from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from institute_homepage import *
import tkinter as tk


def load_institute_view_docs(root):
    # window = Tk()
    window = tk.Toplevel(root)
    window.title("View Documents")
    window.geometry("1166x600") # Increased size

    # Set background color
    window.configure(bg="#272A37")

    def search():
        print("search button is clicked")

    height = 650
    width = 1240
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#525561")

    # ================Background Image ====================
    backgroundImage = PhotoImage(file="assets\\institute_view_docs_bg.png")
    bg_image = Label(
        window,
        image=backgroundImage,
        bg="#525561"
    )
    bg_image.place(x=0, y=0)

    # ================ Header Text Left ====================
    headerText_image_left = PhotoImage(file="assets\\headerText_image.png")
    headerText_image_label1 = Label(
        bg_image,
        image=headerText_image_left,
        bg="#000000"
    )
    headerText_image_label1.place(x=60, y=45)

    headerText1 = Label(
        bg_image,
        text="View Documents",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#000000"
    )
    headerText1.place(x=110, y=45)


    # ================ Enter uid ====================
    image1 = PhotoImage(file="assets\\input_img.png")
    image1_Label = Label(
        bg_image,
        image=image1,
        bg="#000000"
    )
    image1_Label.place(x=60, y=90)

    uid_text = Label(
        image1_Label,
        text="Enter UID",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3d404b"
    )
    uid_text.place(x=25, y=0)

    uid_entry = Entry(
        image1_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    uid_entry.place(x=8, y=17, width=140, height=27)

    # =============== Button1 ====================
    buttonImage1 = PhotoImage(file="assets\\search.png")
    button1 = Button(
        bg_image,
        image=buttonImage1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=search
    )
    button1.place(x=300, y=87, width=320, height=65)

    # ================ Line ====================
    image2 = PhotoImage(file="assets\\line.png")
    image2_Label = Label(
        bg_image,
        image=image2,
        bg="#272A37"
    )
    image2_Label.place(x=60, y=190)

    # ================  msg ====================
    image3 = PhotoImage(file="assets\\institute_docs_msg.png")
    image3_Label = Label(
        bg_image,
        image=image3,
        bg="#000000"
    )
    image3_Label.place(x=60, y=260)

    msg_text = Label(
        image3_Label,
        text="All Documents are listed below: ",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 16),
        bg="#3d404b"
    )
    msg_text.place(x=25, y=0)

    msg_entry = Text(
        image3_Label,
        bd=0,
        bg="#3d404b",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 13),
    )
    msg_entry.place(x=8, y=42, width=580, height=227)
       ############################# backbutton #################
    def load_institute_homepage():
        window.destroy()
        open_institute_homepage()
        
    buttonImage2 = PhotoImage(file="assets\\back.png")
    button2 = Button(
        bg_image,
        image=buttonImage2,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=load_institute_homepage
    )
    button2.place(x=290, y=575, width=60, height=55)

    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    load_institute_view_docs(root)