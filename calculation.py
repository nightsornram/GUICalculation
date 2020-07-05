from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk()
GUI.title('โปรแกรมคำนวณ Beam')
GUI.geometry('500x500')
########################################

def Math_additional():
    GUI2 = Toplevel()
    GUI2.title("หน้าต่างคณิตศาสตร์")
    GUI2.geometry('500x400')

    def Add():
        messagebox.showinfo('การบวก','ตัวอย่าง : 1 + 1 = 2')

    B = ttk.Button(GUI2,text='ตัวอย่างการบวกเลข',command=Add).pack(ipadx=20,ipady=10)


    GUI2.mainloop()

########################################
menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label='Exit',command = GUI.quit)
menubar.add_cascade(label='File',menu=filemenu)

mathmenu = Menu(menubar,tearoff=0)
mathmenu.add_command(label='การบวก',command = Math_additional)
mathmenu.add_command(label='การลบ')
mathmenu.add_command(label='การคูณ')
mathmenu.add_command(label='การหาร')

menubar.add_cascade(label='คณิตศาสตร์',menu=mathmenu)
########################################

Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)
Tab.add(T1,text = 'Beam')
Tab.add(T2,text = 'Sphere')
Tab.add(T3,text = 'Cylinder')



#####################Tab1#######################
img_beam = PhotoImage(file='beam.png')
logo_beam = ttk.Label(T1,text ='Beam',image=img_beam)
logo_beam.pack()

F1 = Frame(T1)
F1.pack()

value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
FONT1 = ('TH Sarabun New',15,'bold')

############
E1 = ttk.Entry(F1,textvariable = value1)
E1.grid(column=1,row=0,pady=10)
L1 = ttk.Label(F1,text= '(1) ความกว้าง',font = FONT1)
L1.grid(column=0,row=0)
############
E2 = ttk.Entry(F1,textvariable = value2)
E2.grid(column=1,row=1,pady=10)
L2 = ttk.Label(F1,text= '(2) ความสูง',font = FONT1)
L2.grid(column=0,row=1)
############
E3 = ttk.Entry(F1,textvariable = value3)
E3.grid(column=1,row=2,pady=10)
L3 = ttk.Label(F1,text= '(3) ความยาว',font = FONT1)
L3.grid(column=0,row=2)

def Calc():
    v1 = float(value1.get())
    v2 = float(value2.get())
    v3 = float(value3.get())
    cal = v1 *v2 *v3
    textshow = f'คานคอนกรีตชิ้นนี้มีปริมาตร : {cal:,.2f} ลบ.ม'
    v_result.set(textshow)

B1 = ttk.Button(T1,text = 'Calculate',command = Calc)
B1.pack(ipadx=20,ipady=10,pady=10)

v_result =StringVar()
v_result.set('--------Result-------')
Result = ttk.Label(T1,textvariable =v_result,foreground = 'green',font =FONT1)
Result.pack()
#####################Tab1#######################


#####################Tab2#######################
img_sphere = PhotoImage(file='volumesphere.png')
logo1 = ttk.Label(T2,image=img_sphere)
logo1.pack()

F2 = Frame(T2)
F2.pack()

def Volumesphere():
    r = float(circle_value.get())
    cal = (4/3)*(22/7)*(r**3)
    textshow = f'รัศมีทรงกลมยาว{r}เมตร จะมีปริมาตร: {cal:,.2f} ลบ.ม'
    c_result.set(textshow)


circle_value = StringVar()
C1 = ttk.Entry(F2,textvariable = circle_value)
C1.grid(column=1,row=0,pady=10)
M1 = ttk.Label(F2,text= '(1) รัศมี : ',font = FONT1)
M1.grid(column=0,row=0)
B2 = ttk.Button(T2,text = 'Calculate',command = Volumesphere)
B2.pack(ipadx=20,ipady=10,pady=10)
c_result = StringVar()
c_result.set('--------Result-------')
Result1 = ttk.Label(T2,textvariable =c_result,foreground = 'green',font =FONT1)
Result1.pack()
#####################Tab2#######################

#####################Tab3#######################
img_cylinder = PhotoImage(file='vloumecylinder.png')
logo2 = ttk.Label(T3,image=img_cylinder)
logo2.pack()

F3 = Frame(T3)
F3.pack()

def Volumecylinder():
    r = float(cylinder_value.get())
    h = float(hight_valvue.get())
    cal = (22/7)*(r**2)*h
    textshow = f'ทรงกระบอกมีรัศมียาว{r}เมตร สูง{h}เมตร จะมีปริมาตร: {cal:,.2f} ลบ.ม'
    CY_result.set(textshow)


cylinder_value = StringVar()
hight_valvue = StringVar()
CY1 = ttk.Entry(F3,textvariable = cylinder_value)
CY1.grid(column=1,row=0,pady=10)
Ra1 = ttk.Label(F3,text= '(1) รัศมี : ',font = FONT1)
Ra1.grid(column=0,row=0)
CY2 = ttk.Entry(F3,textvariable = hight_valvue)
CY2.grid(column=1,row=1,pady=10)
Ra2 = ttk.Label(F3,text= '(2) ความสูง : ',font = FONT1)
Ra2.grid(column=0,row=1)
B3 = ttk.Button(T3,text = 'Calculate',command = Volumecylinder)
B3.pack(ipadx=20,ipady=10,pady=10)
CY_result = StringVar()
CY_result.set('--------Result-------')
Result2 = ttk.Label(T3,textvariable =CY_result,foreground = 'green',font =FONT1)
Result2.pack()
#####################Tab3#######################
GUI.mainloop()
