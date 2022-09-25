from tkinter import *
from tkinter import ttk
from tkinter import messagebox
loggeduser=""
loggedname=""
def gotocpage():
    global root
    root.destroy()
    cabbook()
def validate():
    global userEntered
    global passEntered
    global root
    global loggeduser
    global loggedname
    flag=True
    usr=userEntered.get()
    pwd=passEntered.get()
    f=open("users.txt",'r')
    users=list(f)
    f.close()
    for i in users:
        uname,passw,name,email,secq,secan=i.split('|')
        if usr==uname and pwd==passw:
            root.destroy()
            loggeduser=usr
            loggedname=name
            cabbook()
            return
    messagebox.showerror("Error", "Invalid Id or password")
def RegisterNow():
    global userEntered
    global passEntered
    global nameEntered
    global emailEntered
    global root
    global user
    global securityanswer
    global var
    usr=userEntered.get()
    pwd=passEntered.get()
    name=nameEntered.get()
    email=emailEntered.get()
    secans=securityanswer.get()
    seques=var.get()
    if secans!="" and seques!="" and email!="" and usr!="" and pwd!="" and name!="": 
                if '@' in email and '.com' in email: 
                    flag=0
                    f=open("users.txt",'r')
                    users=list(f)
                    f.close()
                    for i in users:
                        if usr in i or email in i:
                           messagebox.showerror("Validatation Error", "Username/Email Already Exists")
                           flag=1
                    if flag==0:
                        f=open("users.txt",'a')
                        f.write(usr+'|'+pwd+'|'+name+'|'+email+'|'+seques+'|'+secans+'\n')
                        f.close()
                        messagebox.showinfo("Registration Successful", "Registration success! You Can Now Login")
                else:
                    messagebox.showerror("Validatation Error", "Invalid Email Address")
    else:
        messagebox.showerror("Invalid Entry", "Empty Entries given")
def RegisterPage():
    global root
    global backgroundIMG
    global userEntered
    global passEntered
    global canvas
    global var
    global nameEntered
    global emailEntered
    global securityanswer
    canvas.delete('all')
    backgroundIMG=PhotoImage(file="566.jpg")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(90,100,430,550,fill="#000",outline="white")
    canvas.create_text(250,140,text="Register",fill='white',font=("Arial",25,'bold'))
    canvas.create_text(150,240,text="Username:",fill='white',font=("Arial",13,'bold'))
    canvas.create_text(150,200,text="Your Name",fill='white',font=("Arial",13,'bold'))
    nameEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'))
    userEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'))
    emailEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'))
    canvas.create_text(150,280,text="Password:",fill='white',font=("Arial",13,'bold'))
    canvas.create_text(150,450,text="Answer:",fill='white',font=("Arial",13,'bold'))
    canvas.create_text(150,320,text="Email:",fill='white',font=("Arial",13,'bold'))
    canvas.create_text(280,380,text="Security Question:",fill='white',font=("Arial",13,'bold'))
    bullet = "\u2022"
    passEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'),show=bullet)
    canvas.create_window(300,200,window=nameEntered)
    var = StringVar(root)
    var.set("What was your childhood nickname?")
    secmenu=  ttk.Combobox(root, width=30,height=20,textvariable=var)
    secmenu['values'] =["What was your childhood nickname?","What is your favorite movie?","What was the make and model of your first car?","What school did you attend for sixth grade?"]
    secmenu['state'] = 'readonly'
    securityanswer=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'))
    canvas.create_window(300,450,window=securityanswer)
    canvas.create_window(300,320,window=emailEntered)
    canvas.create_window(290,410,window=secmenu)
    canvas.create_window(300,240,window=userEntered)
    canvas.create_window(300,280,window=passEntered)
    Regbutton=Button(canvas,text="Register",width=10,fg="white",bg="#088",font=("Arial",13,'bold'),command=RegisterNow)
    canvas.create_window(200,500,window=Regbutton)
    Loginbutton=Button(canvas,text="Login",fg="white",bg="#000",bd=0,font=("Arial",13,'bold'),command=loginpage)
    canvas.create_window(320,500,window=Loginbutton)

    
def forgotpass():
    global userEntered
    global passEntered
    global securityanswer
    global var
    global root
    global user
    usr=userEntered.get()
    pwd=passEntered.get()
    seciq=var.get()
    secians=securityanswer.get()
    if secians!="" and seciq!="" and usr!="" and pwd!="":
        flag=0
        f=open("users.txt",'r')
        users=list(f)
        f.close()
        for i in range(len(users)):
            uname,passw,nme,email,secq,secan=users[i].split('|')
            if usr==uname and secq.upper()==seciq.upper() and secan.upper().rstrip()==secians.upper():
                users[i]=uname+'|'+pwd+'|'+nme+'|'+email+'|'+secq+'|'+secan
                flag=1
        if flag:
             f=open("users.txt",'w')
             for i in users:
                 f.write(i)
             f.close()
             messagebox.showinfo("Successfull", "Password Reset Success ")
        else:
             messagebox.showerror("Error", "Invalid username or Security Question")
    else:
         messagebox.showerror("Error", "Empty Enrties")

def submitreview():
    global var
    global feedEntry
    global canvas
    global loggeduser
    review=feedEntry.get("1.0",'end-1c')
    with open('reviews.txt','a') as f:
        f.write(loggeduser+'|'+str(var.get())+'|'+review+'\n')
        messagebox.showinfo("Successfull", "Review Successfully submitted")
def feedpage():
    global root
    global canvas
    global gifimg
    global var
    global feedEntry
    canvas.delete('all')
    gifimg=PhotoImage(file="background.gif")
    canvas.create_image(0,0,image=gifimg,anchor=NW)
    rebutton=Button(canvas,text="booking page",width=15,fg="white",bg="Red",bd=0,font=("Arial",13,'bold'),command=gotocpage)
    canvas.create_window(1200,50,window=rebutton)
    ebutton=Button(canvas,text="Give Review",width=15,fg="white",bg="Red",font=("Arial",13,'bold'),command=submitreview)
    canvas.create_window(850,650,window=ebutton)
    canvas.create_text(683,100,text="Feedback" ,fill="White",font=("Arial",25,'underline'))
    canvas.create_text(400,300,text="Rating" ,fill="red",font=("Arial",13))
    canvas.create_text(400,450,text="Review" ,fill="red",font=("Arial",13))
    var = StringVar(root)
    var.set(1)
    secmenu=  ttk.Combobox(root, width=30,height=20,textvariable=var)
    secmenu['values'] =list(range(1,6))
    secmenu['state'] = 'readonly'
    feedEntry=Text(canvas, height=10, width=65,fg='White',bg="red",bd=4,font=("Arial",10,'italic'))
    canvas.create_window(850,450,window=feedEntry)
    canvas.create_window(850,300,window=secmenu)

def changepass():
    global oldpassEntered
    global passEntered
    global loggeduser
    global var
    global root
    global user
    opass=oldpassEntered.get()
    pwd=passEntered.get()
    if opass!="" and pwd!="":
        flag=0
        f=open("users.txt",'r')
        users=list(f)
        f.close()
        for i in range(len(users)):
            uname,passw,nme,email,secq,secan=users[i].split('|')
            if opass==passw and loggeduser ==uname:
                users[i]=uname+'|'+pwd+'|'+nme+'|'+email+'|'+secq+'|'+secan
                flag=1
        if flag:
             f=open("users.txt",'w')
             for i in users:
                 f.write(i)
             f.close()
             messagebox.showinfo("Successfull", "Password Reset Success ")
        else:
             messagebox.showerror("Error", "Invalid Eixting Password")
    else:
         messagebox.showerror("Error", "Empty Enrties")

def viewbooking():
    global canvas
    global backgroundIMG
    global y
    global loggeduser
    canvas.delete('all')
    
    rebutton=Button(canvas,text="booking page",width=15,fg="white",bg="Red",bd=0,font=("Arial",13,'bold'),command=gotocpage)
    canvas.create_window(1200,50,window=rebutton)
    backgroundIMG=PhotoImage(file="background.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    x,y=0,30
    canvas.create_rectangle(150,20,1250,500,fill="white")
    canvas.create_text(683,50,text="Your bookings " ,fill="Maroon",font=("Arial",25,'bold'))
    try:
        f=open(loggeduser+'.txt','r')
        hiss=list(f)
        f.close()
        h=["Passanger","PhoneNo","Source","Destination","Date of Journey","class"]
        for j in range(len(h)):
                canvas.create_text(200+x,110,text=str(h[j]) ,fill="Maroon",font=("Arial",13,'bold'))
                x+=200
        for i in range(len(hiss)):
            x=0
            xi=hiss[i].split('|')
            xi[-1]=xi[-1].rstrip()
            for j in range(len(xi)):
                canvas.create_text(200+x,110+y,text=str(xi[j]) ,fill="maroon",font=("Arial",12))
                x+=200
            y+=30
    except:
        canvas.create_text(700,280,text="No bookings to show" ,fill="Red",font=("Arial",12))
def forgotpage():
    global root
    global canvas
    global userEntered
    global passEntered
    global var
    global securityanswer
    global backgroundIMG
    canvas.delete('all')
    backgroundIMG=PhotoImage(file="background.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(90,150,430,550,fill="#000",outline="white")
    canvas.create_text(240,200,text="Reset Password",fill='white',font=("Arial",25,'bold'))
    canvas.create_text(150,300,text="Username",fill='white',font=("Arial",13,'bold'))
    userEntered=Entry(canvas,bg="white",bd=4,fg='#000',font=("Arial",13,'bold'))
    canvas.create_text(150,350,text="Password",fill='white',font=("Arial",13,'bold'))
    canvas.create_text(150,460,text="Answer",fill='white',font=("Arial",13,'bold'))
    canvas.create_text(250,390,text="Security Question:",fill='white',font=("Arial",13,'bold'))
    bullet = "\u2022"
    passEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'),show=bullet)
    canvas.create_window(290,300,window=userEntered)
    canvas.create_window(290,350,window=passEntered)
    var = StringVar(root)
    var.set("What was your childhood nickname?")
    secmenu=  ttk.Combobox(root, width=40,height=20,textvariable=var)
    secmenu['values'] =["What was your childhood nickname?","What is your favorite movie?","What was the make and model of your first car?","What school did you attend for sixth grade?"]
    secmenu['state'] = 'readonly'

    securityanswer=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'))
    canvas.create_window(280,420,window=secmenu)
    canvas.create_window(290,460,window=securityanswer)
    Resetbutton=Button(canvas,text="Reset Password",width=15,fg="white",bg="#088",font=("Arial",13,'bold'),command=forgotpass)
    canvas.create_window(200,500,window=Resetbutton)
    loginbutton=Button(canvas,text="Login",fg="white",bg="#000",bd=0,font=("Arial",13,'bold'),command=loginpage)
    canvas.create_window(320,500,window=loginbutton)
    
def book():
    global Fromvar
    global Tovar
    global DayVar
    global MonVar
    global yrVar
    global classvar
    global canvas
    global loggeduser
    global PassName
    global PhoneNo
    if PhoneNo.get().isdigit():
        f=open(loggeduser+'.txt','a')
        if len(PhoneNo.get())==10 or PassName.get()!='' :
            f.write(PassName.get()+'|'+PhoneNo.get()+'|'+Fromvar.get()+'|'+Tovar.get()+'|'+str(DayVar.get())+'-'+str(MonVar.get())+'-'+str(yrVar.get())+'|'+classvar.get()+'\n')
            messagebox.showinfo("Success", "Your booking is Successfull")
            f.close()
        else:
             messagebox.showerror("Error", "Empty PhoneNo or Passanger Name")
             f.close()
    else:
        messagebox.showerror("Error", "Please Enter Only Digits in PhoneNo")
cvar,cvar1=0,0
def createFrom(event):
    global canvas
    global cvar
    global fvar
    global Fromvar
    global line
    if cvar>0:
        canvas.delete(fvar,line)
    fvar=canvas.create_text(653,50,text=Fromvar.get(),font=("Arial",10,"bold"),fill="white")
    line=canvas.create_line(700,50,750,50,fill="White",arrow=LAST,width=2)
    cvar+=1
def createTo(event):
    global canvas
    global cvar1
    global fvar1
    global Tovar
    global Fromvar
    global fare
    if cvar1>0:
        canvas.delete(fvar1)
    fvar1=canvas.create_text(800,50,text=Tovar.get(),font=("Arial",10,"bold"),fill="white")
    fre=0
    cvar1+=1
cvar2=0
def classget():
    global canvas
    global cvar2
    global Tovar
    global classvar
    global Fromvar
    global fare
    if cvar2>0:
        canvas.delete(fare)
    mul=1
    if classvar.get()=="Economy":
        mul=1
    elif classvar.get()=="buissness":
        mul=3
    else:
        mul=5
    locs=["Delhi",
          "Mumbai",
          "Chennai",
          "Kolkata",
          "Jaipur",
          "Guwahati",
          "Indore",
          "Chandigarh",
          "Lucknow",
          "Agra",
          "Hayderabad",
          "Pune",
          "Nasik",
          "Panji"]
    fre=locs.index(Fromvar.get())-locs.index(Tovar.get())
    fare=canvas.create_text(880,50,text="Fare :"+str(abs(fre*100*mul)),font=("Arial",10,"bold"),fill="white")
    cvar2+=1
    
def cabbook():
    global root
    global backgroundIMG
    global Fromvar
    global Tovar
    global DayVar
    global MonVar
    global yrVar
    global classvar
    global canvas
    global loggeduser
    global PassName
    global PhoneNo
    global loggedname
    root=Tk()
    root.title("Login Page")
    canvas=Canvas(root,width=1366,height=768,highlightthickness=0)
    backgroundIMG=PhotoImage(file="background1.gif")
    canvas.create_image(0,100,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(0,0,1366,200,fill="navy blue",outline="navy blue")
    canvas.create_rectangle(590,200,890,500,fill="white")
    canvas.create_text(20,30,text="KCabs",fill='white',font=("bauhaus 93",25),anchor=NW)
    canvas.create_text(20,60,text="The best a cab can get",fill='white',font=("Lucida calligraphy",15),anchor=NW)
    IndiaMap=PhotoImage(file="India-map.gif")
    canvas.create_image(683,140,image=IndiaMap)
    canvas.create_text(580,100,text="O",fill='white',font=("Comic sans",13))
    canvas.create_text(580,120,text=".",fill='white',font=("Comic sansr",20))
    canvas.create_text(580,135,text=".",fill='white',font=("Comic sans",20))
    canvas.create_text(620,100,text="From",fill='white',font=("Arial",10))
    canvas.create_text(610,170,text="To",fill='white',font=("Arial",10))
    Locicon=PhotoImage(file="loc-icon.gif")
    canvas.create_image(580,170,image=Locicon)
    Fromvar = StringVar(root)
    Fromvar.set("Delhi")
    From=  ttk.Combobox(root, width=30,height=20,textvariable=Fromvar)
    From['values'] =["Delhi",
                     "Mumbai",
                     "Chennai",
                     "Kolkata",
                     "Jaipur",
                     "Guwahati",
                     "Indore",
                     "Chandigarh",
                     "Lucknow",
                     "Agra",
                     "Hayderabad",
                     "Pune",
                     "Nasik",
                     "Panji"]
    From['state'] = 'readonly'
    From.bind('<<ComboboxSelected>>',createFrom)
    Tovar = StringVar(root)
    Tovar.set("Delhi")
    To=  ttk.Combobox(root, width=30,height=20,textvariable=Tovar)
    To['values'] =["Delhi",
                     "Mumbai",
                     "Chennai",
                     "Kolkata",
                     "Jaipur",
                     "Guwahati",
                     "Indore",
                     "Chandigarh",
                     "Lucknow",
                     "Agra",
                     "Hayderabad",
                     "Pune",
                     "Nasik",
                     "Panji"]

    To['state'] = 'readonly'
    To.bind('<<ComboboxSelected>>',createTo)
    canvas.create_window(800,100,window=From)
    canvas.create_window(800,170,window=To)
    DayVar = StringVar(root)
    DayVar.set(1)
    Day=  ttk.Combobox(root, width=3,height=20,textvariable=DayVar)
    Day['values'] =list(range(1,32))
    Day['state'] = 'readonly'
    canvas.create_text(630,230,text="Day",font=("Arial",10))
    canvas.create_window(665,230,window=Day)
    MonVar = StringVar(root)
    MonVar.set(1)
    Mon=  ttk.Combobox(root, width=3,height=20,textvariable=MonVar)
    Mon['values'] =list(range(1,13))
    Mon['state'] = 'readonly'
    canvas.create_text(710,230,text="Month",font=("Arial",10))
    canvas.create_window(750,230,window=Mon)
    yrVar = StringVar(root)
    yrVar.set(2018)
    yr=  ttk.Combobox(root, width=5,height=20,textvariable=yrVar)
    yr['values'] =list(range(2018,2030))
    yr['state'] = 'readonly'
    canvas.create_text(790,230,text="Year",font=("Arial",10))
    canvas.create_window(835,230,window=yr)
    classvar=StringVar(root)
    canvas.create_text(740,270,text="Select Class of Travel",font=("Arial",10))
    r1=Radiobutton(root,text="Economy",variable=classvar,bg="white",value="Economy",command=classget)
    canvas.create_window(670,300,window=r1)
    r2=Radiobutton(root,text="buissness",variable=classvar,bg="white",value="buissness",command=classget)
    canvas.create_window(750,300,window=r2)
    r3=Radiobutton(root,text="Luxury",variable=classvar,bg="white",value="Luxury",command=classget)
    canvas.create_window(820,300,window=r3)
    PhoneNo=Entry(canvas,bd=3)
    PassName=Entry(canvas,bd=3)
    canvas.create_text(660,350,text="Passanger Name",font=("Arial",10))
    canvas.create_window(780,350,window=PassName)
    canvas.create_text(680,400,text="Phone No.",font=("Arial",10))
    canvas.create_window(780,400,window=PhoneNo)
    bookbutton=Button(canvas,text="book Ride",width=10,fg="white",bg="#088",font=("Arial",13,'bold'),command=book)
    canvas.create_window(750,450,window=bookbutton)
    canvas.create_text(1200,50,text="Welcome "+loggedname,font=("Arial",15),fill="white")
    canvas.pack()
    detbutton=Button(canvas,text="View Past booking",width=15,fg="white",bg="navy blue",bd=0,font=("Arial",13,'bold'),command=viewbooking)
    canvas.create_window(1200,90,window=detbutton)
    lobutton=Button(canvas,text="Logout",width=15,fg="white",bg="navy blue",bd=0,font=("Arial",13,'bold'),command=loginpage)
    canvas.create_window(1200,180,window=lobutton)
    cpbutton=Button(canvas,text="Change your Password",width=20,fg="white",bg="navy blue",bd=0,font=("Arial",13,'bold'),command=changepasswordpage)
    canvas.create_window(1200,110,window=cpbutton)
    revbutton=Button(canvas,text="Review",width=20,fg="white",bg="navy blue",bd=0,font=("Arial",13,'bold'),command=feedpage)
    canvas.create_window(1200,140,window=revbutton)
    root.mainloop()
def cadminlogin():
    global userEntered
    global passEntered
    global root
    flag=True
    usr=userEntered.get()
    pwd=passEntered.get()
    if usr=="Admin" and pwd=="Admin":
            showfeed()
            return
    messagebox.showerror("Error", "Invalid Id or password")
def showfeed():
    global canvas
    global backgroundIMG
    global y
    global loggeduser
    canvas.delete('all')
    
    rebutton=Button(canvas,text="logout",width=15,fg="white",bg="Red",bd=0,font=("Arial",13,'bold'),command=adminloginpage)
    canvas.create_window(1200,50,window=rebutton)
    backgroundIMG=PhotoImage(file="background.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    x,y=0,30
    canvas.create_rectangle(150,20,1250,500,fill="white")
    canvas.create_text(683,50,text="Reviews " ,fill="Maroon",font=("Arial",25,'bold'))
    try:
        f=open('reviews.txt','r')
        hiss=list(f)
        f.close()
        h=["User","Rating","Review"]
        for j in range(len(h)):
                canvas.create_text(210+x,110,text=str(h[j]) ,fill="Maroon",font=("Arial",13,'bold'))
                x+=380
        for i in range(len(hiss)):
            x=0
            xi=hiss[i].split('|')
            xi[-1]=xi[-1].rstrip()
            for j in range(len(xi)):
                canvas.create_text(200+x,110+y,text=str(xi[j]) ,fill="maroon",font=("Arial",12),anchor=NW)
                x+=380
            y+=30
    except:
        canvas.create_text(700,280,text="No Reviews to show" ,fill="Red",font=("Arial",12))
def adminloginpage():
    global root
    global backgroundIMG
    global userEntered
    global passEntered
    global canvas
    canvas.delete('all')
    backgroundIMG=PhotoImage(file="background.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(90,150,430,550,fill="#000",outline="white")
    canvas.create_text(250,200,text="Admin Login",fill='white',font=("Arial",25,'bold'))
    canvas.create_text(150,300,text="Username",fill='white',font=("Arial",13,'bold'))
    userEntered=Entry(canvas,bd=4,font=("Arial",13,'bold'))
    canvas.create_text(150,350,text="Password",fill='white',font=("Arial",13,'bold'))
    passEntered=Entry(canvas,bd=4,font=("Arial",13,'bold'),show='*')
    canvas.create_window(300,300,window=userEntered)
    canvas.create_window(300,350,window=passEntered)
    Loginbutton=Button(canvas,text="Login",width=10,fg="white",bg="#088",font=("Arial",13,'bold'),command=cadminlogin)
    canvas.create_window(200,450,window=Loginbutton)
    sbutton=Button(canvas,text="user section",width=10,fg="white",bg="#000",bd=0,font=("Arial",13,'bold'),command=loginpage)
    canvas.create_window(350,450,window=sbutton)
def changepasswordpage():
    global root
    global canvas
    global oldpassEntered
    global passEntered
    global var
    global securityanswer
    global backgroundIMG
    canvas.delete('all')
    backgroundIMG=PhotoImage(file="background.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(600,150,1000,550,fill="#000",outline="white")
    canvas.create_text(780,200,text="Reset Password",fill='white',font=("Arial",25,'bold'))
    canvas.create_text(700,300,text="Old Password",fill='white',font=("Arial",13,'bold'))
    oldpassEntered=Entry(canvas,bg="white",bd=4,fg='#000',font=("Arial",13,'bold'),show="*")
    canvas.create_text(700,350,text="New Password",fill='white',font=("Arial",13,'bold'))
    passEntered=Entry(canvas,bg="white",bd=4,font=("Arial",13,'bold'),show='*')
    canvas.create_window(860,300,window=oldpassEntered)
    canvas.create_window(860,350,window=passEntered)
    Resetbutton=Button(canvas,text="Reset Password",width=15,fg="white",bg="#088",font=("Arial",13,'bold'),command=changepass)
    canvas.create_window(760,450,window=Resetbutton)
    backbutton=Button(canvas,text="Back",fg="white",bg="#000",bd=0,font=("Arial",13,'bold'),command=gotocpage)
    canvas.create_window(890,450,window=backbutton)
def loginpage():
    global root
    global backgroundIMG
    global userEntered
    global passEntered
    global canvas
    canvas.delete('all')
    backgroundIMG=PhotoImage(file="background.gif")
    canvas.create_image(0,0,image=backgroundIMG,anchor=NW)
    canvas.create_rectangle(90,150,430,550,fill="#000",outline="white")
    canvas.create_text(250,200,text="Login",fill='white',font=("Arial",25,'bold'))
    canvas.create_text(150,300,text="Username",fill='white',font=("Arial",13,'bold'))
    userEntered=Entry(canvas,bd=4,font=("Arial",13,'bold'))
    canvas.create_text(150,350,text="Password",fill='white',font=("Arial",13,'bold'))
    passEntered=Entry(canvas,bd=4,font=("Arial",13,'bold'),show='*')
    canvas.create_window(300,300,window=userEntered)
    canvas.create_window(300,350,window=passEntered)
    Loginbutton=Button(canvas,text="Login",width=10,fg="white",bg="#088",font=("Arial",13,'bold'),command=validate)
    canvas.create_window(200,450,window=Loginbutton)
    Regbutton=Button(canvas,text="Register",fg="white",bg="#000",bd=0,font=("Arial",13,'bold'),command=RegisterPage)
    canvas.create_window(320,450,window=Regbutton)
    forgbutton=Button(canvas,text="Forgot Password",fg="white",bg="#000",bd=0,font=("Arial",10,'underline'),command=forgotpage)
    canvas.create_window(280,380,window=forgbutton)
    abutton=Button(canvas,text="Admin Login",fg="white",bg="#000",bd=0,font=("Arial",10,'underline'),command=adminloginpage)
    canvas.create_window(280,500,window=abutton)
    canvas.pack()
    root.mainloop()
root=Tk()
root.title("Login Page")
canvas=Canvas(root,width=1366,height=768,highlightthickness=0)
loginpage()
