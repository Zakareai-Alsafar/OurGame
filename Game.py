import tkinter
from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
from random import randint
ActivePlayer=1 #set active player
p1=[] #what player 1 selected
p2=[] #what player 2 selected
root=Tk()
root.title("اللاعب الاول")
style=ttk.Style()
style.theme_use('clam') # (aqua,clam,alt,default,classic)

Ximgpath = PhotoImage(file="x.png")
XImg=Ximgpath.subsample(10,10)
Oimgpath = PhotoImage(file="O.png")
OImg=Oimgpath.subsample(10,10)

def SetLayout(id,txt):
    if(id==1):
        if (txt == 'X'):
            btn1.config(image=XImg, compound='center')
        else:
            btn1.config(image=OImg, compound='center')
        btn1.state(['disabled'])
    else:
            if (id == 2):
                if(txt=='X'):
                    btn2.config(image=XImg,compound='center')
                else:
                    btn2.config(image=OImg,compound='center')
                #btn2.config(text=txt)
                btn2.state(['disabled'])
            else:
                if (id == 3):
                    if (txt == 'X'):
                        btn3.config(image=XImg, compound='center')
                    else:
                        btn3.config(image=OImg, compound='center')
                    btn3.state(['disabled'])
                else:
                    if (id == 4):
                        if (txt == 'X'):
                            btn4.config(image=XImg, compound='center')
                        else:
                            btn4.config(image=OImg, compound='center')
                        btn4.state(['disabled'])
                    else:
                       if (id == 5):
                           if (txt == 'X'):
                               btn5.config(image=XImg, compound='center')
                           else:
                               btn5.config(image=OImg, compound='center')
                           btn5.state(['disabled'])
                       else:
                            if (id == 6):
                                if (txt == 'X'):
                                    btn6.config(image=XImg, compound='center')
                                else:
                                    btn6.config(image=OImg, compound='center')
                                btn6.state(['disabled'])
                            else:
                                if (id == 7):
                                    if (txt == 'X'):
                                        btn7.config(image=XImg, compound='center')
                                    else:
                                        btn7.config(image=OImg, compound='center')
                                    btn7.state(['disabled'])
                                else:
                                    if (id == 8):
                                        if (txt == 'X'):
                                            btn8.config(image=XImg, compound='center')
                                        else:
                                            btn8.config(image=OImg, compound='center')
                                        btn8.state(['disabled'])
                                    else:
                                        if (id == 9):
                                            if (txt == 'X'):
                                                btn9.config(image=XImg, compound='center')
                                            else:
                                                btn9.config(image=OImg, compound='center')
                                            btn9.state(['disabled'])

def btnClick(id):
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        SetLayout(id,'X')
        p1.append(id)
        root.title(" اللاعب الثاني")
        ActivePlayer=2
        #print('p1:{}'.format(p1))
    else:
        if(ActivePlayer==2):
            SetLayout(id,'O')
            p2.append(id)
            root.title(" اللاعب الاول")
            ActivePlayer=1

            #print('p1:{}'.format(p2))
    CheekWiner()
def CheekWiner():
    winer=-1
    if(       (1 in p1 and 2 in p1 and 3 in p1) or (4 in p1 and 5 in p1 and 6 in p1) or (7 in p1 and 8 in p1 and 9 in p1)
            or(1 in p1 and 4 in p1 and 7 in p1) or (2 in p1 and 5 in p1 and 8 in p1) or (3 in p1 and 6 in p1 and 9 in p1)
            or(1 in p1 and 5 in p1 and 9 in p1) or (3 in p1 and 5 in p1 and 7 in p1)):
        winer=1
        print(1)
    elif(   (1 in p2 and 2 in p2 and 3 in p2) or (4 in p2 and 5 in p2 and 6 in p2) or (7 in p2 and 8 in p2 and 9 in p2)
         or (1 in p2 and 4 in p2 and 7 in p2) or (2 in p2 and 5 in p2 and 8 in p2) or (3 in p2 and 6 in p2 and 9 in p2)
         or (1 in p2 and 5 in p2 and 9 in p2) or (3 in p2 and 5 in p2 and 7 in p2)):
        winer=2
        print(2)

    if winer==1:
        messagebox.showinfo(title='Cong',message='الاعب الاول فاز')
        exit()
    elif winer==2:
        messagebox.showinfo(title='Cong', message='الاعب الثاني فاز')
        exit()
    elif len(p1)==5 :
        messagebox.showinfo(title='Cong', message='تعادل حبيبي')
        exit()


#Buuon 1
btn1=ttk.Button(root,text=' ')
btn1.grid(row=0,column=0,sticky='snew',ipadx=20,ipady=40)
btn1.config(command=lambda :btnClick(1))
#btn1.config(image=resizeImg,compound='left')

#Buuon 2
btn2=ttk.Button(root,text=' ')
btn2.grid(row=0,column=1,sticky='snew',ipadx=10,ipady=40)
btn2.config(command=lambda :btnClick(2))
#Buuon 3
btn3=ttk.Button(root,text=' ')
btn3.grid(row=0,column=2,sticky='snew',ipadx=10,ipady=40)
btn3.config(command=lambda :btnClick(3))
#Buuon 4
btn4=ttk.Button(root,text=' ')
btn4.grid(row=1,column=0,sticky='snew',ipadx=10,ipady=40)
btn4.config(command=lambda :btnClick(4))
#Buuon 5
btn5=ttk.Button(root,text=' ')
btn5.grid(row=1,column=1,sticky='snew',ipadx=10,ipady=40)
btn5.config(command=lambda :btnClick(5))
#Buuon 6
btn6=ttk.Button(root,text=' ')
btn6.grid(row=1,column=2,sticky='snew',ipadx=10,ipady=40)
btn6.config(command=lambda :btnClick(6))
#Buuon 7
btn7=ttk.Button(root,text=' ')
btn7.grid(row=2,column=0,sticky='snew',ipadx=10,ipady=40)
btn7.config(command=lambda :btnClick(7))
#Buuon 8
btn8=ttk.Button(root,text=' ')
btn8.grid(row=2,column=1,sticky='snew',ipadx=10,ipady=40)
btn8.config(command=lambda :btnClick(8))
#Buuon 9
btn9=ttk.Button(root,text=' ')
btn9.grid(row=2,column=2,sticky='snew',ipadx=10,ipady=40)
btn9.config(command=lambda :btnClick(9))

root.mainloop()