from tkinter import *
from tkinter import messagebox
import random
import smtplib

window=Tk()
window.title("Question paper Setter")
window.geometry("865x620+0+0")
window.config(bg="#9B59B6")
frame1=LabelFrame(window,text="number of students",padx=60,pady=10,bg="#9B59B6")
frame1.grid(row=0,column=0,padx=5,pady=10)

frame2=LabelFrame(window,text="Mail id of students",padx=5,pady=10,bg="#9B59B6")
frame2.grid(row=0,column=1,padx=5,pady=10)

frame3=LabelFrame(window,text="Selection",padx=5,pady=10,bg="#9B59B6")
frame3.grid(row=1,column=1,padx=5,pady=10)

frame4=LabelFrame(window,text="TEACHER'S MAIL",padx=10,pady=10,bg="#9B59B6")
frame4.grid(row=1,column=0,padx=5,pady=10)

def fun():
    global a,but1
    a=int(e1.get())
    b1.config(state=DISABLED,bg="black",fg="white")
    but1.config(state=ACTIVE,bg="white",fg="black")

l1=Label(frame1,text="Enter Number of students : ",font=(" Verdana",12,"bold italic"),bg="#9B59B6")
e1=Entry(frame1,width=50,borderwidth=7)
b1=Button(frame1,text="submit",command=fun,state=ACTIVE,bg="white",fg="black")
l1.grid(row=0,column=0,pady=10)
e1.grid(row=1,column=0,pady=10)
b1.grid(row=2,column=0,pady=10)

global count,l,lab1,but1
l=[]

def enter():
    global count,l,but1
    l.append(enty1.get())
    enty1.delete(0,END)
    count+=1
    if count<=a:
        lab1.config(text=f"Please Enter the mail id of student {count}",font=("Verdana",12,"bold italic"),bg="#9B59B6")
    if count>a:
        but1.config(state=DISABLED,bg="black",fg="white")
        f3b1.config(state=ACTIVE,fg="black",bg="white")
   
count=1
lab1=Label(frame2,text="Please Enter the mail ID of student 1",font=("Verdana",12,"bold italic"),bg="#9B59B6")
enty1=Entry(frame2,width=60,borderwidth=7)
but1=Button(frame2,text="Submit",command=enter,state=DISABLED,bg="black",fg="white")
lab1.grid(row=0,column=0,pady=10)
enty1.grid(row=1,column=0,pady=10)
but1.grid(row=2,column=0,pady=10)

global options,yes
options=[]
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
yes=1

def pr():
    global yes
    options.append(var6.get())
    options.append(var1.get())
    options.append(var2.get())
    options.append(var3.get())
    options.append(var4.get())
    options.append(var5.get())
    f3b1.config(state=DISABLED,fg="white",bg="black")
    op=[]
    for i in sorted(options):
        if i!=0:
            op.append(str(i)+" Marks")
    yes=messagebox.askyesno("confirmation","The Numbrer of Students are "+str(count-1)+"\n"+"\n"+"Their mail IDs are"+str(l)+"\n"+"\n"+"the question types are"+str(op)
                        +"\n"+"\n"+"Press \"YES\" to continue or \"NO\" to start from begining")
    if yes:
        openxt(l,options)
        print(options)
    else:
        window.quit()

check6=Checkbutton(frame3,text=" 1 Marks",font=("Verdana",12,"bold italic"),bg="#9B59B6",variable=var6,onvalue=1)
check1=Checkbutton(frame3,text=" 2 Marks",font=("Verdana",12,"bold italic"),bg="#9B59B6",variable=var1,onvalue=2)
check2=Checkbutton(frame3,text=" 5 Marks",font=("Verdana",12,"bold italic"),bg="#9B59B6",variable=var2,onvalue=5)
check3=Checkbutton(frame3,text="10 Marks",font=("Verdana",12,"bold italic"),bg="#9B59B6",variable=var3,onvalue=10)
check4=Checkbutton(frame3,text="13 Marks",font=("Verdana",12,"bold italic"),bg="#9B59B6",variable=var4,onvalue=13)
check5=Checkbutton(frame3,text="16 Marks",font=("Verdana",12,"bold italic"),bg="#9B59B6",variable=var5,onvalue=16)

check6.deselect()
check1.deselect()
check2.deselect()
check3.deselect()
check4.deselect()
check5.deselect()

check6.grid(row=0,column=0,pady=10)
check1.grid(row=1,column=0,pady=10)
check2.grid(row=2,column=0,pady=10)
check3.grid(row=3,column=0,pady=10)
check4.grid(row=4,column=0,pady=10)
check5.grid(row=5,column=0,pady=10)
check6.grid(row=0,column=0,pady=10)

f3b1=Button(frame3,text="Submit",state=DISABLED,bg="black",fg="white",command=pr)
f3b1.grid(row=6,column=0)

#frame 4
def mailget():
    tpass=enttt.get()
    tmail=entt.get()

    
labt=Label(frame4,text="ENTER TEACHER'S MAIL ID",font=(" Verdana",12,"bold italic"),bg="#9B59B6")
labtt=Label(frame4,text="Enter your password",font=(" Verdana",12,"bold italic"),bg="#9B59B6")
entt=Entry(frame4,width=50,borderwidth=7)
enttt=Entry(frame4,width=50,borderwidth=7)
butt=Button(frame4,text="SUBMIT",font=(" Verdana",12,"bold italic"),command=mailget)
labwar=Label(frame4,text="PLEASE REMOVE TWO STEP VERIFICATION",font=(" Verdana",12,"bold italic underline"),bg="#9B59B6")
labwar2=Label(frame4,text="WE WON'T COLLECT ANY OF YOUR INFORMATION \n YOUR DATA REMAINS PRIVATE WITH YOU!!",font=(" Verdana",12,"bold italic underline"),bg="#9B59B6") 
labt.pack(padx=10,pady=10)
entt.pack(padx=10,pady=10)
labtt.pack(padx=10,pady=10)
enttt.pack(padx=10,pady=10)
butt.pack(padx=10,pady=10)
labwar.pack(padx=10,pady=10)
labwar2.pack(padx=10,pady=10)
global m1,m2,m5,m10,m13,m16
m1,m2,m5,m10,m13,m16=[],[],[],[],[],[]
def openxt(l,options):
    root=Toplevel()
    root.title("Step 2")
    #root.geometry("800x700")
    root.config(bg="#16A085")
    rframe1=LabelFrame(root,text="1 Marks",bg="#16A085")
    rframe2=LabelFrame(root,text="2 Marks",bg="#16A085")
    rframe3=LabelFrame(root,text="5 marks",bg="#16A085")
    rframe4=LabelFrame(root,text="10 marks",bg="#16A085")
    rframe5=LabelFrame(root,text="13 marks",bg="#16A085")
    rframe6=LabelFrame(root,text="16 marks",bg="#16A085")
    rframe1.grid(row=0,column=0,pady=3)
    rframe2.grid(row=0,column=1,pady=3)
    rframe3.grid(row=1,column=0,pady=3)
    rframe4.grid(row=1,column=1,pady=3)
    rframe5.grid(row=2,column=0,pady=3)
    rframe6.grid(row=2,column=1,pady=3)

    def ent1():
        m1.append(ent1r.get('1.0',END))
        ent1r.delete('1.0',END)
        lab2r.config(text=f"You've entered {len(m1)} Questions in 1 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")
        
    
    lab1r=Label(rframe1,text="Enter 1 Mark Questions",font=(" Verdana",12,"bold italic"),bg="#16A085")
    ent1r=Text(rframe1,height=3,width=30,borderwidth=7)
    but1r=Button(rframe1,text="Enter",command=ent1,font=(" Verdana",12,"bold italic"),bg="#99aab5")
    lab2r=Label(rframe1,text="You've entered 0 Questions in 1 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")
    lab1r.grid(row=0,column=0,padx=10,pady=10)
    ent1r.grid(row=0,column=1,padx=10,pady=10)
    but1r.grid(row=1,column=1,padx=10,pady=10)
    lab2r.grid(row=1,column=0,padx=10,pady=10)
    
    def ent2():
        m2.append(ent2r.get('1.0',END))
        ent2r.delete('1.0',END)
        lab4r.config(text=f"You've entered {len(m2)} Questions in 2 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")

    lab3r=Label(rframe2,text="Enter 2 Mark Questions",font=(" Verdana",12,"bold italic"),bg="#16A085")
    ent2r=Text(rframe2,height=3,width=30,borderwidth=7)
    but2r=Button(rframe2,text="Enter",command=ent2,font=(" Verdana",12,"bold italic"),bg="#99aab5")
    lab4r=Label(rframe2,text="You've entered 0 Questions in 2 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")
    lab3r.grid(row=0,column=0,padx=10,pady=10)
    ent2r.grid(row=0,column=1,padx=10,pady=10)
    but2r.grid(row=1,column=1,padx=10,pady=10)
    lab4r.grid(row=1,column=0,padx=10,pady=10)

    def ent3():
        m5.append(ent3r.get('1.0',END))
        ent3r.delete('1.0',END)
        lab6r.config(text=f"You've entered {len(m5)} Questions in 5 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")
        
    lab5r=Label(rframe3,text="Enter 5 Mark Questions",font=(" Verdana",12,"bold italic"),bg="#16A085")
    ent3r=Text(rframe3,height=3,width=30,borderwidth=7)
    but3r=Button(rframe3,text="Enter",command=ent3,font=(" Verdana",12,"bold italic"),bg="#99aab5")
    lab6r=Label(rframe3,text="You've entered 0 Questions in 5 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")
    lab5r.grid(row=0,column=0,padx=10,pady=10)
    ent3r.grid(row=0,column=1,padx=10,pady=10)
    but3r.grid(row=1,column=1,padx=10,pady=10)
    lab6r.grid(row=1,column=0,padx=10,pady=10)

    def ent4():
        m10.append(ent4r.get('1.0',END))
        ent4r.delete('1.0',END)
        lab8r.config(text=f"You've entered {len(m10)} Questions in 10 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")
            
    lab7r=Label(rframe4,text="Enter 10 Mark Questions",font=(" Verdana",12,"bold italic"),bg="#16A085")
    ent4r=Text(rframe4,height=3,width=30,borderwidth=7)
    but4r=Button(rframe4,text="Enter",command=ent4,font=(" Verdana",12,"bold italic"),bg="#99aab5")
    lab8r=Label(rframe4,text="You've entered 0 Questions in 10 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")
    lab7r.grid(row=0,column=0,padx=10,pady=10)
    ent4r.grid(row=0,column=1,padx=10,pady=10)
    but4r.grid(row=1,column=1,padx=10,pady=10)
    lab8r.grid(row=1,column=0,padx=10,pady=10)

    def ent5():
        m13.append(ent5r.get('1.0',END))
        ent5r.delete('1.0',END)
        lab10r.config(text=f"You've entered {len(m13)} Questions in 13 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")

    lab9r=Label(rframe5,text="Enter 13 Mark Questions",font=(" Verdana",12,"bold italic"),bg="#16A085")
    ent5r=Text(rframe5,height=3,width=30,borderwidth=7)
    but5r=Button(rframe5,text="Enter",command=ent5,font=(" Verdana",12,"bold italic"),bg="#99aab5")
    lab10r=Label(rframe5,text="You've entered 0 Questions in 13 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")
    lab9r.grid(row=0,column=0,padx=10,pady=10)
    ent5r.grid(row=0,column=1,padx=10,pady=10)
    but5r.grid(row=1,column=1,padx=10,pady=10)
    lab10r.grid(row=1,column=0,padx=10,pady=10)

    def ent6():
        m16.append(ent6r.get('1.0',END))
        ent6r.delete('1.0',END)
        lab12r.config(text=f"You've entered {len(m16)} Questions in 16 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")

    lab11r=Label(rframe6,text="Enter 16 Mark Questions",font=(" Verdana",12,"bold italic"),bg="#16A085")
    ent6r=Text(rframe6,height=3,width=30,borderwidth=7)
    but6r=Button(rframe6,text="Enter",command=ent6,font=(" Verdana",12,"bold italic"),bg="#99aab5")
    lab12r=Label(rframe6,text="You've entered 0 Questions in 16 marks",font=(" Verdana",12,"bold italic"),bg="#16A085")
    lab11r.grid(row=0,column=0,padx=10,pady=10)
    ent6r.grid(row=0,column=1,padx=10,pady=10)
    but6r.grid(row=1,column=1,padx=10,pady=10)
    lab12r.grid(row=1,column=0,padx=10,pady=10)

    def getdata():
        final=Toplevel()
        final.title("confirmation")
        final.geometry("800x600")
        mailid=l
        final.config(bg="#D35400")
        frame1f=LabelFrame(final,text="Selection",bg="#D35400")
        
        data=[0,0,0,0,0,0]
        frame1f.grid(padx=10,pady=10)

        lab1f=Label(frame1f,text="Enter No. of questions for 1 marks",bg="#D35400",font=(" Verdana",12,"bold italic"))
        lab11f=Label(frame1f,text=f"(Out of {len(m1)} questions you entered)",bg="#D35400",font=(" Verdana",12,"bold italic"))
        ent1f=Entry(frame1f,width=10,borderwidth=7)
        lab1f.grid(row=0,column=0,padx=10,pady=5)
        lab11f.grid(row=1,column=0,padx=10,pady=5)
        ent1f.grid(row=0,column=1,padx=10,pady=5)

        lab2f=Label(frame1f,text="Enter No. of questions for 2 marks",bg="#D35400",font=(" Verdana",12,"bold italic"))
        lab22f=Label(frame1f,text=f"(Out of {len(m2)} questions you entered)",bg="#D35400",font=(" Verdana",12,"bold italic"))
        ent2f=Entry(frame1f,width=10,borderwidth=7)
        lab2f.grid(row=0,column=2,padx=10,pady=5)
        lab22f.grid(row=1,column=2,padx=10,pady=5)
        ent2f.grid(row=0,column=3,padx=10,pady=5)

        lab3f=Label(frame1f,text="Enter No. of questions for 5 marks",bg="#D35400",font=(" Verdana",12,"bold italic"))
        lab33f=Label(frame1f,text=f"(Out of {len(m5)} questions you entered)",bg="#D35400",font=(" Verdana",12,"bold italic"))
        ent3f=Entry(frame1f,width=10,borderwidth=7)
        lab3f.grid(row=2,column=0,padx=10,pady=5)
        lab33f.grid(row=3,column=0,padx=10,pady=5)
        ent3f.grid(row=2,column=1,padx=10,pady=5)

        lab4f=Label(frame1f,text="Enter No. of questions for 10 marks",bg="#D35400",font=(" Verdana",12,"bold italic"))
        lab44f=Label(frame1f,text=f"(Out of {len(m10)} questions you entered)",bg="#D35400",font=(" Verdana",12,"bold italic"))
        ent4f=Entry(frame1f,width=10,borderwidth=7)
        lab4f.grid(row=2,column=2,padx=10,pady=5)
        lab44f.grid(row=3,column=2,padx=10,pady=5)
        ent4f.grid(row=2,column=3,padx=10,pady=5)

        lab5f=Label(frame1f,text="Enter No. of questions for 13 marks",bg="#D35400",font=(" Verdana",12,"bold italic"))
        lab55f=Label(frame1f,text=f"(Out of {len(m13)} questions you entered)",bg="#D35400",font=(" Verdana",12,"bold italic"))
        ent5f=Entry(frame1f,width=10,borderwidth=7)
        lab5f.grid(row=4,column=0,padx=10,pady=5)
        lab55f.grid(row=5,column=0,padx=10)
        ent5f.grid(row=4,column=1,padx=10,pady=5)

        lab6f=Label(frame1f,text="Enter No. of questions for 16 marks",bg="#D35400",font=(" Verdana",12,"bold italic"))
        lab66f=Label(frame1f,text=f"(Out of {len(m16)} questions you entered)",bg="#D35400",font=(" Verdana",12,"bold italic"))
        ent6f=Entry(frame1f,width=10,borderwidth=7)
        lab6f.grid(row=4,column=2,padx=10,pady=5)
        lab66f.grid(row=5,column=2,padx=10)
        ent6f.grid(row=4,column=3,padx=10,pady=5)
        
        def sub():
            global tmail,tpass
            frame2f=LabelFrame(final,text="PROGRESS",bg="#CA6F1E")
            frame2f.grid(padx=10,pady=10)
            lf=Label(frame2f,text="Sit back and relax...\n We'll let you know once it's done!",font=(" Verdana",12,"bold italic"),bg="#CA6F1E")
            lf.grid(row=0,column=0,ipadx=100,ipady=100)
            if ent1f.get():data[0]=int(ent1f.get())
            if ent2f.get():data[1]=int(ent2f.get())
            if ent3f.get():data[2]=int(ent3f.get())
            if ent4f.get():data[3]=int(ent4f.get())
            if ent5f.get():data[4]=int(ent5f.get())
            if ent6f.get():data[5]=int(ent6f.get())
            numberofstu=a
            
            connect=smtplib.SMTP('smtp.gmail.com',25)
            connect.ehlo()
            connect.starttls()
            mail=tmail
            pas=tpass
            print(mail,pas)
            connect.login(entt.get(),enttt.get())
            for i in range(numberofstu):
                dupm1,dupm2,dupm5,dupm10,dupm13,dupm16=[],[],[],[],[],[]
                dupm1+=m1
                dupm2+=m2
                dupm5+=m5
                dupm10+=m10
                dupm13+=m13
                dupm16+=m16
                content=""
                if m1:
                    content+="\n***\n1 Mark Questions:\n\n"
                    for j in range(data[0]):
                        if dupm1:
                            q=random.choice(dupm1)
                            dupm1.remove(q)
                            content=content+f"\n{j+1}. "+q
                
                if m2:
                    content+="\n***\n2 Mark Questions:\n\n"
                    for j in range(data[1]):
                        if dupm2:
                            q=random.choice(dupm2)
                            dupm2.remove(q)
                            content=content+f"\n{j+1}. "+q
                    
                if m5:
                    content+="\n***\n5 Mark Questions:\n\n"
                    for j in range(data[2]):
                        if dupm5:
                            q=random.choice(dupm5)
                            dupm5.remove(q)
                            content=content+f"\n{j+1}. "+q
                    
                if m10:
                    content+="\n***\n10 Mark Questions:\n\n"
                    for j in range(data[3]):
                        if dupm10:
                            q=random.choice(dupm10)
                            dupm10.remove(q)
                            content=content+f"\n{j+1}. "+q
                
                if m13:
                    content+="\n***\n13 Mark Questions:\n\n"
                    for j in range(data[4]):
                        if dupm13:
                            q=random.choice(dupm13)
                            dupm13.remove(q)
                            content=content+f"\n{j+1}. "+q
                
                if m16:
                    content+="\n***\n16 Mark Questions:\n"+"\n"
                    for j in range(data[5]):
                        if dupm16:
                            q=random.choice(dupm16)
                            dupm16.remove(q)
                            content=content+f"\n{j+1}. "+q
                
                connect.sendmail(mailid[i],mailid[i],content)
                print(mailid[i])
                dupm1.clear()
                dupm2.clear()
                dupm5.clear()
                dupm10.clear()
                dupm13.clear()
                dupm16.clear()
            lf.config(text="E-mail sent successfully!")
            connect.quit()

window.mainloop()