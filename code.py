appart11={"Janvier":"Payé","Fevrier":"Payé","Mars":"Payé","Avril":"Payé","Mai":"Payé","Juin":"Payé","Juillet":"Payé","Aout":"Payé","Septembre":"Payé","Octobre":"Payé","Novembre":"Payé","Decembre":"Payé"}
appart12={"Janvier":"Payé","Fevrier":"Payé","Mars":"Payé","Avril":"Payé","Mai":"Payé","Juin":"Payé","Juillet":"Payé","Aout":"Payé","Septembre":"Non Payé","Octobre":"Non Payé","Novembre":"Non Payé","Decembre":"Non Payé"}
appart21={"Janvier":"Payé","Fevrier":"Payé","Mars":"Payé","Avril":"Payé","Mai":"Payé","Juin":"Payé","Juillet":"Payé","Aout":"Payé","Septembre":"Payé","Octobre":"Payé","Novembre":"Payé","Decembre":"Payé"}
appart22={"Janvier":"Payé","Fevrier":"Payé","Mars":"Payé","Avril":"Payé","Mai":"Payé","Juin":"Payé","Juillet":"Payé","Aout":"Non Payé","Septembre":"Non Payé","Octobre":"Non Payé","Novembre":"Non Payé","Decembre":"Non Payé"}
appart31={"Janvier":"Payé","Fevrier":"Payé","Mars":"Payé","Avril":"Payé","Mai":"Payé","Juin":"Non Payé","Juillet":"Non Payé","Aout":"Non Payé","Septembre":"Non Payé","Octobre":"Non Payé","Novembre":"Non Payé","Decembre":"Non Payé"}
appart32={"Janvier":"Payé","Fevrier":"Payé","Mars":"Payé","Avril":"Payé","Mai":"Payé","Juin":"Payé","Juillet":"Payé","Aout":"Payé","Septembre":"Payé","Octobre":"Payé","Novembre":"Payé","Decembre":"Payé"}
from tkinter import *
fen=Tk()
myStyle="{arial} 20 bold"
def aff(appart1,appart2):
    if (txt1.get() == "1"):
        vf = True
        nm = 0
        for i in appart1.values():
            if i != "Payé":
                vf = False
                nm = nm + 1
        if vf == True:
            txt2.set("Payé")
            ch = ""
            for i, j in appart1.items():
                ch = ch + i + ":" + j + ","
            txt3.set(ch)
        else:
            txt2.set("Non payé et le montant a payer en DT est:")
            txt3.set(nm * 50)
    elif (txt1.get() == "2"):
        vf = True
        nm = 0
        for i in appart2.values():
            if i != "Payé":
                vf = False
                nm = nm + 1
        if vf == True:
            txt2.set("Payé")
            ch = ""
            for i, j in appart2.items():
                ch = ch + i + ":" + j + ","
            txt3.set(ch)
        else:
            txt2.set("Non payé et le montant a payer en DT est:")
            txt3.set(nm * 50)
    else:
        txt2.set("Chaque bloc contient 2 appartements")
        txt3.set("")
def afficher():
    a=vc.get()
    if(a==1):
        aff(appart11, appart12)
    if(a==2):
        aff(appart21, appart22)
    if(a==3):
        aff(appart31, appart32)
txt1=StringVar()
txt2=StringVar()
txt3=StringVar()
vc=IntVar()
fen.geometry("1400x592")
fen.title("Gestion des ressources syndicales")
ph1=PhotoImage(file="hotel.png")
l=Label(fen,image=ph1).place(x=850,y=0,width="700",height=592)
c1=Canvas(fen,bg="#1D3557").place(x=0,y=0,width="1000",height=592)
l1=Label(fen,fg="WHITE",text="Choisir le numero de bloc:",bg="#1D3557",font=myStyle).place(x=70,y=50)
r1=Radiobutton(fen,value="1",bg="#1D3557",text="Bloc 1",font=myStyle,variable=vc).place(x=110,y=100)
r2=Radiobutton(fen,value="2",bg="#1D3557",text="Bloc 2",font=myStyle,variable=vc).place(x=110,y=150)
r3=Radiobutton(fen,value="3",bg="#1D3557",text="Bloc 3",font=myStyle,variable=vc).place(x=110,y=200)
l2=Label(fen,fg="WHITE",text="Taper le numero d'appartement:",bg="#1D3557",font=myStyle).place(x=70,y=250)
t1=Entry(fen,bg="#1D3557",font=myStyle,textvariable=txt1).place(x=110,y=300,width="50",height=40)
b=Button(fen,command=afficher,fg="white",text="Affichage",bg="black",font=myStyle).place(x=110,y=350)
t2=Entry(fen,bg="#1D3557",font=myStyle,textvariable=txt2).place(x=110,y=420,width="850",height=50)
t3=Entry(fen,bg="#1D3557",font=myStyle,textvariable=txt3).place(x=110,y=470,width="850",height=50)
fen.resizable(False,False)
fen.iconbitmap("home.ico")
fen.mainloop()