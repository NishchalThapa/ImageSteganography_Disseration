from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class LoginForm:
    def __init__(self):
        self.wn = Tk()
        self.wn.attributes("-fullscreen", True)

        x = ImageTk.PhotoImage(file='background.jpg')
        self.background_img_background = Label(self.wn, bd=0, image=x)
        self.background_img_background.place(x=0, y=0)

        self.Username_value = StringVar()
        self.Password_value = StringVar()

# ================ CANVAS =====================

        self.canvas = Canvas(self.wn)
        self.canvas.create_image(0, 0, image=x, anchor=NW)
        self.canvas.pack(fill='both', expand=True)

# ================ LABEL AND ENTRY =====================
        self.canvas.create_text(1300, 400, text='Login', fill='black', font=('times', 60, 'bold'))
        self.canvas.create_text(1050, 600, text='Username', fill='black', font=('times', 30, 'bold'))
        self.canvas.create_text(1050, 750, text='Password', fill='black', font=('times', 30, 'bold'))

        self.Username = Entry(self.wn, font=('bell mt', 20, 'bold'), textvariable=self.Username_value)
        self.Username.place(x=1150, y=588)

        self.show_password()
        self.hide_password()

# ================ BUTTON =====================
        self.Exit = Button(self.wn, text="EXIT", font=('bell mt', 15, 'bold'), bd=5, bg='red', fg='white',
                           command=self.exit_btn)
        self.Exit.place(x=-0, y=0)

        self.Login = Button(self.wn, text='Log In', font=('bell mt', 20, 'bold'), height=1)
                            # command=self.Login_Button)
        self.Login.place(x=1250, y=800)
        #
        #         # self.SignUp = Button(self.Frame, text='Click Here!', font=('bell mt', 14, 'bold', 'underline', 'italic'),
        #                              # fg='red', bd=0, command=self.Click_Here_Button)
        #         # self.SignUp.place(x=731, y=539)
        #
        #         # self.Forget_Password = Button(self.Frame, text='Forget Password', font=('bell mt', 15, 'bold', 'italic'),
        #                                       # fg='blue', bd=5, command=self.Forget_Password_Button)
        #         # self.Forget_Password.place(x=900, y=700)
        #
        #         # self.connection = Employee_data()

        self.wn.mainloop()

# ================ Method =====================
    def show_password(self):
        self.Password_Show = Entry(self.wn, font=('bell mt', 20, 'bold'), textvariable=self.Password_value)
        self.Password_Show.place(x=1150, y=733)

        self.hide_show = Button(self.wn, text='Hide', font=('bell mt', 14, 'bold'), height=1,
                                command=self.hide_password, width=6, bd=0)
        self.hide_show.place(x=1440, y=733)

    def hide_password(self):
        self.Password_Hide = Entry(self.wn, font=('bell mt', 20, 'bold'), textvariable=self.Password_value, show="x")
        self.Password_Hide.place(x=1150, y=733)

        self.hide_show = Button(self.wn, text='Show', font=('bell mt', 14, 'bold'), height=1,
                                command=self.show_password, width=6, bd=0)
        self.hide_show.place(x=1440, y=733)

    def exit_btn(self):
        ask = messagebox.askyesno('Exit', 'Do you want to exit?')
        if ask == 1:
            exit()
        else:
            pass

    # def Login_Button(self):
    #     username = self.Username.get()
    #     passwd1 = self.Password_Hide.get()
    #     passwd2 = self.Password_Show.get()
    #     self.passwd = passwd2
    #     self.passwd = passwd1
    #     # get_info = self.connection.extract_user_data(username)
    #     # post = get_info[0][5]
    #     if username == "" or self.passwd == "":
    #         messagebox.showerror('Error', 'Please Fill All Boxes')
    #     elif username == post:
    #         messagebox.showinfo('Sorry', 'User is not authorized to login \nContact your manager to grant access')
    #     else:
    #         hash = SHA256.new()
    #         hash.update(f"{self.passwd}".encode("utf-8"))
    #         hash_passwd = hash.hexdigest()
    #         print("Login IN", self.passwd, hash_passwd)
    #         if get_info:
    #             check_password = get_info[0][3]
    #             if check_password == hash_passwd:
    #                 self.Open_home_form(username, post)
    #             else:
    #                 messagebox.showerror('Error', 'Incorrect Passoword')
    #         else:
    #             messagebox.showerror('Error', "User doesn't exigist")

    # def Click_Here_Button(self):
    #     self.wn.destroy()
    #     # from Signup_Page import Signup_Form
    #     Signup_Form()
    #
    # def Forget_Password_Button(self):
    #     User = self.Username.get()
    #     if User == "":
    #         messagebox.showerror('Error', 'Enter your Username')
    #     elif self.connection.extract_user_data(User):
    #         self.wn.destroy()
    #         from Forget_Password_Page import Forget_Password_Form
    #         Forget_Password_Form(User)
    #     else:
    #         messagebox.showerror('Error', 'Invalid Username')
    #
    # def Open_home_form(self, username, post):
    #     self.wn.destroy()
    #     Home_Form(username, post)


LoginForm()
