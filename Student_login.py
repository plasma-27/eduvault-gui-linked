from tkinter import Tk, Frame, Label, Button, BOTTOM, FLAT,Entry,Canvas
from PIL import ImageTk, Image















# from student_register import studentSignup
# from institute_register import instituteSignup
from tkinter import messagebox
from dbConnection import *
from password import *
from postLogin import *
from login_activity import *
from otp import *
from tkinter import simpledialog
from current_user_info import *
from demo2 import *
from student_profile import *
from check_if_user_suspended import *



  
# def show_otp_dialog(userid, window):
#     if (userid[0]=="S"):
#         user_type = "S"
#     else:
#         user_type = "I"    
#     generated_otp = generate_otp()
#     user_info = currentUserInfo(userid,user_type)
#     # otp_send(generated_otp,user_info)
#     while True:  # Keep asking for OTP until correct or user cancels
#         otp = simpledialog.askstring("OTP Verification", f"Please enter the OTP {generated_otp} sent to your registered E-mail Id:")

#         # if otp is None:
            
#         #     window.destroy()  # Close the main window
#         #     return

#         if verify_otp(otp, generated_otp):
#             update_last_login(userid)
#             window.destroy()  # Close the login window
#             # display_hello(userid)
#             userMainWindow = userHomePage(user_info)
#             userMainWindow.run()
#             return
#         else: 
#             messagebox.showerror("Incorrect OTP", "The entered OTP is incorrect. Please try again.")


    
def open_student_login():
    def show_otp_dialog(userid, window):
        if userid[0] == "S":
            user_type = "S"
        else:
            user_type = "I"

        generated_otp = generate_otp()
        user_info = currentUserInfo(userid, user_type)
        # otp_send(generated_otp,user_info)
        attempts = 0
        while attempts < 3:  # Limit the maximum number of attempts to 3
            otp = simpledialog.askstring("OTP Verification", f"Please enter the OTP {generated_otp} sent to your registered E-mail Id:")

            if otp is None:
                window.destroy()  # Close the main window
                return

            if verify_otp(otp, generated_otp):
                update_last_login(userid)
                window.destroy()  # Close the login window
                # userMainWindow = userHomePage(user_info)
                # userMainWindow.run()
                main(userid)
                return
            else:
                attempts += 1
                remaining_attempts = 3 - attempts
                messagebox.showerror("Incorrect OTP", f"The entered OTP is incorrect. You have {remaining_attempts} attempt(s) remaining. Please try again.")

        # If the maximum number of attempts is reached
        messagebox.showerror("Max Attempts Reached", "You have reached the maximum number of OTP attempts. Please try again later.")
        window.destroy()  # Close the main window
   
        
    def submit():
        userid = Login_emailName_entry.get()
        check_if_user_is_suspended_user_id = str(userid)
        suspended = check_if_user_is_suspended(check_if_user_is_suspended_user_id,"S")
        if suspended :
            messagebox.showinfo("suspension notice","admin suspended you " ,icon=tk.messagebox.ERROR)
        else :
            password = Login_passwordName_entry.get()
            
            
            if not userid or not password:
                messagebox.showerror("Error", "Please enter both userid and password.")
                
                return
            
            dbobj = db()
            mydb,cursor = dbobj.dbconnect("credentials")
            
            query_boiledPass = "SELECT hash from login WHERE uid=%s"
            query_uid=userid
            cursor.execute(query_boiledPass, (query_uid,))
            resultTuple = cursor.fetchone()
            if resultTuple is None:
                # User does not exist
                messagebox.showerror("Error", "User does not exist.")
                return
            else:
                raw_boiledhash = resultTuple[0]
                
                passFuncobj = passFunc("key",password,password)
                isPasswordVerified = passFuncobj.passVerify(password,raw_boiledhash)
            print("submit button is clicked")
            if isPasswordVerified:
                show_otp_dialog(userid,window)
        
            else:
                messagebox.showerror("Access Denied","Invalid userid or Password")


    window = Tk()
    window.title("EduVault : Academic Records Management")  # Set the title of the window

    height = 650
    width = 1240
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#040405")

    # ================ Background Image ====================
    Login_backgroundImage = PhotoImage(file="assets/image_1.png")
    bg_imageLogin = Label(
        window,
        image=Login_backgroundImage,
        bg="#040405"
    )
    bg_imageLogin.place(x=120, y=28)

    # ================ Header Text Left ====================
    Login_headerText_image_left = PhotoImage(file="assets/headerText_image.png")
    Login_headerText_image_label1 = Label(
        bg_imageLogin,
        image=Login_headerText_image_left,
        bg="#272A37"
    )
    Login_headerText_image_label1.place(x=60, y=45)

    Login_headerText1 = Label(
        bg_imageLogin,
        text="EduVault",
        fg="#FFFFFF",
        font=("yu gothic ui bold", 20 * -1),
        bg="#272A37"
    )
    Login_headerText1.place(x=110, y=45)

    # ================ LOGIN TO ACCOUNT HEADER ====================
    loginAccount_header = Label(
        bg_imageLogin,
        text="Login to continue",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 28 * -1),
        bg="#272A37"
    )
    loginAccount_header.place(x=75, y=121)

    # ================ NOT A MEMBER TEXT ====================
    loginText = Label(
        bg_imageLogin,
        text="Not a Member?",
        fg="#FFFFFF",
        font=("yu gothic ui Regular", 15 * -1),
        bg="#272A37"
    )
    loginText.place(x=75, y=187)

    # ================ GO TO SIGN UP ====================
    switchSignup = Button(
        bg_imageLogin,
        text="Student Register",
        fg="#206DB4",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,   
        cursor="hand2",
        activebackground="#272A37",
        activeforeground="#ffffff"
    )
    switchSignup.place(x=220, y=185, width=150, height=35)




    switchInstituteSignup = Button(
        bg_imageLogin,
        text="Institute Register",
        fg="#206DB4",
        font=("yu gothic ui Bold", 15 * -1),
        bg="#272A37",
        bd=0,
        cursor="hand2",
        activebackground="#272A37",
        activeforeground="#ffffff",
        # command=instituteSignup  
    )
    switchInstituteSignup.place(x=switchSignup.winfo_x() + switchSignup.winfo_reqwidth() + 250, y=185, width=150, height=35)

    # ================ Email Name Section ====================
    Login_emailName_image = PhotoImage(file="assets/email.png")
    Login_emailName_image_Label = Label(
        bg_imageLogin,
        image=Login_emailName_image,
        bg="#272A37"
    )
    Login_emailName_image_Label.place(x=76, y=242)

    Login_emailName_text = Label(
        Login_emailName_image_Label,
        text="UserID",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    Login_emailName_text.place(x=25, y=0)

    Login_emailName_icon = PhotoImage(file="assets/email-icon.png")
    Login_emailName_icon_Label = Label(
        Login_emailName_image_Label,
        image=Login_emailName_icon,
        bg="#3D404B"
    )
    Login_emailName_icon_Label.place(x=370, y=15)

    Login_emailName_entry = Entry(
        Login_emailName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    Login_emailName_entry.place(x=8, y=17, width=354, height=27)

    # ================ Password Name Section ====================
    Login_passwordName_image = PhotoImage(file="assets/email.png")
    Login_passwordName_image_Label = Label(
        bg_imageLogin,
        image=Login_passwordName_image,
        bg="#272A37"
    )
    Login_passwordName_image_Label.place(x=80, y=330)

    Login_passwordName_text = Label(
        Login_passwordName_image_Label,
        text="Password",
        fg="#FFFFFF",
        font=("yu gothic ui SemiBold", 13 * -1),
        bg="#3D404B"
    )
    Login_passwordName_text.place(x=25, y=0)

    Login_passwordName_icon = PhotoImage(file="images\\password_icon.png")
    Login_passwordName_icon_Label = Label(
        Login_passwordName_image_Label,
        image=Login_passwordName_icon,
        bg="#3D404B"
    )
    Login_passwordName_icon_Label.place(x=370, y=15)

    Login_passwordName_entry = Entry(
        Login_passwordName_image_Label,
        bd=0,
        bg="#3D404B",
        highlightthickness=0,
        font=("yu gothic ui SemiBold", 16 * -1),
    )
    Login_passwordName_entry.place(x=8, y=17, width=354, height=27)

    # =============== Submit Button ====================
    Login_button_image_1 = PhotoImage(file="assets/button_1.png")
    Login_button_1 = Button(
        bg_imageLogin,
        image=Login_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        activebackground="#272A37",
        cursor="hand2",
        command=submit
    )
    Login_button_1.place(x=120, y=445, width=333, height=65)

    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    open_student_login()















# class LoginPage:
#     def __init__(self, window):
#         self.window = window
#         self.window.geometry('1166x718')
#         self.window.resizable(0, 0)
#         self.window.state('zoomed')
#         self.window.title('Login Page')

#         # ========================================================================
#         # ============================background image============================
#         # ========================================================================
#         self.bg_frame = Image.open('background1.png')
#         photo = ImageTk.PhotoImage(self.bg_frame)
#         self.bg_panel = Label(self.window, image=photo)
#         self.bg_panel.image = photo
#         self.bg_panel.pack(fill='both', expand='yes')
#         # ====== Login Frame =========================
#         self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
#         self.lgn_frame.place(x=300, y=110)

#         # ========================================================================
#         # ========================================================
#         # ========================================================================
#         self.txt = "Hii Student!"
#         self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
#                              fg='white',
#                              bd=5,
#                              relief=FLAT)
#         self.heading.place(x=60, y=50, width=300, height=30)

#         # ========================================================================
#         # ============ Left Side Image ================================================
#         # ========================================================================
#         self.side_image = Image.open('images\\vector2.png')
#         photo = ImageTk.PhotoImage(self.side_image)
#         self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
#         self.side_image_label.image = photo
#         self.side_image_label.place(x=100, y=150)

#         # ========================================================================
#         # ============ Sign In Image =============================================
#         # ========================================================================
#         self.sign_in_image = Image.open('images\\hyy.png')
#         photo = ImageTk.PhotoImage(self.sign_in_image)
#         self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
#         self.sign_in_image_label.image = photo
#         self.sign_in_image_label.place(x=620, y=130)

#         # ========================================================================
#         # ============ Sign In label =============================================
#         # ========================================================================
#         self.sign_in_label = Label(self.lgn_frame, text="Student", bg="#040405", fg="white",
#                                     font=("yu gothic ui", 17, "bold"))
#         self.sign_in_label.place(x=650, y=240)

#         # ========================================================================
#         # ============================username====================================
#         # ========================================================================
#         self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
#                                     font=("yu gothic ui", 13, "bold"))
#         self.username_label.place(x=550, y=300)

#         self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
#                                     font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
#         self.username_entry.place(x=580, y=335, width=270)

#         self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
#         self.username_line.place(x=550, y=359)
#         # ===== Username icon =========
#         self.username_icon = Image.open('images\\username_icon.png')
#         photo = ImageTk.PhotoImage(self.username_icon)
#         self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
#         self.username_icon_label.image = photo
#         self.username_icon_label.place(x=550, y=332)

#         # ========================================================================
#         # ============================login button================================
#         # ========================================================================
#         self.lgn_button = Image.open('assets\\button_1.png')
#         photo = ImageTk.PhotoImage(self.lgn_button)
#         self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
#         self.lgn_button_label.image = photo
#         self.lgn_button_label.place(x=550, y=450)
#         self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
#                             bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=submit)
#         self.login.place(x=20, y=10)
#         # ========================================================================
#         # ============================Forgot password=============================
#         # ========================================================================
        
        
#         # =========== Sign Up ==================================================
#         self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
#                                 relief=FLAT, borderwidth=0, background="#040405", fg='white')
#         self.sign_label.place(x=550, y=560)

#         self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
#         self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
#                                           borderwidth=0, background="#040405", activebackground="#040405")
#         self.signup_button_label.place(x=670, y=555, width=111, height=35)

#         # ========================================================================
#         # ============================password====================================
#         # ========================================================================
#         self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
#                                     font=("yu gothic ui", 13, "bold"))
#         self.password_label.place(x=550, y=380)

#         self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
#                                     font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
#         self.password_entry.place(x=580, y=416, width=244)

#         self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
#         self.password_line.place(x=550, y=440)
#         # ======== Password icon ================
#         self.password_icon = Image.open('images\\password_icon.png')
#         photo = ImageTk.PhotoImage(self.password_icon)
#         self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
#         self.password_icon_label.image = photo
#         self.password_icon_label.place(x=550, y=414)
#         # ========= show/hide password ==================================================================
#         self.show_image = ImageTk.PhotoImage \
#             (file='images\\show.png')

#         self.hide_image = ImageTk.PhotoImage \
#             (file='images\\hide.png')

#         self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
#                                   activebackground="white"
#                                   , borderwidth=0, background="white", cursor="hand2")
#         self.show_button.place(x=860, y=420)
        
#         # Footer
#         self.footer_frame = Frame(self.window, bg='#040405', width=1166, height=30)
#         self.footer_frame.pack(side=BOTTOM, fill='x')

#         self.footer_label = Label(self.footer_frame, text='© 2024 EduVault. All rights reserved.', font=("Helvetica", 10), bg='#040405', fg='white')
#         self.footer_label.pack(pady=5)

#     def show(self):
#         self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
#                                   activebackground="white"
#                                   , borderwidth=0, background="white", cursor="hand2")
#         self.hide_button.place(x=860, y=420)
#         self.password_entry.config(show='')

#     def hide(self):
#         self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
#                                   activebackground="white"
#                                   , borderwidth=0, background="white", cursor="hand2")
#         self.show_button.place(x=860, y=420)
#         self.password_entry.config(show='*')
        
    


# def page():
#     window = Tk()
#     LoginPage(window)
#     window.mainloop()


# if __name__ == '__main__':
#     page()