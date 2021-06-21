from tkinter import *
from tkinter import ttk, messagebox  # for a drop down menu
from PIL import Image, ImageTk  # to deal with images image tk deals with jpg format
import pymysql


class Register:
    def __init__(self, root):
        # setting the geometry of everything
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")  # height =700 (+0+0 means the starting point )
        self.root.config(bg="gray")
        # image for background
        self.bg = ImageTk.PhotoImage(file="Images/change.jpg")  # importing an image
        # we need to impose the image on a label
        bg = Label(self.root, image=self.bg).place(x=200, y=0, relwidth=1, relheight=1)

        # side image ([phone ])
        self.sec = ImageTk.PhotoImage(file="images/zze.jpg")
        sec = Label(self.root, image=self.sec).place(x=70, y=100, width=400, height=500)

        # creating a frame for regisration
        frame1 = Frame(self.root, bg='white')
        frame1.place(x=480, y=100, width=700, height=500)

        # for text on the form
        title = Label(frame1, text="Register Here!!", font=("times new roman", 25, "bold"), bg="white",
                      fg="blue").place(x=50, y=30)

        # credentials
        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(
            x=50, y=60)
        # creating a entry field
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=90, width=250)

        # for last name
        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black").place(
            x=400, y=60)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=400, y=90, width=250)

        # for contact number
        c_num = Label(frame1, text="Contact Number", font=("times new roman", 15, "bold"), bg="white",
                      fg="black").place(x=50, y=130)
        self.txt_con = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_con.place(x=50, y=160, width=250)

        # for email address can run a try or while loop till added in the right format
        # example re.findall(r'.@.com') i.e python quantifiers
        e_mail = Label(frame1, text="Email Address", font=("times new roman", 15, "bold"), bg="white",
                       fg="black").place(x=400, y=150)
        self.txt_mail = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_mail.place(x=400, y=180, width=250)

        # for securiy questions

        s_quest = Label(frame1, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white",
                        fg="black").place(x=50, y=220)

        # creating a drop down menu

        self.drop_men = ttk.Combobox(frame1, font=("times new roman", 13), state='readonly', justify=CENTER)
        # values for the drop down menu
        self.drop_men['values'] = ("Select", "Your First Pet Name ", "Your Birth place", "Best friends name")

        self.drop_men.place(x=50, y=250, width=250)
        # to display select in the first box
        self.drop_men.current(0)
        answer = Label(frame1, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=400,
                                                                                                                  y=240,
                                                                                                                  width=250)
        self.txt_answer = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=400, y=280, width=250)

        # run_val=1
        # while(run_val==1):

        passwrd = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(
            x=50, y=300)
        self.txt_passwrd = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_passwrd.place(x=50, y=330, width=250)

        conpasswrd = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                           fg="black").place(x=400, y=320)
        self.txt_conpasswrd = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_conpasswrd.place(x=400, y=350, width=250)
        #   if(txt_passwrd==txt_conpasswrd):
        #     run_val = 20
        # break;
        # else:
        # posted = Label(frame1,text="Password does not match ",font=("times new roman",15,"bold"),bg="white",fg = "black").place(x=30,y=480)
        # terms check box
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I agree to terms and conditions", variable=self.var_chk, onvalue=1,
                          offvalue=0).place(x=50, y=360)
        self.btnimg = ImageTk.PhotoImage(file='images/masterb.jpg')
        btn_register = Button(frame1, image=self.btnimg, bd=0, cursor="hand2", command=self.register_data).place(x=80,
                                                                                                                 y=385)

        btn_login = Button(self.root, text="Sign In ", font=("times new roman", 20), bd=0, cursor="hand2").place(x=360,
                                                                                                                 y=550)

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_con.delete(0, END)
        self.txt_mail.delete(0, END)
        self.drop_men.current(0)
        self.txt_answer.delete(0, END)
        self.txt_passwrd.delete(0, END)
        self.txt_conpasswrd.delete(0, END)

    # taking in input and printing them
    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        if self.txt_con.get() == "" or self.txt_mail.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        if self.drop_men.get() == "Select" or self.txt_answer.get() == "":
            s
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        if self.txt_passwrd.get() == " " or self.txt_conpasswrd.get() == " ":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        if self.txt_passwrd.get() != self.txt_conpasswrd.get():
            messagebox.showerror("Error", "Passwords don't match", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please accept our terms and conditions", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="123456", database="employee2")
                cur = con.cursor()
                cur.execute("select * from employee where email=%s", self.txt_mail.get())
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Error", "User Already exists Please try with another email", parent=self.root)

                else:
                    cur.execute(
                        "insert into employee (f_name,l_name,contact,email,question,answe,password) values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.txt_fname.get(), self.txt_lname.get(), self.txt_con.get(), self.txt_mail.get(),
                         self.drop_men.get(), self.txt_answer.get(), self.txt_passwrd.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                    self.clear()


            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)} ", parent=self.root)


root = Tk()  # object of tk
obj = Register(root)  # object of the cclass Register
root.mainloop()