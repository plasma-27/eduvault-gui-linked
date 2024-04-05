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
                bg="#272A37").grid(row=0, column=1, sticky="ew")
        
        tk.Label(self, 
                text="Size (in kb)",
                padx=30,
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=2, sticky="ew")

        tk.Label(self,
                text="  View  ",
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=3, sticky="ew")
        
        tk.Label(self,
                text=" ",
                fg="#FFFFFF",
                font=("yu gothic ui bold", 20 * -1),
                bg="#272A37").grid(row=0, column=0, sticky="ew")

        buttonImage1 = tk.PhotoImage(file="assets\\share.png")
        action_button1 = tk.Button(self,
                                  image=buttonImage1,
                                  borderwidth=0,
                                  highlightthickness=0,
                                  relief="flat",
                                  activebackground="#272A37",
                                  cursor="hand2"
                                  )
        action_button1.image=buttonImage1
            

        

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
            
            test_label = tk.Label(self,text= " ",
                                fg="#FFFFFF",
                                font=("yu gothic ui bold", 20 * -1),
                                bg="#272A37")
            
            C1 = tk.Checkbutton(self,
                                activebackground="#272A37", 
                                activeforeground="#272A37",
                                bg="#272A37",bd=6,
                                onvalue = 1, 
                                offvalue = 0)


    

            nr_label.grid(row=row, column=1, sticky="ew")
            name_label.grid(row=row, column=2, sticky="ew")
            test_label.grid(row=row - 1, column=3, sticky="ew")
            C1.grid(row = row, column = 0, sticky= "ew")

            row += 1
            
        action_button1.grid(row=n, column=3, sticky="ew")

        
              

       

      
def open_student_shate_docs(root):

    # root = tk.Tk()
    window = tk.Toplevel(root)
    window.title("Share Documents")
    # window.geometry("1166x600") # Increased size

    # Set background color
    window.configure(bg="#272A37")
    height = (n)*39 + 35
    width = 1240
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 4) - (height // 4)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    window.configure(bg="#525561")


    Example(window).pack(side="top", fill="both", expand=True, padx=10, pady=10)


    window.mainloop()


if __name__ == "__main__":
    open_student_shate_docs()