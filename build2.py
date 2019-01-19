from tkinter import *
import tkinter
#import Image,ImageTk
window=Tk()
window.title("Fitness Calulator")
Name=StringVar()
Age=IntVar()
Weight=DoubleVar()
Height=DoubleVar()
BPL=IntVar()
BPH=IntVar()
PsRate=IntVar()
RBC=DoubleVar()
WBC=IntVar()
Plate=IntVar()
HB=IntVar()
UA=DoubleVar()
Chol=IntVar()

"""background_image=window.PhotoImage("fit.jpg")
background_label = window.Label(parent, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)"""


#photo = PhotoImage(file = "")
#w = Label(root, image=photo)
#w.pack()




frame=Frame(window,)                     #windows,frame
frame.grid(row=0, column=10,sticky="N")
#label
#label.grid
#image=Image.open("fit.jpg")
#tkpi=ImageTk.PhotoImage("fit.jpg")
window.configure(background="yellow")  #Window theme
"""mb =  Menubutton ( window, text = "GF") 
mb.grid() 
mb.menu  =  Menu ( mb, tearoff = 0 ) 
mb["menu"]  =  mb.menu 
cVar  = IntVar() 
aVar = IntVar() 
mb.menu.add_command ( label ='Contact', variable = cVar ) 
mb.menu.add_command( label = 'About', variable = aVar ) 
mb.grid() """

menu = Menu(window) 
window.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=window.destroy) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 


lname=Label(window, text="Name", font="Helvetica" "16",bg="yellow")  #Name
lname.grid(row=1,column=1)
ename=Entry(window,cursor="arrow",textvariable=Name, bd=2)
ename.grid(row=1, column=2)

"""wage=Label(window,text="Age",font="Helvetica" "16",bg="yellow")
wage.grid(row=1,column=7)
w = Scale(window, from_=0, to=100,orient=HORIZONTAL) 
w.grid(row=1,column=9) """
 

lage=Label(window, text="Age", font="Helvetica" "16",bg="yellow") #Age
lage.grid(row=1,column=5)
eage=Entry(window, cursor="arrow",textvariable=Age, bd=2)
eage.grid(row=1, column=6)

Gender=Label(window,text="Gender",font="Helvetica" "16",bg="yellow") #gender
Gender.grid(row=2,column=1)
G1=Radiobutton(window,text="Male", cursor="dotbox", font="16",bg="yellow",value=1)
G2=Radiobutton(window,text="Female",cursor="dotbox",font="16",bg="yellow",value=2)
G1.grid(row=2,column=2)
G2.grid(row=2, column=6)

lweight=Label(window,text="Weight (kg)",font="Helvetica" "16",bg="yellow")   #weight
lweight.grid(row=3,column=1)
eweight=Entry(window,cursor="arrow",textvariable=Weight,bd=1.5)
eweight.grid(row=3,column=2)

lheight=Label(window,text="Height (cm)",font="Helvetica" "16",bg="yellow")  #height
lheight.grid(row=4,column=1)
eheight=Entry(window,cursor="arrow",textvariable=Height,bd=1.5)
eheight.grid(row=4,column=2)

lbpl=Label(window,text="BP Low (mm)",font="Helvetica" "16",bg="yellow") #Low_BloodPressure
lbpl.grid(row=5,column=1)
ebpl=Entry(window,cursor="arrow",textvariable=BPL,bd=1.5)
ebpl.grid(row=5,column=2)

lbph=Label(window,text="BP High (mm)",font="Helvetica" "16",bg="yellow") #High_BloodPressure
lbph.grid(row=6,column=1)
ebph=Entry(window,cursor="arrow",textvariable=BPH,bd=1.5)
ebph.grid(row=6,column=2)

lpulse=Label(window,text="Pulse Rate (bpm)",font="Helvetica" "16",bg="yellow") #PulseRate
lpulse.grid(row=7,column=1)
epulse=Entry(window,cursor="arrow",textvariable=PsRate,bd=1.5)
epulse.grid(row=7,column=2)

lrbc=Label(window,text="RBC Count (cells/lit",font="Helvetica" "16",bg="yellow") #RBC_COUNT
lrbc.grid(row=8,column=1)
erbc=Entry(window,cursor="arrow",textvariable=RBC,bd=1.5)
erbc.grid(row=8,column=2)

lwbc=Label(window,text="WBC Count (cells/lit)",font="Helvetica" "16",bg="yellow") #WBC_Count
lwbc.grid(row=9,column=1)
ewbc=Entry(window,cursor="arrow",textvariable=WBC,bd=1.5)
ewbc.grid(row=9,column=2)

lplt=Label(window,text="Platelets",font="Helvetica" "16",bg="yellow") #platelets
lplt.grid(row=10,column=1)
eplt=Entry(window,cursor="arrow",textvariable=Plate,bd=1.5)
eplt.grid(row=10,column=2)


lHB=Label(window,text="Hemoglobin (g/dl)",font="Helvetica" "16",bg="yellow") #HB
lHB.grid(row=11,column=1)
eHB=Entry(window,cursor="arrow",textvariable=HB,bd=1.5)
eHB.grid(row=11,column=2)


luric=Label(window,text="Uric Acid (mg/l)",font="Helvetica" "16",bg="yellow") #uric_acid
luric.grid(row=12,column=1)
euric=Entry(window,cursor="arrow",textvariable=UA,bd=1.5)
euric.grid(row=12,column=2)

lcol=Label(window,text="Cholesterol (mg/dl)",font="Helvetica" "16",bg="yellow") #Cholesterol
lcol.grid(row=13,column=1)
ecol=Entry(window,cursor="arrow",textvariable=Chol,bd=1.5)
ecol.grid(row=13,column=2)


def GetGender():
    if(bool(G1.get())==1):
        Gen=G1.get()
    else:
        Gen=G2.get()
def GetDetails():
   # h1=Label(window,text="--------------------------------------")
    #h1.grid(row=17,column=1)
    #h2=Label(window,text="--------------------------------------")
    #h2.grid(row=18,column=1)
    window2=Tk()
    window2.title("User Fitness Report")
    window2.configure(background="blanchedalmond")
    
    l1=Label(window2,fg="black",bg="blanchedalmond",text="Name                    : " +Name.get())
    l1.grid(row=20,column=18)
    l2=Label(window2,fg="black",bg="blanchedalmond",text="Age                     : " +str(Age.get()))
    l2.grid(row=21,column=18)

    l3=Label(window2,fg="black",bg="blanchedalmond",text="BMI(Body Mass Index)           : " +str((Weight.get())/(Height.get())**2))   #output commands
    l3.grid(row=23,column=18)
    l4=Label(window2,fg="black",bg="blanchedalmond",text="Height(cm)           : " +str(Height.get()))
    l4.grid(row=24,column=18)
    l5=Label(window2,fg="black",bg="blanchedalmond",text="BP Low(mm)          : " +str(BPL.get()))
    l5.grid(row=25,column=18)
    l6=Label(window2,fg="black",bg="blanchedalmond",text="BP High(mm)         : " +str(BPH.get()))
    l6.grid(row=26,column=18)
    if(PsRate.get()<60):
        l7=Label(window2,fg="RED",bg="blanchedalmond",text="Pulse Rate(Low)   : " +str(PsRate.get()))
        l7.grid(row=27,column=18)
    elif(60<PsRate.get()<100):
        l7=Label(window2,fg="blue",bg="blanchedalmond",text="Pulse Rate(Medium)   : " +str(PsRate.get()))
        l7.grid(row=27,column=18)
    else:
        l7=Label(window2,fg="black",bg="blanchedalmond",text="Pulse Rate(High)   : " +str(PsRate.get()))
        l7.grid(row=27,column=18)

    if(RBC.get()<4.2):
        l8=Label(window2,fg="RED",bg="blanchedalmond",text="RBC Count(Low) : " +str(RBC.get()))
        l8.grid(row=28,column=18)
    elif(4.2<RBC.get()<6.1):
        l8=Label(window2,fg="blue",bg="blanchedalmond",text="RBC Count(Medium) : " +str(RBC.get()))
        l8.grid(row=28,column=18)
    else:
        l8=Label(window2,fg="black",bg="blanchedalmond",text="RBC Count(High) : " +str(RBC.get()))
        l8.grid(row=28,column=18)

    if(WBC.get()<4500):
        l9=Label(window2,fg="RED",bg="blanchedalmond",text="WBC Count(Low) : " +str(WBC.get()))
        l9.grid(row=29,column=18)
    elif(4500<WBC.get()<10500):
        l9=Label(window2,fg="blue",bg="blanchedalmond",text="WBC Count(Medium) : " +str(WBC.get()))
        l9.grid(row=29,column=18)                                                                               
    else:
        l9=Label(window2,fg="black",bg="blanchedalmond",text="WBC Count(High) : " +str(WBC.get()))
        l9.grid(row=29,column=18)
        
    if(Plate.get()<150000):
        l10=Label(window2,fg="Red",bg="blanchedalmond",text="Platelets(Low)          : " +str(Plate.get()))
        l10.grid(row=30,column=18)
    elif(150000<Plate.get()<450000):
        l10=Label(window2,fg="blue",bg="blanchedalmond",text="Platelets(Medium)           : " +str(Plate.get()))
        l10.grid(row=30,column=18)
    else:
        l10=Label(window2,fg="black",bg="blanchedalmond",text="Platelets(High)         : " +str(Plate.get()))
        l10.grid(row=30,column=18)

    if(HB.get()<13.5):
        l11=Label(window2,fg="red",bg="blanchedalmond",text="Hemoglobin(Low)   : " +str(HB.get()))
        l11.grid(row=31,column=18)
    elif(13.5<HB.get()<18):
        l11=Label(window2,fg="blue",bg="blanchedalmond",text="Hemoglobin(medium)   : " +str(HB.get()))
        l11.grid(row=31,column=18)
    else:
        l11=Label(window2,fg="black",bg="blanchedalmond",text="Hemoglobin(High)   : " +str(HB.get()))
        l11.grid(row=31,column=18)

    if(UA.get()<250):
         l12=Label(window2,fg="red",bg="blanchedalmond",text="Uric Acid(low)     : " +str(UA.get()))
         l12.grid(row=32,column=18)
    elif(250<UA.get()<750):
         l12=Label(window2,fg="blue",bg="blanchedalmond",text="Uric Acid(Medium)     : " +str(UA.get()))
         l12.grid(row=32,column=18)
    else:
         l12=Label(window2,fg="black",bg="blanchedalmond",text="Uric Acid(High)     : " +str(UA.get()))
         l12.grid(row=32,column=18)

    if(Chol.get()<60):
        l13=Label(window2,fg="red",bg="blanchedalmond",text="Cholesterol(Low) : " +str(Chol.get()))
        l13.grid(row=33,column=18)
    elif(60<Chol.get()<200):
        l13=Label(window2,fg="blue",bg="blanchedalmond",text="Cholesterol(Medium) : " +str(Chol.get()))
        l13.grid(row=33,column=18)
    else:
        l13=Label(window2,fg="black",bg="blanchedalmond",text="Cholesterol(High) : " +str(Chol.get()))
        l13.grid(row=33,column=18)

generate=Button(window,text="Generate Report",fg="White",bg="black",borderwidth=3,command=GetDetails)
generate.grid(row=15,column=20)                                        #initialize generate button
window.mainloop()
