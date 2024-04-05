from tkinter import Tk, Frame,Text,Label, Button, BOTTOM, FLAT,Entry,Canvas,PhotoImage
from tkinter import ttk
from tkinter import messagebox
from file_operations_interface import *


def open_student_upload_docs(user_id,root):
    window = tk.Toplevel(root)
    window.title("Upload Documents")
    # window.geometry("1166x600") # Increased size

    # Set background color
    window.configure(bg="#272A37")
    # window = Tk()

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
        text="Upload Your Documents",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#000000"
    )
    headerText1.place(x=110, y=45)

    # ================ Line x1 ====================
    image2 = PhotoImage(file="assets\\line.png")
    image2_Label = Label(
        bg_image,
        image=image2,
        bg="#272A37"
    )
    image2_Label.place(x=60, y=130)


    # ================ Label 1 ====================
    image1 = PhotoImage(file="assets\\email.png")
    image1_Label = Label(
        bg_image,
        image=image1,
        bg="#000000"
    )
    image1_Label.place(x=60, y=170)

    Label1_text = Label(
        image1_Label,
        text="            Category",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 23),
        bg="#3d404b"
    )
    Label1_text.place(x=25, y=0)




    #=====------------------DROP DOWN      --------------- 

    # Define the style for combobox widget
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= "#272A37", background= "#272A37")

    # Add a Combobox widget
    cb= ttk.Combobox(window, width= 25, values=["Personal Documents", "Marksheets", "Certificates"], font=("Verdana 16 bold", 16), foreground = "white")

    cb.tk.eval('[ttk::combobox::PopdownWindow %s].f.l configure -foreground white -background black' % cb)
    cb.place(x = 95, y = 270)

    #cb.pack()

    # ================ Line x2 ====================

    image3_Label = Label(
        bg_image,
        image=image2,
        bg="#272A37"
    )
    image3_Label.place(x=60, y=350)

    # ================ Label 2 ====================
    image3 = PhotoImage(file="assets\\email.png")
    image3_Label = Label(
        bg_image,
        image=image1,
        bg="#000000"
    )
    image3_Label.place(x=60, y=400)

    Label2_text = Label(
        image3_Label,
        text="    Document Name",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 23),
        bg="#3d404b"
    )
    Label2_text.place(x=25, y=0)

    # ================ Label 3 ====================
    image4 = PhotoImage(file="assets\\email.png")
    image4_Label = Label(
        bg_image,
        image=image1,
        bg="#000000"
    )
    image4_Label.place(x=60, y=510)


    msg_entry = Text(
        image4_Label,
        bd=0,
        bg="#3d404b",
        fg='#ffffff',
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 13),
    )
    msg_entry.place(x=8, y=12, width=400, height=30)


    # ================ Line x3 ====================
    image5 = PhotoImage(file="assets\\line.png")
    image5_Label = Label(
        bg_image,
        image=image2,
        bg="#272A37"
    )
    image5_Label.place(x=60, y=590)

    def upload_file():
        # Get selected values from comboboxes
        document_name = msg_entry.get("1.0",'end-1c')
        category = cb.get()
        
        upload_file_selector(user_id,document_name,category)

        # Use these values for further processing, for example, calling the upload_file function
        # upload_file(self.uid, document_name, category)

        # For now, just print the selected values
        print(f"Uploading file for UID {user_id}, Document Name: {document_name}, Category: {category}")

    # =============== Button1 ====================
    buttonImage1 = PhotoImage(file="assets\\upload.png")
    button1 = Button(
        bg_image,
        image=buttonImage1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=upload_file
    )
    button1.place(x=500, y=560, width=320, height=65)






    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    open_student_upload_docs("S353356847444")