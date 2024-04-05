import tkinter as tk
from PIL import Image, ImageTk




from current_user_info import *
from dbConnection import *
from doc_upload_selector import *
from student_view_docs import *#////////////////////////////this is giving error not allowing login student to run
from student_share_docs import *
from student_upload_docs import *


def main(user_id):
    currentuser = currentUserInfo(user_id,"S")
# Function to fetch student name from the database (placeholder)
    def fetch_student_name():
    # Placeholder code to fetch student's name from the database
        return currentuser.name  # Replace this with actual retrieval logic from your database

# Function to fetch user information from the database (placeholder)
    def fetch_user_info():
    # Placeholder function to fetch user information from the database
    # Replace this with your actual database retrieval logic
        
        user_info = {
        "Name": currentuser.name ,
        "Email": currentuser.email,
        "Contact Number": currentuser.phone
        }
        return user_info

    def open_profile_window():
        user_info = fetch_user_info()  

    # Create a new window for the profile with increased size
        profile_window = tk.Toplevel(root)
        profile_window.title("Profile")
        profile_window.geometry("1166x600") # Increased size

    # Set background color
        profile_window.configure(bg="#272A37")

    # Load the background image
        bg_image = Image.open("assets//image_1.png")
        bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a label for the background image
        bg_label = tk.Label(profile_window, image=bg_photo, bg="#272A37")
        bg_label.image = bg_photo  # Retain a reference to avoid garbage collection
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Fetch student's name from the database
        student_name = currentuser.name

    # Load the header text image
        header_text_image = Image.open("assets//headerText_image.png")
        header_text_photo = ImageTk.PhotoImage(header_text_image)

        # Create a frame to hold the image and greeting label
        header_frame = tk.Frame(profile_window, bg="#272A37")
        header_frame.pack(anchor="w", padx=10, pady=10)

    # Create a label for the header text image
        header_text_label = tk.Label(header_frame, image=header_text_photo, bg="#272A37")
        header_text_label.image = header_text_photo  # Retain a reference to avoid garbage collection
        header_text_label.pack(side="left")

    # Create a label for the greeting
        greeting_label = tk.Label(header_frame, text=f"Welcome {student_name} !", fg="white", bg="#272A37", font=("yu gothic ui bold", 20))
        greeting_label.pack(side="left", padx=(10, 0), pady=(0, 10))

    # Display user information in labels with spacing between lines
        for key, value in user_info.items():
            label = tk.Label(profile_window, text=f"{key}: {value}\n", bg="#272A37", fg="white", font=("yu gothic ui bold", 14))
            label.pack(anchor="w", padx=10, pady=(0, 10))  # Add vertical spacing between lines



    

# Create the main window
    root = tk.Tk()
    root.geometry("1166x600")
    root.configure(bg="black")

    def open_share_documents_window():
        # root.destroy()
        open_student_shate_docs(root)

    frame = tk.Frame(root, bg="black")
    frame.pack(anchor="nw", padx=10, pady=10)

# Load the image
    image_path = "images/hyy.png"
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

# Create a label for the image
    image_label = tk.Label(frame, image=photo, bg="black")
    image_label.photo = photo  # Retain a reference to avoid garbage collection
    image_label.pack(side="left")

# Fetch student's name from the database
    student_name = fetch_student_name()

# Create a label for the greeting
    greeting_label = tk.Label(frame, text=f"Hii {student_name} !", fg="white", bg="black", font=("times New roman", 20))
    greeting_label.pack(side="left", padx=10)

    view_profile_button = tk.Button(root, text="View Profile", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                cursor='hand2', activebackground='#3047ff', fg='white', command=open_profile_window)
    view_profile_button.pack(anchor="w", padx=10, pady=(20, 40))

    def open_document_window():
        # root.destroy()
        open_view_docs(user_id,root)

    def view_personal_docs():
         print("View Personal Documents")

    def view_marksheets():
         print("View Marksheets")

    def view_certificates():
         print("View Certificates")

    view_document_button = tk.Button(root, text="View Document", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                 cursor='hand2', activebackground='#3047ff', fg='white', command=open_document_window)
    view_document_button.pack(anchor="w", padx=10, pady=(10, 40))

    share_document_button = tk.Button(root, text="Share Document", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                  cursor='hand2', activebackground='#3047ff', fg='white', command=open_share_documents_window)
    share_document_button.pack(anchor="w", padx=10, pady=(10, 40))

    change_password_button = tk.Button(root, text="Change Password", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                   cursor='hand2', activebackground='#3047ff', fg='white')
    change_password_button.pack(anchor="w", padx=10, pady=(10, 40))
    
    def upload_document():
        open_student_upload_docs(user_id,root)
        
    document_uplod_button = tk.Button(root, text="upload documents", font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff',
                                   cursor='hand2', activebackground='#3047ff', fg='white',command = upload_document)
    document_uplod_button.pack(anchor="w", padx=10, pady=(10, 40))

    # def upload_document():
        


    root.mainloop()

    
if __name__ =='__main__':
    main("S353356847444")