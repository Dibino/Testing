from tkinter import *
app=Tk()
app.config(bg="#000000")



#=================================================entry====================================================#
entry =Entry(app,width=30,font=('Arial',30),relief=FLAT,fg="grey",bg="#080402")
entry.place(x=10,y=150)
#=============================================functions====================================================#









def standarad ():
    
    
    heading = Label(app,text="Standard",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#333334",activeforeground="lime",command=lambda:print('1'))
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#333334",fg="black",width=20,height=5,activebackground="#333334",activeforeground="lime",borderwidth=0)
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#333334",fg="black",width=20,height=5,activebackground="#333334",activeforeground="lime",borderwidth=0)
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#333334",fg="black",width=20,height=5,activebackground="#333334",activeforeground="lime",borderwidth=0)
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#333334",fg="black",width=20,height=5,activebackground="#333334",activeforeground="lime",borderwidth=0)
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#333334",fg="black",width=20,height=5,activebackground="#333334",activeforeground="lime",borderwidth=0)
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#333334",fg="black",width=20,height=5,activebackground="#333334",activeforeground="lime",borderwidth=0)
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#333334",fg="black",width=20,height=5,activebackground="#333334",activeforeground="lime",borderwidth=0)
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#333334",fg="black",width=20,height=5,activebackground="#333334",activeforeground="lime",borderwidth=0)
    nine.place(x=459,y=442)
    arith = Button(app,text="1/x",fg="black",bg="#1f1f1f",width=20,height=5,activebackground="#1f1f1f",activeforeground="lime",borderwidth=0)
    arith.place(x=5,y=442)
    square = Button(app,text="x^2",fg="black",bg="#1f1f1f",width=20,height=5,activebackground="#1f1f1f",activeforeground="lime",borderwidth=0)
    square.place(x=5,y=530)
    percentage = Button(app,text="%",fg="black",bg="#1f1f1f",width=20,height=5,activebackground="#1f1f1f",activeforeground="lime",borderwidth=0)
    percentage.place(x=5,y=617)
    zero = Button(app,text="0",bg="#1f1f1f",fg="black",width=20,height=5,activebackground="#1f1f1f",activeforeground="lime",borderwidth=0)
    zero.place(x=308,y=354)
    cancel = Button(app,text="C",fg="black",bg="#1f1f1f",width=20,height=5,activebackground="#1f1f1f",activeforeground="lime",borderwidth=0)
    cancel.place(x=5,y=354)
    Del = Button(app,text="del",fg="black",bg="#1f1f1f",width=20,height=5,activebackground="#1f1f1f",activeforeground="lime",borderwidth=0)
    Del.place(x=156,y=354)
    multiplication = Button(app,text="X",fg="black",bg="#1f1f1f",width=20,activebackground="#1f1f1f",activeforeground="lime",height=5,borderwidth=0)
    multiplication.place(x=459,y=354)
    addition = Button(app,text="+",fg="black",bg="#1f1f1f",width=20,height=5,activebackground="#1f1f1f",activeforeground="lime",borderwidth=0)
    addition.place(x=610,y=530)
    subtraction = Button(app,text="-",fg="black",bg="#1f1f1f",width=20,height=5,activebackground="#1f1f1f",activeforeground="lime",borderwidth=0)
    subtraction.place(x=610,y=442)
    division = Button(app,text="/",fg="black",bg="#1f1f1f",width=20,height=5,activebackground="#1f1f1f",activeforeground="lime",borderwidth=0)
    division.place(x=610,y=354)
    equal_to = Button(app,text="=",fg="black",bg="#1f1f1f",width=20,height=5,activebackground="#1f1f1f",activeforeground="lime",borderwidth=0)
    equal_to.place(x=610,y=617)
    
    
    
    
    
def scientific ():
    heading = Label(app,text="scientific",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    
    one = Button(app,text="1",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    Tan = Button(app,text="tan",fg="black",bg="#333334",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Tan.place(x=5,y=442)
    Sine = Button(app,text="sine",fg="black",bg="#333334",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Sine.place(x=5,y=530)
    Cos = Button(app,text="cos",fg="black",bg="#333334",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Cos.place(x=5,y=617)
    zero = Button(app,text="0",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    cancel = Button(app,text="C",fg="black",bg="#333334",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    cancel.place(x=5,y=354)
    Del = Button(app,text="del",fg="black",bg="#333334",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    multiplication = Button(app,text="sinh",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    multiplication.place(x=459,y=354)
    addition = Button(app,text="cosh",fg="black",bg="#333334",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    addition.place(x=610,y=530)
    subtraction = Button(app,text="log",fg="black",bg="#333334",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    subtraction.place(x=610,y=442)
    division = Button(app,text="exp",fg="black",bg="#333334",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    division.place(x=610,y=354)
    Tanh = Button(app,text="tanh",fg="black",bg="#333334",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Tanh.place(x=610,y=617)
    
    
    
    
    
 
 
 
def currency ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="Currency",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#333334",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    
    point = Button(app,text=".",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    
    Del = Button(app,text="del",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
  
    
def volume ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="volume   ",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    
    point = Button(app,text=".",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    
    Del = Button(app,text="del",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
   
    
       
    
def lenth ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="lenth     ",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    
    point = Button(app,text=".",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    
    Del = Button(app,text="del",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
   
       
def weight_and_mass ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="weight and mass",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#333334",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    
    point = Button(app,text=".",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    
    Del = Button(app,text="del",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
   
def temperature ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="temperature          ",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    
    point = Button(app,text=".",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    
    Del = Button(app,text="del",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
    


def energy ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="energy           ",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#333334",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    
    point = Button(app,text=".",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    
    Del = Button(app,text="del",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
  


def Area ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="Area              ",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#333334",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    
    point = Button(app,text=".",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    
    Del = Button(app,text="del",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
   



def speed ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="speed               ",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="white",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="white",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="white",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="white",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="white",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="white",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="white",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="white",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="white",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    
    point = Button(app,text=".",bg="white",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="white",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    
    Del = Button(app,text="del",bg="white",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
   


def Time ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="Time           ",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    point = Button(app,text=".",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    Del = Button(app,text="del",bg="#1f1f1f",fg="red",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
  

def power ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="power           ",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    point = Button(app,text=".",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    Del = Button(app,text="del",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
    
def newton ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="newton            ",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#333334",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    point = Button(app,text=".",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    Del = Button(app,text="del",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
   




def Data ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="Data               ",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#333334",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    point = Button(app,text=".",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    Del = Button(app,text="del",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
   


def pressure ():
    close = Label(app,text=" "*8,font=('popins',25),bg="#000000",height=14,width=40)
    close.place(x=0,y=354)
    heading = Label(app,text="pressure           ",font=('popins',25),fg="grey",bg="#000000")
    heading.place(x=0,y=0)
    one = Button(app,text="1",bg="#333334",fg="black",width=20,height=5,borderwidth=0,command=lambda:print('1'),activebackground="#1f1f1f",activeforeground="lime")
    one.place(x=156,y=617)
    two = Button(app,text="2",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    two.place(x=308,y=617)
    three = Button(app,text="3",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    three.place(x=459,y=617)
    four = Button(app,text="4",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    four.place(x=156,y=530)
    five = Button(app,text="5",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    five.place(x=308,y=530)
    six = Button(app,text="6",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    six.place(x=459,y=530)
    seven = Button(app,text="7",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    seven.place(x=156,y=442)
    eight = Button(app,text="8",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    eight.place(x=308,y=442)
    nine = Button(app,text="9",bg="#1f1f1f",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    nine.place(x=459,y=442)
    point = Button(app,text=".",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    point.place(x=5,y=617)
    zero = Button(app,text="0",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    zero.place(x=308,y=354)
    Del = Button(app,text="del",bg="#333334",fg="black",width=20,height=5,borderwidth=0,activebackground="#1f1f1f",activeforeground="lime")
    Del.place(x=156,y=354)
    
    
   


def About ():
    about = Label(app,text='''The executive governor,Bauchi  state Government,
Area  5 , Jarma Quarters.

	
Layin Burtsatse,
Matsango Azare,
Bauchi state.
 July 11, 2020.

Dear sir.
Letter of complaint
I hereby write on behalf of the community ofMatsangoAzare
to forward our complain on the bad road that threatensour 
community.Road is among the social aminities that people 
enjoy, it is one of the best mean of transportation which
without there would be hardship in daily conveyance0fgood
and it is very important especially in our area. Sir,with 
bad road networking, many problems occur such as accident 
which causes fatal injuries and in most of the timeslives
are lost and in ability to ride vehicles in night, etcOur
road has many patholes which cause the problems mentioned 
above. Sir we have been experiencing such in almost daily
basis. However, the Matsango people are committed to 
development of the state and they hadimmenselycontributed
for the victory of this government during electionandthey
would continue to support her. We would besogratefulifour
complain is considered.
,
Yours faithfully	
Abubakar Abdullahi 
ABUBAKAR ABDULLAHI.	
''',bg='black',fg='white')
    about.place(x=-20,y=0)

    
    
    
     
    







def abba ():
    llbl2 =Label(app,text='''

'''*104,bg="#333334",fg="red",font =('arial'),height=75,borderwidth=0)
    llbl2.place(x=1115,y=0)

    first_label=Label(app,bg='#333334',text='''
                                                                                 '''*128)
    first_label.place(x=1120,y=36)

      
    
   
    
    
    
    standard_button = Button(app,text="      Standard                   ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=standarad)
    standard_button.place(x=1120,y=38)
    Scientific_button = Button(app,text="      Scientific                   ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=scientific)
    Scientific_button.place(x=1120,y=76)
    currency_button = Button(app,text="      currency                    ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=currency)
    currency_button.place(x=1120,y=114)
    volume_button = Button(app,text="      volume                          ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=volume)
    volume_button.place(x=1120,y=152)
    lenth_button = Button(app,text="      lenth                          ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=lenth)
    lenth_button.place(x=1120,y=190)
    weight_and_mass_button = Button(app,text="      weight and mass                 ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=weight_and_mass)
    weight_and_mass_button.place(x=1120,y=228)
    temperature_button = Button(app,text="      temperature                    ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=temperature)
    temperature_button.place(x=1120,y=266)
    energy_button = Button(app,text="      energy                         ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=energy)
    energy_button.place(x=1120,y=304)
    Area_button = Button(app,text="      Area                          ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=Area)
    Area_button.place(x=1120,y=342)
    speed_button = Button(app,text="      speed                         ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=speed)
    speed_button.place(x=1120,y=380)
    Time_button = Button(app,text="      Time                                 ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=Time)
    Time_button.place(x=1120,y=418)
    power_button = Button(app,text="      power                            ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=power)
    power_button.place(x=1120,y=456)
    Data_button = Button(app,text="      Data                                ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=Data)
    Data_button.place(x=1120,y=494)
    pressure_button = Button(app,text="      pressure                         ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=pressure)
    pressure_button.place(x=1120,y=532)
    Newton_button = Button(app,text="      Newton                         ",bg="black",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0,command=newton)
    Newton_button.place(x=1120,y=570)
    About_button = Button(app,text="      About                        ",bg="#080402",fg="grey",activebackground="black",activeforeground="blue",font=('Arial',15),borderwidth=0)
    About_button.place(x=1120,y=608)
    
    
  









    
    
#=========================================================================labels================================================================#


heading2 = Button(app,text=" III      Calculators           ",font=('Arial',16,'bold'),fg="grey",bg="black",activebackground="black",activeforeground="blue",borderwidth=0,command=abba)
heading2.place(x=1120,y=-2)


   






app.mainloop()