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
from student_profile import *
from institute_homepage import *
from institute_register import *
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

def show_otp_dialog(userid, window):
    if userid[0] == "S":
        user_type = "S"
    else:
        user_type = "I"

    generated_otp = generate_otp()
    user_info = currentUserInfo(userid, user_type)
    otp_send(generated_otp,user_info)
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
            print("opening institute profile page")
            # main(userid)
            open_institute_homepage(userid)
            
            return
        else:
            attempts += 1
            remaining_attempts = 3 - attempts
            messagebox.showerror("Incorrect OTP", f"The entered OTP is incorrect. You have {remaining_attempts} attempt(s) remaining. Please try again.")

    # If the maximum number of attempts is reached
    messagebox.showerror("Max Attempts Reached", "You have reached the maximum number of OTP attempts. Please try again later.")
    window.destroy()  # Close the main window
   
        
def submit(institute_id,institute_password,window):
    userid = institute_id

    check_if_user_is_suspended_user_id = str(userid)
    suspended = check_if_user_is_suspended(check_if_user_is_suspended_user_id,"I")
    suspended = 0
    password = institute_password
    if suspended :
        messagebox.showinfo("suspension notice","admin suspended you or your institute is not verified yet" ,icon=tk.messagebox.ERROR)
    else:
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
    
   

















class LoginPage:
    def __init__(self, window):
        self.window = window
        
        

        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=300, y=110)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "Hii Institute!"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=60, y=70, width=300, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector3.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=50, y=150)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Institute", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)

        


        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground = '#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)
        user_id = self.username_entry.get()

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=550, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.login)
        self.login.place(x=20, y=10)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        
        
        # =========== Sign Up ==================================================
        def load_institute_register():
            self.window.destroy()
            load_register()

        self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="#040405", fg='white')
        self.sign_label.place(x=550, y=560)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
        self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="#040405", activebackground="#040405",command=load_institute_register)
        self.signup_button_label.place(x=670, y=555, width=111, height=35)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground = '#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)
        user_password = self.password_entry.get()

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        
        # Footer
        self.footer_frame = Frame(self.window, bg='#040405', width=1166, height=30)
        self.footer_frame.pack(side=BOTTOM, fill='x')

        self.footer_label = Label(self.footer_frame, text='© 2024 EduVault. All rights reserved.', font=("Helvetica", 10), bg='#040405', fg='white')
        self.footer_label.pack(pady=5)


    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')
    
    def login(self):
        institute_id = self.username_entry.get()
        institute_password = self.password_entry.get()
        window = self.window
        submit(institute_id,institute_password,window)
        

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()


