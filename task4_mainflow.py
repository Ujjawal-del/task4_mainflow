from tkinter import *
from PIL import ImageTk,Image

def init_calculator():
    root = Tk()
    root.geometry("300x430+0+0")
    root.resizable(False,False)
    root.title("calculator")

    root.iconbitmap("Calc-icon.ico")

    bg_image = ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\300x430_background.png")
    bg_label = Label(root,image=bg_image).place(x=0,y=0)

    input_user = Entry(root,width=35,bd=12,relief=SUNKEN,borderwidth=5,font=("times new roman",10))
    input_user.grid(row=0,column=0,padx=15,pady=20,columnspan=4)

    def button_click(number):
        current_num = input_user.get()
        input_user.delete(0,END)
        input_user.insert(0,str(current_num) + str(number))
        #print(current_num)

    def add_num():
        first_num = input_user.get()
        global f_num
        global maths
        maths = "addition"
        f_num = int(first_num)
        input_user.delete(0,END)

    def sub_num():
        first_num = input_user.get()
        global f_num
        global maths
        maths = "subtraction"
        f_num = int(first_num)
        input_user.delete(0,END)

    def div_num():
        first_num = input_user.get()
        global f_num
        global maths
        maths = "divide"
        f_num = int(first_num)
        input_user.delete(0,END)

    def mul_num():
        first_num = input_user.get()
        global f_num
        global maths
        maths = "multiply"
        f_num = int(first_num)
        input_user.delete(0,END)

    def clr_num():
        input_user.delete(0,END)

    def equ_num():
        second_num = input_user.get()
        input_user.delete(0,END)

        if (maths == "addition"):
            input_user.insert(0,f_num + int(second_num))
        elif(maths == "subtraction"):
            input_user.insert(0,f_num - int(second_num))
        elif(maths == "divide"):
            input_user.insert(0,f_num / int(second_num))
        elif(maths == "multiply"):
            input_user.insert(0,f_num * int(second_num))

    num_images = {
        "1":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\1.png"),
        "2":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\2.png"),
        "3":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\3.png"),
        "4":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\4.png"),
        "5":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\5.png"),
        "6":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\6.png"),
        "7":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\7.png"),
        "8":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\8.png"),
        "9":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\9.png"),
        "0":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\10.png"),
        "+":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\11.png"),
        "-":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\12.png"),
        "/":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\14.png"),
        "*":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\13.png"),
        "c":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\16.png"),
        "=":ImageTk.PhotoImage(file="C:\\Users\\91995\\Downloads\\15.png"),
    }

    buttons = {
        "1":(1,0,lambda:button_click(1)),
        "2":(1,1,lambda:button_click(2)),
        "3":(1,2,lambda:button_click(3)),
        "4":(2,0,lambda:button_click(4)),
        "5":(2,1,lambda:button_click(5)),
        "6":(2,2,lambda:button_click(6)),
        "7":(3,0,lambda:button_click(7)),
        "8":(3,1,lambda:button_click(8)),
        "9":(3,2,lambda:button_click(9)),
        "0":(4,1,lambda:button_click(0)),
        "+":(4,0,add_num),
        "-":(4,2,sub_num),
        "/":(5,0,div_num),
        "*":(5,1,mul_num),
        "c":(6,1,clr_num),
        "=":(5,2,equ_num),
    }   

    for btn,(row,col,cmd) in buttons.items():
        Button(root,image=num_images[btn],command=cmd).grid(row=row,column=col,padx=20,pady=1)

    root.mainloop()

init_calculator()