from tkinter import *
import sqlite3
from sqlite3 import Error
global main_windows
main_windows = Tk()
main_windows.title("Welcome To Chatroom")
a_icon = PhotoImage(file="./icons/icon.png")
main_windows.iconphoto(False,a_icon)
windows_width = 1000
windows_height = 500
main_windows.resizable =(False,False)
main_windows.geometry("%dx%d"%(windows_width,windows_height))
frame = Frame(main_windows,height=windows_height, width=windows_width, bg="white")
frame.pack()

def main_menu(frame):
    def signup_call(frame):
        frame.destroy()
        signup(main_windows)
            
    welcome_label = Label(frame, text="Welcome", font=("Helvetica",20), bg="white")
    welcome_label.place(x=450,y=0)
    login_frame = Frame(frame,bg="#f4f4f5",height=400,width=400)
    login_frame.place(x=550,y=60)
    login_label = Label(login_frame,text="Login",fg="#0669db", font=("Helvetica",20),bg="white")
    login_label.place(x=175,y=10)
    username_label = Label(login_frame,text="Username:",font=("Helvetica",15),bg="#f4f4f5")
    username_label.place(x=50, y=105)
    username_txt = Entry(login_frame)
    username_txt.place(x=170, y=105)
    password_label = Label(login_frame,text="Password:",font=("Helvetica",15),bg="#f4f4f5")
    password_label.place(x=50, y=170)
    password_txt = Entry(login_frame,show="*")
    password_txt.place(x=170, y=170)
    login_btn = Button(login_frame,text="Login",bg= "#0c6cb4")
    login_btn.place(x=200, y=225)
    Signup_label = Label(login_frame,text="Create an account:",font=("Helvetica",13),fg="black",bg="#f4f4f5")
    Signup_label.place(x=50, y=300)
    Signup_button = Button(login_frame,text="Sign up",bg="#f4f4f5",command=lambda:signup_call(login_frame))
    Signup_button.place(x=220, y=295)

def signup(window):
    frame =Frame(window, height=1000,width=1000,bg="white")
    frame.place(x=0,y=0)
    def signup_frame(frame):
        frame_frame = Frame(frame,height=1000,width=500)
        frame_frame.place(x=300,y=5)
        signup_lbl = Label(frame_frame,text="Signup",font=("Helvetica",20), fg="#ED2939")
        signup_lbl.place(x=180,y=5)
        name_lbl = Label(frame_frame, text="Name:",font=("Helvetica",15))
        name_lbl.place(x=50,y=40)
        name_txt = Entry(frame_frame)
        name_txt.place(x=170,y=40)        
        numb_lbl = Label(frame_frame, text="Number:",font=("Helvetica",15))
        numb_lbl.place(x=50,y=80)
        numb_txt = Entry(frame_frame)
        numb_txt.place(x=170,y=80)
        username_lbl = Label(frame_frame, text="Username:",font=("Helvetica",15))
        username_lbl.place(x=50,y=120)
        username_txt = Entry(frame_frame)
        username_txt.place(x=170,y=120)
        mail_lbl = Label(frame_frame, text="Mail:",font=("Helvetica",15))
        mail_lbl.place(x=50,y=160)
        mail_txt = Entry(frame_frame)
        mail_txt.place(x=170,y=160)
        password_lbl = Label(frame_frame, text="Password:",font=("Helvetica",15))
        password_lbl.place(x=50,y=200)
        password_txt = Entry(frame_frame, show="*")
        password_txt.place(x=170,y=200)
        conform_password_lbl = Label(frame_frame, text="Conform Password:",font=("Helvetica",15))
        conform_password_lbl.place(x=50,y=240)
        conform_password_txt = Entry(frame_frame, show="*")
        conform_password_txt.place(x=230,y=238)
        signup_btn = Button(frame_frame,text="Sign Up", bg="#007f00",command=lambda:create_new_account(name_txt,numb_txt,username_txt,mail_txt,password_txt,conform_password_txt))
        signup_btn.place(x=50,y=290)

    
    signup_frame(frame)

def create_new_account(*args):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor = cursor.execute(f"""
           insert into user (name,number,username,email,pass1,pass2)
            values("{args[0].get()}",{args[1].get()},"{args[2].get()}","{args[3].get()}","{args[4].get()}","{args[5].get()}");
            """)
    except Error as e:
        print(e)
  
    
    
def create_connection():
    path = './database/user_info.db'
    try:
        conn = sqlite3.connect(path)
        print("[ + ] Database Connection Successful")
        return conn
    except Error as e:
        print(e)
    
    
    


main_menu(frame)
main_windows.mainloop()

    
