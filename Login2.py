from tkinter import *
from PIL import Image,ImageTk
import pymysql  #for database
from tkinter import messagebox
import config
class Login:

    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost", user="root",password="", database="employee2")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_email.get(), self.txt_password.get()))
                row=cur.fetchone()
                print(row)
                if row==None:
                    messagebox.showerror("Error", "Invalid Username and Password", parent=self.root)
                else:
                    messagebox.showinfo("Login Success", "Welcome User!!", parent=self.root)
                    config.nickname = row[1]
                    self.root.destroy()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)

    def __init__(self,root):
        self.root = root
        self.root.title("Login Form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #====Bg image===
        self.bg=ImageTk.PhotoImage(file="images/bg3.jpg")
        bg=Label(self.root,image=self.bg).place(x=120,y=0,relwidth=1,relheight=1)

        # ====Left image===
        self.left = ImageTk.PhotoImage(file="images/avatar.png")
        left = Label(self.root, image=self.left).place(x=288, y=180, width=400, height=500)

        #===register Frame===
        frame1=Frame(self.root,bg="white")
        frame1.place(x=688,y=180,width=700,height=500)

        #===========frame heading=============
        title=Label(frame1,text="LOGIN HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)


        #=============email entry=============
        email = Label(frame1, text="Email Address", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(
            x=50, y=100)
        self.txt_email=Entry(frame1,font=("times new roman",14),bg="lightgray")
        self.txt_email.place(x=230,y=101,width =250)


        # =============password entry=============
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(
            x=50, y=150)
        self.txt_password = Entry(frame1, font=("times new roman", 14),bg="lightgray")
        self.txt_password.place(x=230, y=151, width=250)

        btn_login = Button(frame1, text="Sign In ", command=self.login, font=("times new roman", 20), bd=0,
                           cursor="hand2").place(x=120, y=230)

        btn_reg = Button(frame1, text="Register Here", command=self.regg, font=("times new roman", 20), bd=0,
                           cursor="hand2").place(x=300, y=230)

    def regg(self):
        root.destroy()
        import register;



root = Tk()
obj=Login(root)
root.mainloop()