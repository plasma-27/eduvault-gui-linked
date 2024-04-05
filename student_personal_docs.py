import tkinter as tk

from tkinter import messagebox
import time

#set value of n (no of pending approvals)
global n
n = 6


class Example(tk.LabelFrame):
    def __init__(self, *args, **kwargs):
        tk.LabelFrame.__init__(self, *args, **kwargs)

        data = [
            # Nr. Name  Active
            ["dsfsvfdbtt",123],
            ["dscdvsfvfsdv",234],["dsfvbtb",678],
            ["fdfgbgf",456],["dsfbdfgnn",12],
            ["dvrgbdfgb",123]
            ]


        self.photo = tk.PhotoImage(file="assets\\admin_bg.png")
        self.grid_columnconfigure(1, weight=1)

        tk.Label(self,
                text="Document Name",
                fg="#FFFFFF",
                padx=30, 
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=0, sticky="ew")
        
        tk.Label(self, 
                text="Size (in kb)",
                padx=30,
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=1, sticky="ew")
        

        tk.Label(self,
                text="  View  ",
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=3, sticky="ew")

        tk.Label(self,
                text="  Delete ",
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=4, sticky="ew")

        row = 1

        for (nr, name) in data:
          
            nr_label = tk.Label(self,text=str(nr),
                                fg="#FFFFFF",
                                font=("yu gothic ui bold", 20 * -1),
                                bg="#272A37")

            name_label = tk.Label(self, 
                                  text=str(name),
                                  fg="#FFFFFF",
                                  font=("yu gothic ui bold", 20 * -1),
                                  bg="#272A37")


            buttonImage1 = tk.PhotoImage(file="assets\\approval_view.png")
            action_button1 = tk.Button(self,
                                      image=buttonImage1,
                                      borderwidth=0,
                                      highlightthickness=0,
                                      relief="flat",
                                      activebackground="#272A37",
                                      cursor="hand2"
                                      )
            action_button1.image=buttonImage1
            
            buttonImage2 = tk.PhotoImage(file="assets\\delete.png")
            action_button2 = tk.Button(self,
                                      image=buttonImage2,
                                      borderwidth=0,
                                      highlightthickness=0,
                                      relief="flat",
                                      activebackground="#272A37",
                                      cursor="hand2"
                                      )
            action_button2.image=buttonImage2
            
          

            nr_label.grid(row=row, column=0, sticky="ew")
            name_label.grid(row=row, column=1, sticky="ew")
       
            action_button1.grid(row=row, column=3, sticky="ew")
            action_button2.grid(row=row, column=4, sticky="ew")

            row += 1
      


def open_personal_docs(user_id,root):
    # root = tk.Tk()
    window = tk.Toplevel(root)
    window.title("Personal Documents")
    window.geometry("1166x600") # Increased size

    # Set background color
    window.configure(bg="#272A37")
    
    height = (n)*42 + 35
    width = 1240
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#525561")


    Example(window).pack(side="top", fill="both", expand=True, padx=10, pady=10)


    window.mainloop()


if __name__ == "__main__":
    open_personal_docs()
    