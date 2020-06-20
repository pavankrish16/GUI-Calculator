''' a²
√
1/x

These are the specials symbols used in the calculator.

This programs intialises the calculator at res function(line46) by opening standar calculator
'''

#import tkinter as tk
from tkinter import  *
from math import *

font_entry="-family {Microsoft Sans Serif} -size 30 "\
" -slant roman -underline 0 -overstrike 0"
font_label="-family {Microsoft Sans Serif} -size 10 "\
" -slant roman -underline 0 -overstrike 0"
font12 = "-family {Segoe UI} -size 16 -weight normal -slant "  \
"roman -underline 0 -overstrike 0"
font13 = "-family {Segoe UI} -size 16 -slant "  \
"roman -underline 0 -overstrike 0"

side_btns={ "activebackground":"#d9d9d9", "activeforeground":"#000000", "background":"#f0f0f0", "borderwidth":"0", "disabledforeground":"#a3a3a3", "font":font12, "foreground":"#000000", "highlightbackground":"#d9d9d9", "highlightcolor":"black", "pady":"0",}
center_btns=side_btns.copy()
center_btns.update({"background":"#ffffff","font":font13})

#Creating a fake window
x=Tk()
x.withdraw()

#Creating window for Normal Calculator
wind=Toplevel(x)
wind.geometry("470x605")
wind.resizable(0,0)
icon=PhotoImage(file=r"calcy.png")      #Used to load Images.
wind.iconphoto(False,icon)
wind.title("Krishna's Advanced GUI Calculator")

#Creating window for Sceintific Calculator
wind1=Toplevel(x)
wind1.geometry("470x629")
wind1.resizable(0,0)
wind1.title("Krishna's Advanced GUI Calculator")
wind1.withdraw()

def res(x):         #Used to toggle b/w Standard & Sceientifc Calculator.
    if(x=='N'):
        wind1.withdraw()    #Used to hide current window
        wind.deiconify()    #Used to Open Hidden window
    else:
        wind1.deiconify()
        wind.withdraw()
        menu_bar(wind1)         #Intialsing menu bar
        obj1=sceintific(wind1)  #Creating an instance of Sceintific Calculator.    

    
def menu_bar(screen):
    menubar=Menu(screen,font=font_label,background="#000000",foreground="#000000",borderwidth="0",disabledforeground="#000000")
    filemenu=Menu(menubar,tearoff=0,font=font_label)
    filemenu.add_command(label="Standard",command=lambda:res('N'))      #Adding Menubar Options.
    filemenu.add_command(label="Sceintific",command=lambda:res('S'))
    filemenu.add_separator()
    menubar.add_cascade(label="FILE",menu=filemenu)
    screen.config(menu=menubar)

class normal:
    def __init__(self,wind):
        self.win=wind
        self.inp_entry=StringVar()      #Used to update Entry Box Value.
        self.inp=StringVar()
        self.inp_label=Label(self.win,background="#e6e6e6",foreground="#000000",borderwidth="0",disabledforeground="#a3a3a3",font=font_label,justify=RIGHT,textvariable=self.inp,anchor=E)
        self.inp_label.place(x=0,y=0,height=50,width=470)
        self.inp_field=Entry(self.win,background="#e6e6e6",foreground="#000000",borderwidth="0",disabledforeground="#a3a3a3",font=font_entry,justify=RIGHT,insertbackground="black",textvariable=self.inp_entry)
        self.inp_field.place(x=0,y=50,height=130,width=470)

        self.del_pic=PhotoImage(file=r"del.png")
        self.plmi_pic=PhotoImage(file=r"plmi.png")
        
        #ROW 1
        bt_mod=Button(wind,text='%',command=lambda:self.btn('%'),**side_btns)
        bt_ce=Button(wind,text='CE',command=lambda:self.btn('ce'),**side_btns)
        bt_c=Button(wind,text='C',command=lambda:self.btn('c'),**side_btns)
        bt_del=Button(wind,image=self.del_pic,command=lambda:self.btn('X'),**side_btns)
        
        #ROW 2
        bt_inverse=Button(wind,text='1/x',command=lambda:self.btn('**-1'),**side_btns)
        bt_square=Button(wind,text='x²',command=lambda:self.btn('**2'),**side_btns)
        bt_root=Button(wind,text='√',command=lambda:self.btn('**0.5'),**side_btns)
        bt_div=Button(wind,text='/',command=lambda:self.btn('/'),**side_btns)

        #ROW 3
        bt7=Button(wind,text='7',command=lambda:self.btn('7'),**center_btns)
        bt8=Button(wind,text='8',command=lambda:self.btn('8'),**center_btns)
        bt9=Button(wind,text='9',command=lambda:self.btn('9'),**center_btns)
        bt_mul=Button(wind,text='*',command=lambda:self.btn('*'),**side_btns)
        
        #ROW 4
        bt4=Button(wind,text='4',command=lambda:self.btn('4'),**center_btns)
        bt5=Button(wind,text='5',command=lambda:self.btn('5'),**center_btns)
        bt6=Button(wind,text='6',command=lambda:self.btn('6'),**center_btns)
        bt_minus=Button(wind,text='-',command=lambda:self.btn('-'),**side_btns)

        #ROW 5
        bt1=Button(wind,text='1',command=lambda:self.btn('1'),**center_btns)
        bt2=Button(wind,text='2',command=lambda:self.btn('2'),**center_btns)
        bt_root=Button(wind,text='3',command=lambda:self.btn('3'),**center_btns)
        bt_plus=Button(wind,text='+',command=lambda:self.btn('+'),**side_btns)

        #ROW 6
        bt_plmi=Button(wind,image=self.plmi_pic,command=lambda:self.btn('+-'),**center_btns)
        bt0=Button(wind,text='0',command=lambda:self.btn('0'),**center_btns)
        bt_dot=Button(wind,text='.',command=lambda:self.btn('.'),**center_btns)
        bt_equ=Button(wind,text='=',command=lambda:self.btn('='),activebackground="#ADD8E6", activeforeground="#000000", background="#ADD8E6", borderwidth="0", disabledforeground="#ADD8E6", font=font12, foreground="#000000", highlightbackground="#ADD8E6", highlightcolor="black", pady="0")

        
        #Placing Button in their respective positions
        self.pos=[(1,181),(118,181),(235,181),(352,181),(1,252),(118,252),(235,252),(352,252),(1,323),(118,323),(235,323),(352,323),(1,394),(118,394),(235,394),(352,394),(1,465),(118,465),(235,465),(352,465),(1,536),(118,536),(235,536),(352,536)]
        self.lis=self.win.winfo_children()[3:]      #to store variable names in list
        self.place_btns(0)
        
        #print(len(self.pos))
        self.exp=''

    #Arraging Buttons
    def place_btns(self,i):
        if(i==len(self.pos)):
            return
        else:
            self.lis[i].place(x=self.pos[i][0],y=self.pos[i][1],height=70,width=116)
            self.place_btns(i+1)
            self.temp=''
                
    #Defining Buttons and User Input
    def btn(self,x):
        self.x=x
        c=0
        ops='*+/-'
        spc_ops=[]
        if(self.exp!='' and self.exp[-1] in ops and x in ops):
            self.exp=self.exp[:-1]
            self.exp+=x
            self.inp.set(self.exp)
        elif(self.x=='='):
            if(self.exp==''):
                self.exp=self.inp_entry.get()
            self.inp.set(self.exp)
            ans=str(eval(self.exp))
            self.inp_entry.set(ans)
            self.temp=''
        elif(x=='X'):
            X=self.inp_entry.get()
            self.inp_entry.set(X[:-1])
        elif(x=='c' or x=='ce'):
            self.inp_entry.set("")
            self.exp=""
            self.inp.set("")
        elif(x in ops):
            self.inp.set(self.exp+x)
            ans=str(eval(self.exp))
            self.inp_entry.set(ans)
            self.exp+=x
            self.temp=''
        else:
            self.exp+=x
            self.temp+=x
            self.inp_entry.set(self.temp)

menu_bar(wind)
obj=normal(wind)

class sceintific():
    def __init__(self,wind1):
        self.win=wind1
        self.win.iconphoto(False,icon)
        self.inp_entry=StringVar()
        self.inp=StringVar()
        self.inp_label=Label(self.win,background="#e6e6e6",foreground="#000000",borderwidth="0",disabledforeground="#a3a3a3",font=font_label,justify=RIGHT,textvariable=self.inp,anchor=E)
        self.inp_label.place(x=0,y=0,height=50,width=470)
        self.inp_field=Entry(self.win,background="#e6e6e6",foreground="#000000",borderwidth="0",disabledforeground="#a3a3a3",font=font_entry,justify=RIGHT,insertbackground="black",textvariable=self.inp_entry)
        self.inp_field.place(x=0,y=50,height=130,width=470)

        self.del_pic=PhotoImage(file=r"del.png")
        self.plmi_pic=PhotoImage(file=r"plmi.png")
        self.tp_pic=PhotoImage(file=r"superscript.png")
        self.pi=PhotoImage(file=r"pi.png")
        self.cube=PhotoImage(file=r"xcube.png")
        self.xysupscript=PhotoImage(file=r"xysuperscript.png")
        
        #ROW 1
        bt_tp=Button(wind1,text='2ª',command=lambda:self.btn('2x'),**side_btns)
        bt_pi=Button(wind1,image=self.pi,command=lambda:self.btn('3.14'),**side_btns)
        #bt_pi.place(x=0,y=188,height=50,width=63)
        bt_e=Button(wind1,text='e',command=lambda:self.btn('2.7182818284590452353602874713527'),**side_btns)
        bt_c=Button(wind1,text='C',command=lambda:self.btn('c'),**side_btns)
        bt_del=Button(wind1,image=self.del_pic,command=lambda:self.btn('X'),**side_btns)
        
        #ROW 2
        bt_squ=Button(wind1,text='x²',command=lambda:self.btn('**2'),**side_btns)
        bt_inverse=Button(wind1,text='1/x',command=lambda:self.btn('**-1'),**side_btns)
        bt_abs=Button(wind1,text='|x|',command=lambda:self.btn('abs'),**side_btns)
        bt_root=Button(wind1,text='√',command=lambda:self.btn('**0.5'),**side_btns)
        bt_mod=Button(wind1,text='%',command=lambda:self.btn('%'),**side_btns)

        #ROW 3
        bt_cube=Button(wind1,text='x³',command=lambda:self.btn('x3'),**side_btns)
        bt_opnbrc=Button(wind1,text='(',command=lambda:self.btn('('),**side_btns)
        bt_clsbrc=Button(wind1,text=')',command=lambda:self.btn(')'),**side_btns)
        bt_fac=Button(wind1,text='x!',command=lambda:self.btn('!'),**side_btns)
        bt_div=Button(wind1,text='/',command=lambda:self.btn('/'),**side_btns)
     
        #ROW 4
        bt_xy=Button(wind1,text='aᵇ',command=lambda:self.btn('**'),**side_btns)
        bt7=Button(wind1,text='7',command=lambda:self.btn('7'),**center_btns)
        bt8=Button(wind1,text='8',command=lambda:self.btn('8'),**center_btns)
        bt9=Button(wind1,text='9',command=lambda:self.btn('9'),**center_btns)
        bt_mul=Button(wind1,text='*',command=lambda:self.btn('*'),**side_btns)

        #ROW 5
        bt_10x=Button(wind1,text='10ª',command=lambda:self.btn('10x'),**side_btns)
        bt4=Button(wind1,text='4',command=lambda:self.btn('4'),**center_btns)
        bt5=Button(wind1,text='5',command=lambda:self.btn('5'),**center_btns)
        bt6=Button(wind1,text='6',command=lambda:self.btn('6'),**center_btns) 
        bt_minus=Button(wind1,text='-',command=lambda:self.btn('-'),**side_btns)

        #ROW 6
        bt_log=Button(wind1,text='log',command=lambda:self.btn('log'),**side_btns)
        bt1=Button(wind1,text='1',command=lambda:self.btn('1'),**center_btns)
        bt2=Button(wind1,text='2',command=lambda:self.btn('2'),**center_btns)
        bt3=Button(wind1,text='3',command=lambda:self.btn('3'),**center_btns)
        bt_plus=Button(wind1,text='+',command=lambda:self.btn('+'),**side_btns)

        #ROW 7
        bt_ln=Button(wind1,text='ln',command=lambda:self.btn('ln'),**side_btns)
        bt_plmi=Button(wind1,image=self.plmi_pic,command=lambda:self.btn('+-'),**center_btns)
        bt0=Button(wind1,text='0',command=lambda:self.btn('0'),**center_btns)
        bt_dot=Button(wind1,text='.',command=lambda:self.btn('.'),**center_btns)
        bt_equ=Button(wind1,text='=',command=lambda:self.btn('='),activebackground="#ADD8E6", activeforeground="#000000", background="#ADD8E6", borderwidth="0", disabledforeground="#ADD8E6", font=font12, foreground="#000000", highlightbackground="#ADD8E6", highlightcolor="black", pady="0")


        #Placing Button in their respective positions
        self.pos=[(1,181),(95,181),(189,181),(283,181),(376,181),(1,242),(95,242),(189,242),(283,242),(376,242),(1,303),(95,303),(189,303),(283,303),(376,303),(1,364),(95,364),(189,364),(283,364),(376,364),(1,425),(95,425),(189,425),(283,425),(376,425),(1,486),(95,486),(189,486),(283,486),(376,486),(1,547),(95,547),(189,547),(283,547),(376,547)]
        self.lis=self.win.winfo_children()[3:]      #to store variable names in list
        self.place_btns(0)
        #print(len(self.pos))
        self.exp=''
        self.temp=''

    #Arranging Buttons
    def place_btns(self,i):
        if(i==len(self.pos)):
            return
        else:
            self.lis[i].place(x=self.pos[i][0],y=self.pos[i][1],height=59,width=93) #Actual Height should be 60
            self.place_btns(i+1)

    #Defining Button Operations and User input
    def btn(self,x):
        self.x=x
        c=0
        ops='*+/-'
        if(self.exp!='' and self.exp[-1] in ops and x in ops):
            self.exp=self.exp[:-1]
            self.exp+=x
            self.inp.set(self.exp)
        elif(self.x=='='):
            if(self.exp==''):               #If user enters the input from keyboard then, we need to extract expression from entry widget.
                self.exp=self.inp_entry.get()
            self.inp.set(self.exp)
            ans=str(eval(self.exp))
            self.inp_entry.set(ans)
            self.temp=''
        elif(x=='X'):
            self.inp_entry.set(self.inp_entry.get()[:-1])           #Here we are taking input from entry widget and slicing it upto last element.
        elif(x=='c' or x=='ce'):
            self.inp_entry.set("")
            self.exp=""
            self.inp.set("")
            self.temp=''
        elif(x in ops):             #whenever user enter any operator(+,-...) it evaluates the expression upto then and displays in entry widget.
            self.inp.set(self.exp+x)
            ans=str(eval(self.exp))
            self.inp_entry.set(ans)
            self.exp+=x
            self.temp=''
        elif(x=='abs'):
            t=x+'('+self.temp+')'
            self.exp=self.exp[:-1]
            self.exp+=t
            self.inp_entry.set(eval(self.exp))
            self.temp=''
            self.inp.set(self.exp)
        elif(x=='!'):
            t=factorial(int(self.temp))
            self.exp=self.exp[:-1]
            self.exp+=str(t)
            self.inp.set(self.exp)
            self.inp_entry.set(str(eval(self.exp)))
            self.temp=''
        elif(x=='10x' or x=='2x'):
            if(x=='10x'):
                x=10
            else:
                x=2
            t=x**int(self.temp)
            self.exp=self.exp[:-1]
            self.exp+=str(t)
            self.inp_entry.set(str(eval(self.exp)))
            self.temp=''
            self.inp.set(self.exp)
        elif(x=='**'):
            self.exp+=self.temp+x
            self.temp=''
        elif(x=='log' or x=='ln'):
            if(x=='log'):
                t=10    
            else:
                t=2
            x=log(int(self.temp),t)
            self.temp=''
            self.exp=self.exp[:-1]
            self.exp+=str(x)
            self.inp.set(self.exp)
            self.inp_entry.set(str(eval(self.exp)))
        elif(x=='+-'):
            if(self.temp[0] not in '+-'):
                self.temp='-'+self.temp
        else:
            self.exp+=x
            self.temp+=x
            self.inp_entry.set(self.temp)
