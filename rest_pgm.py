from telnetlib import LOGOUT
from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import smtplib
#from PIL import ImageTk, Image
#Functions

def reset():
    textReceipt.delete(1.0,END)
    e_DalFry.set('0')
    e_roti.set('0')
    e_Veg65.set('0')
    e_Thali.set('0')
    e_DumAlu.set('0')
    e_chawal.set('0')
    e_MixVeg.set('0')
    e_paneer.set('0')
    e_kebab.set('0')

    e_Chi_Handi.set('0')
    e_Chi_Maratha.set('0')
    e_EggCury.set('0')
    e_EggBhurgy.set('0')
    e_Mut_Masala.set('0')
    e_Mut_Handi.set('0')
    e_fish.set('0')
    e_Chi_TripeRice.set('0')
    e_colNonVeg.set('0')

    e_VerginMojito.set('0')
    e_MatchaLatte.set('0')
    e_ApplePie.set('0')
    e_Sundae.set('0')
    e_Lemonade.set('0')
    e_brownie.set('0')
    e_CheeseCake.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')

    textroti.config(state=DISABLED)
    textDalFry.config(state=DISABLED)
    textVeg65.config(state=DISABLED)
    textThali.config(state=DISABLED)
    textDumAlu.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textkebab.config(state=DISABLED)
    textMixVeg.config(state=DISABLED)
    textchawal.config(state=DISABLED)

    textChi_Handi.config(state=DISABLED)
    textChi_Maratha.config(state=DISABLED)
    textMut_Handi.config(state=DISABLED)
    textEggBhurgy.config(state=DISABLED)
    textMut_Masala.config(state=DISABLED)
    textChi_TripeRice.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textEggCury.config(state=DISABLED)
    textChowmien.config(state=DISABLED)

    textMatchaLatte.config(state=DISABLED)
    textApplePie.config(state=DISABLED)
    textVerginMojito.config(state=DISABLED)
    textSundae.config(state=DISABLED)
    textLemonade.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textCheeseCake.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofNonVegvar.set('')
    costofVegvar.set('')
    costofDessertvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')




def send():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        def send_msg():
            message=textarea.get(1.0,END)+textReceipt.get(1.0,END)
            e=mailfield.get()
           #auth='woVHAjOGldMsPhnT7gS6XRIi4cYr0ym3FZkEWfKv9Qxauq8J2DHDWus7AqZKnkeXlVzQJa3fIRrp925S'
            #url='https://www.fast2sms.com/dev/bulk'

            '''params={
                'authorization':auth,
                'message':message,
                'numbers':number,
                'sender-id':'FSTSMS',5
                'route':'p',
                'language':'english'
                
            }'''
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            em=e                       
            s.login('koushikv333@gmail.com','wvhjtqituxkcrvbh')
            s.sendmail('koushikv333@gmail.com',em,message)
            messagebox.showinfo('Send Successfully','Bill sent succesfully')
            '''if e==None:
                messagebox.showinfo('message','Enter sender email')
            else:
                 messagebox.showinfo('Send Successfully','Bill sent succesfully')'''
            s.quit()
            '''response=requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')'''
            '''if s.quit()==True:
                messagebox.showinfo('Send Successfully','Message sent succesfully')

            else:
                messagebox.showerror('Error','Something went wrong')'''

        root2=Toplevel()

        root2.title("Send Bill")
        root2.config(bg='red4')
        root2.geometry('485x750+50+50')

        logoImage=PhotoImage(file='C:\SYCS\SOFTWARE COMPT\download (1).png')
        label=Label(root2,image=logoImage,bg='red4')
        label.pack(pady=5)

        # logoImage1=PhotoImage(file='C:\SYCS\SOFTWARE COMPT\My QR code.png')
        # label=Label(root2,image=logoImage1,bg='red4',height=100,width=100)
        # label.pack(pady=10,padx=50)

        emailLabel=Label(root2,text='Email-ID',font=('arial',18,'bold underline'),bg='red4',fg='white')
        emailLabel.pack(pady=5)
        
        mailfield=Entry(root2,font=('helvetica',17,'bold'),bd=3,width=30)
        mailfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        billLabel.pack(pady=5)

        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

        if costofVegvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Veg\t\t\t{priceofVeg}Rs\n')
        if costofNonVegvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of NonVeg\t\t\t{priceofNonVeg}Rs\n')
        if costofDessertvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Dessert\t\t\t{priceofDessert}Rs\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems + 50}Rs\n')

        sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE
                          ,command=send_msg)
        sendButton.pack(pady=5)
    
        root2.mainloop()


def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Succesfully Saved')

def receipt():
    global billnumber,date
    if costofVegvar.get() != '' or costofDessertvar.get() != '' or costofNonVegvar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END,'***************************************************************\n')
        if e_roti.get()!='0':
            textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')

        if e_DalFry.get()!='0':
            textReceipt.insert(END,f'DalFry\t\t\t{int(e_DalFry.get())*120}\n\n')

        if e_Thali.get()!='0':
            textReceipt.insert(END,f'Thali\t\t\t{int(e_Thali.get())*210}\n\n')

        if e_chawal.get() != '0':
            textReceipt.insert(END, f'Chawal:\t\t\t{int(e_chawal.get()) * 60}\n\n')

        if e_Veg65.get() != '0':
            textReceipt.insert(END, f'Veg65:\t\t\t{int(e_Veg65.get()) * 175}\n\n')

        if e_paneer.get() != '0':
            textReceipt.insert(END, f'Paneer:\t\t\t{int(e_paneer.get()) * 150}\n\n')

        if e_DumAlu.get() != '0':
            textReceipt.insert(END, f'DumAlu:\t\t\t{int(e_DumAlu.get()) * 125}\n\n')

        if e_kebab.get() != '0':
            textReceipt.insert(END, f'kebab:\t\t\t{int(e_kebab.get()) * 180}\n\n')

        if e_MixVeg.get() != '0':
            textReceipt.insert(END, f'MixVeg:\t\t\t{int(e_MixVeg.get()) * 165}\n\n')

        if e_Chi_Handi.get() != '0':
            textReceipt.insert(END, f'Chi_Handi:\t\t\t{int(e_Chi_Handi.get()) * 210}\n\n')

        if e_Chi_Maratha.get() != '0':
            textReceipt.insert(END, f'Chi_Maratha:\t\t\t{int(e_Chi_Maratha.get()) * 230}\n\n')

        if e_EggCury.get() != '0':
            textReceipt.insert(END, f'EggCury:\t\t\t{int(e_EggCury.get()) * 125}\n\n')

        if e_Mut_Masala.get() != '0':
            textReceipt.insert(END, f'Mut_Masala:\t\t\t{int(e_Mut_Masala.get()) * 230}\n\n')

        if e_Mut_Handi.get() != '0':
            textReceipt.insert(END, f'Mut_Handi:\t\t\t{int(e_Mut_Handi.get()) * 230}\n\n')

        if e_EggBhurgy.get() != '0':
            textReceipt.insert(END, f'EggBhurgy:\t\t\t{int(e_EggBhurgy.get()) * 80}\n\n')

        if e_fish.get() != '0':
            textReceipt.insert(END, f'Fish Fry:\t\t\t{int(e_fish.get()) * 240}\n\n')

        if e_Chi_TripeRice.get() != '0':
            textReceipt.insert(END, f'Chi_TripeRice:\t\t\t{int(e_Chi_TripeRice.get()) * 90}\n\n')

        if e_colNonVeg.get() != '0':
            textReceipt.insert(END, f'Chowmien:\t\t\t{int(e_colNonVeg.get()) * 80}\n\n')

        if e_MatchaLatte.get() != '0':
            textReceipt.insert(END, f'MatchaLatte:\t\t\t{int(e_MatchaLatte.get()) * 280}\n\n')

        if e_ApplePie.get() != '0':
            textReceipt.insert(END, f'ApplePie:\t\t\t{int(e_ApplePie.get()) * 300}\n\n')

        if e_VerginMojito.get() != '0':
            textReceipt.insert(END, f'VerginMojito:\t\t\t{int(e_VerginMojito.get()) * 279}\n\n')

        if e_Lemonade.get() != '0':
            textReceipt.insert(END, f'Lemonade:\t\t\t{int(e_Lemonade.get()) * 169}\n\n')

        if e_brownie.get() != '0':
            textReceipt.insert(END, f'Brownie:\t\t\t{int(e_brownie.get()) * 129}\n\n')

        if e_CheeseCake.get() != '0':
            textReceipt.insert(END, f'CheeseCake:\t\t\t{int(e_CheeseCake.get()) * 349}\n\n')

        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate:\t\t\t{int(e_chocolate.get()) * 120}\n\n')

        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 550}\n\n')

        if e_Sundae.get() != '0':
            textReceipt.insert(END, f'Sundae:\t\t\t{int(e_Sundae.get()) * 600}\n\n')

        textReceipt.insert(END,'***************************************************************\n')
        if costofVegvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost Of Veg\t\t\t{priceofVeg}Rs\n\n')
        if costofNonVegvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of NonVeg\t\t\t{priceofNonVeg}Rs\n\n')
        if costofDessertvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Dessert\t\t\t{priceofDessert}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
        textReceipt.insert(END,'***************************************************************\n')

    else:
        messagebox.showerror('Error','No Item Is selected')



def totalcost():
    global priceofVeg,priceofNonVeg,priceofDessert,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_roti.get())
        item2=int(e_DalFry.get())
        item3=int(e_Thali.get())
        item4 = int(e_Veg65.get())
        item5 = int(e_DumAlu.get())
        item6 = int(e_chawal.get())
        item7 = int(e_MixVeg.get())
        item8 = int(e_paneer.get())
        item9 = int(e_kebab.get())

        item10 = int(e_Chi_Handi.get())
        item11 = int(e_Chi_Maratha.get())
        item12 = int(e_EggCury.get())
        item13 = int(e_Mut_Masala.get())
        item14 = int(e_Mut_Handi.get())
        item15 = int(e_EggBhurgy.get())
        item16 = int(e_fish.get())
        item17 = int(e_Chi_TripeRice.get())
        item18 = int(e_colNonVeg.get())

        item19 = int(e_MatchaLatte.get())
        item20 = int(e_ApplePie.get())
        item21 = int(e_VerginMojito.get())
        item22 = int(e_Sundae.get())
        item23 = int(e_Lemonade.get())
        item24 = int(e_brownie.get())
        item25 = int(e_CheeseCake.get())
        item26 = int(e_chocolate.get())
        item27 = int(e_blackforest.get())

        priceofVeg=(item1*10)+(item2*120)+(item3*210)+(item4*60)+ (item5*175) + (item6*150) + (item7*125) \
                    + (item8*180) + (item9*165)

        priceofNonVeg=(item10*210)+(item11*230)+ (item12*125) + (item13*230) + (item14*230) + (item15*80) \
                      + (item16*240) + (item17*90) + (item18*80)

        priceofDessert=(item19*280)+(item20*300)+ (item21*279) + (item22*169) + (item23*129) + (item24*349) \
                     + (item25*120) + (item26*550) + (item27*600)

        costofVegvar.set(str(priceofVeg)+ ' Rs')
        costofNonVegvar.set(str(priceofNonVeg)+ ' Rs')
        costofDessertvar.set(str(priceofDessert)+ ' Rs')

        subtotalofItems=priceofVeg+priceofNonVeg+priceofDessert
        subtotalvar.set(str(subtotalofItems)+' Rs')

        servicetaxvar.set('50 Rs')

        tottalcost=subtotalofItems+50
        totalcostvar.set(str(tottalcost)+' Rs')

    else:
        messagebox.showerror('Error','No Item Is selected')



def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def DalFry():
    if var2.get()==1:
        textDalFry.config(state=NORMAL)
        textDalFry.delete(0,END)
        textDalFry.focus()

    else:
        textDalFry.config(state=DISABLED)
        e_DalFry.set('0')

def Thali():
    if var3.get()==1:
        textThali.config(state=NORMAL)
        textThali.delete(0,END)
        textThali.focus()

    else:
        textThali.config(state=DISABLED)
        e_Thali.set('0')

def Veg65():
    if var4.get() == 1:
        textVeg65.config(state=NORMAL)
        textVeg65.focus()
        textVeg65.delete(0, END)
    elif var4.get() == 0:
        textVeg65.config(state=DISABLED)
        e_Veg65.set('0')


def DumAlu():
    if var5.get() == 1:
        textDumAlu.config(state=NORMAL)
        textDumAlu.focus()
        textDumAlu.delete(0, END)
    elif var5.get() == 0:
        textDumAlu.config(state=DISABLED)
        e_DumAlu.set('0')


def chawal():
    if var6.get() == 1:
        textchawal.config(state=NORMAL)
        textchawal.focus()
        textchawal.delete(0, END)
    elif var6.get() == 0:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')


def MixVeg():
    if var7.get() == 1:
        textMixVeg.config(state=NORMAL)
        textMixVeg.focus()
        textMixVeg.delete(0, END)
    elif var7.get() == 0:
        textMixVeg.config(state=DISABLED)
        e_MixVeg.set('0')


def paneer():
    if var8.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.focus()
        textpaneer.delete(0, END)
    elif var8.get() == 0:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')


def kebab():
    if var9.get() == 1:
        textkebab.config(state=NORMAL)
        textkebab.focus()
        textkebab.delete(0, END)
    elif var9.get() == 0:
        textkebab.config(state=DISABLED)
        e_kebab.set('0')


def Chi_Handi():
    if var10.get() == 1:
        textChi_Handi.config(state=NORMAL)
        textChi_Handi.focus()
        textChi_Handi.delete(0, END)
    elif var10.get() == 0:
        textChi_Handi.config(state=DISABLED)
        e_Chi_Handi.set('0')


def Chi_Maratha():
    if var11.get() == 1:
        textChi_Maratha.config(state=NORMAL)
        textChi_Maratha.focus()
        textChi_Maratha.delete(0, END)
    elif var11.get() == 0:
        textChi_Maratha.config(state=DISABLED)
        e_Chi_Maratha.set('0')


def EggCury():
    if var12.get() == 1:
        textEggCury.config(state=NORMAL)
        textEggCury.focus()
        textEggCury.delete(0, END)
    elif var12.get() == 0:
        textEggCury.config(state=DISABLED)
        e_EggCury.set('0')


def Mut_Masala():
    if var13.get() == 1:
        textMut_Masala.config(state=NORMAL)
        textMut_Masala.focus()
        textMut_Masala.delete(0, END)
    elif var13.get() == 0:
        textMut_Masala.config(state=DISABLED)
        e_Mut_Masala.set('0')


def Mut_Handi():
    if var14.get() == 1:
        textMut_Handi.config(state=NORMAL)
        textMut_Handi.focus()
        textMut_Handi.delete(0, END)
    elif var14.get() == 0:
        textMut_Handi.config(state=DISABLED)
        e_Mut_Handi.set('0')


def EggBhurgy():
    if var15.get() == 1:
        textEggBhurgy.config(state=NORMAL)
        textEggBhurgy.focus()
        textEggBhurgy.delete(0, END)
    elif var15.get() == 0:
        textEggBhurgy.config(state=DISABLED)
        e_EggBhurgy.set('0')


def fish():
    if var16.get() == 1:
        textfish.config(state=NORMAL)
        textfish.focus()
        textfish.delete(0, END)
    elif var16.get() == 0:
        textfish.config(state=DISABLED)
        e_fish.set('0')


def Chi_TripeRice():
    if var17.get() == 1:
        textChi_TripeRice.config(state=NORMAL)
        textChi_TripeRice.focus()
        textChi_TripeRice.delete(0, END)
    elif var17.get() == 0:
        textChi_TripeRice.config(state=DISABLED)
        e_Chi_TripeRice.set('0')


def Chowmien():
    if var18.get() == 1:
        textChowmien.config(state=NORMAL)
        textChowmien.focus()
        textChowmien.delete(0, END)
    elif var18.get() == 0:
        textChowmien.config(state=DISABLED)
        e_colNonVeg.set('0')


def MatchaLatte():
    if var19.get() == 1:
        textMatchaLatte.config(state=NORMAL)
        textMatchaLatte.focus()
        textMatchaLatte.delete(0, END)
    elif var19.get() == 0:
        textMatchaLatte.config(state=DISABLED)
        e_MatchaLatte.set('0')


def ApplePie():
    if var20.get() == 1:
        textApplePie.config(state=NORMAL)
        textApplePie.focus()
        textApplePie.delete(0, END)
    elif var20.get() == 0:
        textApplePie.config(state=DISABLED)
        e_ApplePie.set('0')


def VerginMojito():
    if var21.get() == 1:
        textVerginMojito.config(state=NORMAL)
        textVerginMojito.focus()
        textVerginMojito.delete(0, END)
    elif var21.get() == 0:
        textVerginMojito.config(state=DISABLED)
        e_VerginMojito.set('0')


def Sundae():
    if var22.get() == 1:
        textSundae.config(state=NORMAL)
        textSundae.focus()
        textSundae.delete(0, END)
    elif var22.get() == 0:
        textSundae.config(state=DISABLED)
        e_Sundae.set('0')


def Lemonade():
    if var23.get() == 1:
        textLemonade.config(state=NORMAL)
        textLemonade.focus()
        textLemonade.delete(0, END)
    elif var23.get() == 0:
        textLemonade.config(state=DISABLED)
        e_Lemonade.set('0')


def brownie():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.focus()
        textbrownie.delete(0, END)
    elif var24.get() == 0:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')


def CheeseCake():
    if var25.get() == 1:
        textCheeseCake.config(state=NORMAL)
        textCheeseCake.focus()
        textCheeseCake.delete(0, END)
    elif var25.get() == 0:
        textCheeseCake.config(state=DISABLED)
        e_CheeseCake.set('0')


def chocolate():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.focus()
        textchocolate.delete(0, END)
    elif var26.get() == 0:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')


def blackforest():
    if var27.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.focus()
        textblackforest.delete(0, END)
    elif var27.get() == 0:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')



root=Tk()

root.geometry('1290x690+0+0')

root.resizable(0,0)

root.title('RESTAURANT MANAGEMENT SYSTEM')

root.config(bg='firebrick4')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='black')
topFrame.pack(side=TOP)




labelTitle=Label(topFrame,text='Indian Cuisine',font=('Lobster',30,'bold'),fg='red',bd=9,
                 bg='orange',width=52)
labelTitle.grid(row=0,column=0)
#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='black')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='white',pady=8)
costFrame.pack(side=BOTTOM)

VegFrame=LabelFrame(menuFrame,text='Veg',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
VegFrame.pack(side=LEFT)

NonVegFrame=LabelFrame(menuFrame,text='NonVeg',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
NonVegFrame.pack(side=LEFT)

DessertFrame=LabelFrame(menuFrame,text='Dessert',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
DessertFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

#Variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_roti=StringVar()
e_DalFry=StringVar()
e_Veg65 = StringVar()
e_chawal = StringVar()
e_Thali = StringVar()
e_MixVeg = StringVar()
e_DumAlu = StringVar()
e_kebab = StringVar()
e_paneer = StringVar()

e_Chi_Handi=StringVar()
e_Chi_Maratha = StringVar()
e_EggCury = StringVar()
e_Mut_Masala = StringVar()
e_EggBhurgy = StringVar()
e_Mut_Handi = StringVar()
e_fish = StringVar()
e_Chi_TripeRice = StringVar()
e_colNonVeg = StringVar()

e_MatchaLatte=StringVar()
e_VerginMojito = StringVar()
e_Sundae = StringVar()
e_ApplePie = StringVar()
e_blackforest = StringVar()
e_Lemonade = StringVar()
e_brownie = StringVar()
e_CheeseCake = StringVar()
e_chocolate = StringVar()

costofVegvar=StringVar()
costofNonVegvar=StringVar()
costofDessertvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

e_roti.set('0')
e_DalFry.set('0')
e_Veg65.set('0')
e_Thali.set('0')
e_DumAlu.set('0')
e_chawal.set('0')
e_MixVeg.set('0')
e_kebab.set('0')
e_paneer.set('0')

e_Chi_Handi.set('0')
e_Chi_Maratha.set('0')
e_EggCury.set('0')
e_EggBhurgy.set('0')
e_Mut_Masala.set('0')
e_Mut_Handi.set('0')
e_fish.set('0')
e_Chi_TripeRice.set('0')
e_colNonVeg.set('0')

e_VerginMojito.set('0')
e_Lemonade.set('0')
e_CheeseCake.set('0')
e_ApplePie.set('0')
e_chocolate.set('0')
e_MatchaLatte.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_Sundae.set('0')

##Veg

roti=Checkbutton(VegFrame,text='Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1
                 ,command=roti)
roti.grid(row=0,column=0,sticky=W)

DalFry=Checkbutton(VegFrame,text='DalFry',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2
                 ,command=DalFry)
DalFry.grid(row=1,column=0,sticky=W)

Thali=Checkbutton(VegFrame,text='Thali',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3
                 ,command=Thali)
Thali.grid(row=2,column=0,sticky=W)

Veg65=Checkbutton(VegFrame,text='Veg65',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4
                  ,command=Veg65)
Veg65.grid(row=3,column=0,sticky=W)

DumAlu=Checkbutton(VegFrame,text='DumAlu',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5
                  ,command=DumAlu)
DumAlu.grid(row=4,column=0,sticky=W)

chawal=Checkbutton(VegFrame,text='Chawal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6
                   ,command=chawal)
chawal.grid(row=5,column=0,sticky=W)

MixVeg=Checkbutton(VegFrame,text='MixVeg',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,
                   command=MixVeg)
MixVeg.grid(row=6,column=0,sticky=W)

paneer=Checkbutton(VegFrame,text='Paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8
                   ,command=paneer)
paneer.grid(row=7,column=0,sticky=W)

kebab=Checkbutton(VegFrame,text='kebab',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9
                    ,command=kebab)
kebab.grid(row=8,column=0,sticky=W)

#Entry Fields for Veg Items

textroti=Entry(VegFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textDalFry=Entry(VegFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_DalFry)
textDalFry.grid(row=1,column=1)

textThali=Entry(VegFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_Thali)
textThali.grid(row=2,column=1)

textVeg65 = Entry(VegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Veg65)
textVeg65.grid(row=3, column=1)

textDumAlu = Entry(VegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_DumAlu)
textDumAlu.grid(row=4, column=1)

textchawal = Entry(VegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chawal)
textchawal.grid(row=5, column=1)

textMixVeg = Entry(VegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_MixVeg)
textMixVeg.grid(row=6, column=1)

textpaneer = Entry(VegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_paneer)
textpaneer.grid(row=7, column=1)

textkebab = Entry(VegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kebab)
textkebab.grid(row=8, column=1)

#NonVeg

Chi_Handi=Checkbutton(NonVegFrame,text='Chi_Handi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10
                  ,command=Chi_Handi)
Chi_Handi.grid(row=0,column=0,sticky=W)

Chi_Maratha=Checkbutton(NonVegFrame,text='Chi_Maratha',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11
                   ,command=Chi_Maratha)
Chi_Maratha.grid(row=1,column=0,sticky=W)

EggCury=Checkbutton(NonVegFrame,text='EggCury',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12
                   ,command=EggCury)
EggCury.grid(row=2,column=0,sticky=W)

Mut_Masala=Checkbutton(NonVegFrame,text='Mut_Masala',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13
                     ,command=Mut_Masala)
Mut_Masala.grid(row=3,column=0,sticky=W)

Mut_Handi=Checkbutton(NonVegFrame,text='Mut_Handi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14
                     ,command=Mut_Handi)
Mut_Handi.grid(row=4,column=0,sticky=W)

EggBhurgy=Checkbutton(NonVegFrame,text='EggBhurgy',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15
                     ,command=EggBhurgy)
EggBhurgy.grid(row=5,column=0,sticky=W)

fish=Checkbutton(NonVegFrame,text='Fish Fry',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16
                      ,command=fish)
fish.grid(row=6,column=0,sticky=W)

Chi_TripeRice=Checkbutton(NonVegFrame,text='Chi_TripeRice',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17
                      ,command=Chi_TripeRice)
Chi_TripeRice.grid(row=7,column=0,sticky=W)

Chowmien=Checkbutton(NonVegFrame,text='Chowmien',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18
                       ,command=Chowmien)
Chowmien.grid(row=8,column=0,sticky=W)

#entry fields for drink items

textChi_Handi = Entry(NonVegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Chi_Handi)
textChi_Handi.grid(row=0, column=1)

textChi_Maratha = Entry(NonVegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Chi_Maratha)
textChi_Maratha.grid(row=1, column=1)

textEggCury = Entry(NonVegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_EggCury)
textEggCury.grid(row=2, column=1)

textMut_Masala = Entry(NonVegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Mut_Masala)
textMut_Masala.grid(row=3, column=1)

textMut_Handi = Entry(NonVegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Mut_Handi)
textMut_Handi.grid(row=4, column=1)

textEggBhurgy = Entry(NonVegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_EggBhurgy)
textEggBhurgy.grid(row=5, column=1)

textfish = Entry(NonVegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_fish)
textfish.grid(row=6, column=1)

textChi_TripeRice = Entry(NonVegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Chi_TripeRice)
textChi_TripeRice.grid(row=7, column=1)

textChowmien = Entry(NonVegFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_colNonVeg)
textChowmien.grid(row=8, column=1)

#Dessert

MatchaLattecake=Checkbutton(DessertFrame,text='MatchaLatte',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19
                     ,command=MatchaLatte)
MatchaLattecake.grid(row=0,column=0,sticky=W)

ApplePiecake=Checkbutton(DessertFrame,text='ApplePie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20
                      ,command=ApplePie)
ApplePiecake.grid(row=1,column=0,sticky=W)

VerginMojitocake=Checkbutton(DessertFrame,text='VerginMojito',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21
                       ,command=VerginMojito)
VerginMojitocake.grid(row=2,column=0,sticky=W)

Sundaecake=Checkbutton(DessertFrame,text='Sundae',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22
                        ,command=Sundae)
Sundaecake.grid(row=3,column=0,sticky=W)

Lemonadecake=Checkbutton(DessertFrame,text='Lemonade',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23
                       ,command=Lemonade)
Lemonadecake.grid(row=4,column=0,sticky=W)

browniecake=Checkbutton(DessertFrame,text='Brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24
                        ,command=brownie)
browniecake.grid(row=5,column=0,sticky=W)

CheeseCakecake=Checkbutton(DessertFrame,text='CheeseCake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25
                          ,command=CheeseCake)
CheeseCakecake.grid(row=6,column=0,sticky=W)

chocolatecake=Checkbutton(DessertFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26
                          ,command=chocolate)
chocolatecake.grid(row=7,column=0,sticky=W)

blackforestcake=Checkbutton(DessertFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27
                            ,command=blackforest)
blackforestcake.grid(row=8,column=0,sticky=W)

#entry fields for Dessert

textMatchaLatte = Entry(DessertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_MatchaLatte)
textMatchaLatte.grid(row=0, column=1)

textApplePie = Entry(DessertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_ApplePie)
textApplePie.grid(row=1, column=1)

textVerginMojito = Entry(DessertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_VerginMojito)
textVerginMojito.grid(row=2, column=1)

textSundae = Entry(DessertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Sundae)
textSundae.grid(row=3, column=1)

textLemonade = Entry(DessertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_Lemonade)
textLemonade.grid(row=4, column=1)

textbrownie = Entry(DessertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=5, column=1)

textCheeseCake = Entry(DessertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_CheeseCake)
textCheeseCake.grid(row=6, column=1)

textchocolate = Entry(DessertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chocolate)
textchocolate.grid(row=7, column=1)

textblackforest = Entry(DessertFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8, column=1)

#costlabels & entry fields

labelCostofVeg=Label(costFrame,text='Cost of Veg',font=('arial',16,'bold'),bg="white",fg='black')
labelCostofVeg.grid(row=0,column=0)

textCostofVeg=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofVegvar)
textCostofVeg.grid(row=0,column=1,padx=41)

labelCostofNonVeg=Label(costFrame,text='Cost of NonVeg',font=('arial',16,'bold'),bg='white',fg='black')
labelCostofNonVeg.grid(row=1,column=0)

textCostofNonVeg=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofNonVegvar)
textCostofNonVeg.grid(row=1,column=1,padx=41)

labelCostofDessert=Label(costFrame,text='Cost of Dessert',font=('arial',16,'bold'),bg='white',fg='black')
labelCostofDessert.grid(row=2,column=0)

textCostofDessert=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofDessertvar)
textCostofDessert.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='white',fg='black')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='white',fg='black')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='white',fg='black')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5
                     ,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5
                  ,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                   command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#Calculator
operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator='white'
def log_out():
    messagebox.showinfo(' Admin message', 'Logging Out!!!Byyee')
    root.destroy()
    import rest_login_page
calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
                  ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
                   ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
                  ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='black',bg='green1',bd=6,width=6,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='black',bg='green1',bd=6,width=6
                   ,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='LogOut',font=('arial',16,'bold'),fg='yellow',bg='red',bd=6,width=6,
                command=log_out)#command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()

















'''from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import smtplib
from PIL import ImageTk, Image
#Functions

def reset():
    textReceipt.delete(1.0,END)
    e_daal.set('0')
    e_roti.set('0')
    e_sabji.set('0')
    e_fish.set('0')
    e_kebab.set('0')
    e_chawal.set('0')
    e_mutton.set('0')
    e_paneer.set('0')
    e_chicken.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_roohafza.set('0')
    e_shikanji.set('0')
    e_jaljeera.set('0')
    e_masalatea.set('0')
    e_badammilk.set('0')
    e_coldrinks.set('0')

    e_kitkat.set('0')
    e_oreo.set('0')
    e_apple.set('0')
    e_vanilla.set('0')
    e_banana.set('0')
    e_brownie.set('0')
    e_pineapple.set('0')
    e_chocolate.set('0')
    e_blackforest.set('0')

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textkebab.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textchawal.config(state=DISABLED)

    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textmasalatea.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textcolddrinks.config(state=DISABLED)

    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textblackforest.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')




def send():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        def send_msg():
            message=textarea.get(1.0,END)+textReceipt.get(1.0,END)
            e=mailfield.get()
           #auth='woVHAjOGldMsPhnT7gS6XRIi4cYr0ym3FZkEWfKv9Qxauq8J2DHDWus7AqZKnkeXlVzQJa3fIRrp925S'
            #url='https://www.fast2sms.com/dev/bulk'

            params={
                'authorization':auth,
                'message':message,
                'numbers':number,
                'sender-id':'FSTSMS',
                'route':'p',
                'language':'english'
                
            }
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            em=e                       
            s.login('koushikv333@gmail.com','wvhjtqituxkcrvbh')
            s.sendmail('koushikv333@gmail.com',em,message)
           #messagebox.showinfo('Send Successfully','Bill sent succesfully')
            if e==None:
                messagebox.showinfo('message','Enter sender email')
            else:
                 messagebox.showinfo('Send Successfully','Bill sent succesfully')
            s.quit()
            response=requests.get(url,params=params)
            dic=response.json()
            result=dic.get('return')
            if s.quit()==True:
                messagebox.showinfo('Send Successfully','Message sent succesfully')

            else:
                messagebox.showerror('Error','Something went wrong')

        root2=Toplevel()

        root2.title("Send Bill")
        root2.config(bg='red4')
        root2.geometry('485x800+50+50')

        logoImage=PhotoImage(file='C:\SYCS\SOFTWARE COMPT\download (1).png')
        label=Label(root2,image=logoImage,bg='red4')
        label.pack(pady=5)

        emailLabel=Label(root2,text='Email-ID',font=('arial',18,'bold underline'),bg='red4',fg='white')
        emailLabel.pack(pady=5)
        
        mailfield=Entry(root2,font=('helvetica',17,'bold'),bd=3,width=30)
        mailfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        billLabel.pack(pady=5)

        textarea=Text(root2,font=('arial',12,'bold'),bd=3,width=42,height=14)
        textarea.pack(pady=5)
        textarea.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n\n')

        if costoffoodvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n')
        if costofdrinksvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')
        if costofcakesvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalofItems + 50}Rs\n')

        sendButton=Button(root2,text='SEND',font=('arial',19,'bold'),bg='white',fg='red4',bd=7,relief=GROOVE
                          ,command=send_msg)
        sendButton.pack(pady=5)
    
        root2.mainloop()


def save():
    if textReceipt.get(1.0,END)=='\n':
        pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
            pass
        else:

            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Succesfully Saved')

def receipt():
    global billnumber,date
    if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0,END)
        x=random.randint(100,10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%Y')
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'***************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END,'***************************************************************\n')
        if e_roti.get()!='0':
            textReceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')

        if e_daal.get()!='0':
            textReceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*60}\n\n')

        if e_fish.get()!='0':
            textReceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*100}\n\n')

        if e_chawal.get() != '0':
            textReceipt.insert(END, f'Chawal:\t\t\t{int(e_chawal.get()) * 30}\n\n')

        if e_sabji.get() != '0':
            textReceipt.insert(END, f'Sabji:\t\t\t{int(e_sabji.get()) * 50}\n\n')

        if e_paneer.get() != '0':
            textReceipt.insert(END, f'Paneer:\t\t\t{int(e_paneer.get()) * 100}\n\n')

        if e_kebab.get() != '0':
            textReceipt.insert(END, f'Kebab:\t\t\t{int(e_kebab.get()) * 40}\n\n')

        if e_chicken.get() != '0':
            textReceipt.insert(END, f'Chicken:\t\t\t{int(e_chicken.get()) * 120}\n\n')

        if e_mutton.get() != '0':
            textReceipt.insert(END, f'Mutton:\t\t\t{int(e_mutton.get()) * 120}\n\n')

        if e_lassi.get() != '0':
            textReceipt.insert(END, f'Lassi:\t\t\t{int(e_lassi.get()) * 50}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee:\t\t\t{int(e_coffee.get()) * 40}\n\n')

        if e_faluda.get() != '0':
            textReceipt.insert(END, f'Faluda:\t\t\t{int(e_faluda.get()) * 80}\n\n')

        if e_shikanji.get() != '0':
            textReceipt.insert(END, f'Shikanji:\t\t\t{int(e_shikanji.get()) * 30}\n\n')

        if e_jaljeera.get() != '0':
            textReceipt.insert(END, f'Jaljeera:\t\t\t{int(e_jaljeera.get()) * 40}\n\n')

        if e_roohafza.get() != '0':
            textReceipt.insert(END, f'Roohafza:\t\t\t{int(e_roohafza.get()) * 60}\n\n')

        if e_masalatea.get() != '0':
            textReceipt.insert(END, f'Masala Chai:\t\t\t{int(e_masalatea.get()) * 20}\n\n')

        if e_badammilk.get() != '0':
            textReceipt.insert(END, f'Badam Milk:\t\t\t{int(e_badammilk.get()) * 50}\n\n')

        if e_coldrinks.get() != '0':
            textReceipt.insert(END, f'Cold Drinks:\t\t\t{int(e_coldrinks.get()) * 80}\n\n')

        if e_oreo.get() != '0':
            textReceipt.insert(END, f'Oreo:\t\t\t{int(e_oreo.get()) * 350}\n\n')

        if e_apple.get() != '0':
            textReceipt.insert(END, f'Apple:\t\t\t{int(e_apple.get()) * 300}\n\n')

        if e_kitkat.get() != '0':
            textReceipt.insert(END, f'Kitkat:\t\t\t{int(e_kitkat.get()) * 500}\n\n')

        if e_banana.get() != '0':
            textReceipt.insert(END, f'Banana:\t\t\t{int(e_banana.get()) * 450}\n\n')

        if e_brownie.get() != '0':
            textReceipt.insert(END, f'Brownie:\t\t\t{int(e_brownie.get()) * 400}\n\n')

        if e_pineapple.get() != '0':
            textReceipt.insert(END, f'Pineapple:\t\t\t{int(e_pineapple.get()) * 300}\n\n')

        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate:\t\t\t{int(e_chocolate.get()) * 550}\n\n')

        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 550}\n\n')

        if e_vanilla.get() != '0':
            textReceipt.insert(END, f'Vanilla:\t\t\t{int(e_vanilla.get()) * 550}\n\n')

        textReceipt.insert(END,'***************************************************************\n')
        if costoffoodvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costofcakesvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
        textReceipt.insert(END,'***************************************************************\n')

    else:
        messagebox.showerror('Error','No Item Is selected')



def totalcost():
    global priceofFood,priceofDrinks,priceofCakes,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_roti.get())
        item2=int(e_daal.get())
        item3=int(e_fish.get())
        item4 = int(e_sabji.get())
        item5 = int(e_kebab.get())
        item6 = int(e_chawal.get())
        item7 = int(e_mutton.get())
        item8 = int(e_paneer.get())
        item9 = int(e_chicken.get())

        item10 = int(e_lassi.get())
        item11 = int(e_coffee.get())
        item12 = int(e_faluda.get())
        item13 = int(e_shikanji.get())
        item14 = int(e_jaljeera.get())
        item15 = int(e_roohafza.get())
        item16 = int(e_masalatea.get())
        item17 = int(e_badammilk.get())
        item18 = int(e_coldrinks.get())

        item19 = int(e_oreo.get())
        item20 = int(e_apple.get())
        item21 = int(e_kitkat.get())
        item22 = int(e_vanilla.get())
        item23 = int(e_banana.get())
        item24 = int(e_brownie.get())
        item25 = int(e_pineapple.get())
        item26 = int(e_chocolate.get())
        item27 = int(e_blackforest.get())

        priceofFood=(item1*10)+(item2*60)+(item3*100)+(item4*50)+ (item5*40) + (item6 * 30) + (item7 * 120) \
                    + (item8 * 100) + (item9 * 120)

        priceofDrinks=(item10*50)+(item11*40)+ (item12 * 80) + (item13 * 30) + (item14 * 40) + (item15 * 60) \
                      + (item16 * 20) + (item17 * 50) + (item18 * 80)

        priceofCakes=(item19*400)+(item20*300)+ (item21 * 500) + (item22 * 550) + (item23 * 450) + (item24 * 800) \
                     + (item25 * 620) + (item26 * 700) + (item27 * 550)

        costoffoodvar.set(str(priceofFood)+ ' Rs')
        costofdrinksvar.set(str(priceofDrinks)+ ' Rs')
        costofcakesvar.set(str(priceofCakes)+ ' Rs')

        subtotalofItems=priceofFood+priceofDrinks+priceofCakes
        subtotalvar.set(str(subtotalofItems)+' Rs')

        servicetaxvar.set('50 Rs')

        tottalcost=subtotalofItems+50
        totalcostvar.set(str(tottalcost)+' Rs')

    else:
        messagebox.showerror('Error','No Item Is selected')



def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def daal():
    if var2.get()==1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0,END)
        textdaal.focus()

    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def fish():
    if var3.get()==1:
        textfish.config(state=NORMAL)
        textfish.delete(0,END)
        textfish.focus()

    else:
        textfish.config(state=DISABLED)
        e_fish.set('0')

def sabji():
    if var4.get() == 1:
        textsabji.config(state=NORMAL)
        textsabji.focus()
        textsabji.delete(0, END)
    elif var4.get() == 0:
        textsabji.config(state=DISABLED)
        e_sabji.set('0')


def kebab():
    if var5.get() == 1:
        textkebab.config(state=NORMAL)
        textkebab.focus()
        textkebab.delete(0, END)
    elif var5.get() == 0:
        textkebab.config(state=DISABLED)
        e_kebab.set('0')


def chawal():
    if var6.get() == 1:
        textchawal.config(state=NORMAL)
        textchawal.focus()
        textchawal.delete(0, END)
    elif var6.get() == 0:
        textchawal.config(state=DISABLED)
        e_chawal.set('0')


def mutton():
    if var7.get() == 1:
        textmutton.config(state=NORMAL)
        textmutton.focus()
        textmutton.delete(0, END)
    elif var7.get() == 0:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')


def paneer():
    if var8.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.focus()
        textpaneer.delete(0, END)
    elif var8.get() == 0:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')


def chicken():
    if var9.get() == 1:
        textchicken.config(state=NORMAL)
        textchicken.focus()
        textchicken.delete(0, END)
    elif var9.get() == 0:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')


def lassi():
    if var10.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.focus()
        textlassi.delete(0, END)
    elif var10.get() == 0:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')


def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.focus()
        textcoffee.delete(0, END)
    elif var11.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')


def faluda():
    if var12.get() == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.focus()
        textfaluda.delete(0, END)
    elif var12.get() == 0:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')


def shikanji():
    if var13.get() == 1:
        textshikanji.config(state=NORMAL)
        textshikanji.focus()
        textshikanji.delete(0, END)
    elif var13.get() == 0:
        textshikanji.config(state=DISABLED)
        e_shikanji.set('0')


def jaljeera():
    if var14.get() == 1:
        textjaljeera.config(state=NORMAL)
        textjaljeera.focus()
        textjaljeera.delete(0, END)
    elif var14.get() == 0:
        textjaljeera.config(state=DISABLED)
        e_jaljeera.set('0')


def roohafza():
    if var15.get() == 1:
        textroohafza.config(state=NORMAL)
        textroohafza.focus()
        textroohafza.delete(0, END)
    elif var15.get() == 0:
        textroohafza.config(state=DISABLED)
        e_roohafza.set('0')


def masalatea():
    if var16.get() == 1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.focus()
        textmasalatea.delete(0, END)
    elif var16.get() == 0:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')


def badammilk():
    if var17.get() == 1:
        textbadammilk.config(state=NORMAL)
        textbadammilk.focus()
        textbadammilk.delete(0, END)
    elif var17.get() == 0:
        textbadammilk.config(state=DISABLED)
        e_badammilk.set('0')


def colddrinks():
    if var18.get() == 1:
        textcolddrinks.config(state=NORMAL)
        textcolddrinks.focus()
        textcolddrinks.delete(0, END)
    elif var18.get() == 0:
        textcolddrinks.config(state=DISABLED)
        e_coldrinks.set('0')


def oreo():
    if var19.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
    elif var19.get() == 0:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')


def apple():
    if var20.get() == 1:
        textapple.config(state=NORMAL)
        textapple.focus()
        textapple.delete(0, END)
    elif var20.get() == 0:
        textapple.config(state=DISABLED)
        e_apple.set('0')


def kitkat():
    if var21.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.focus()
        textkitkat.delete(0, END)
    elif var21.get() == 0:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')


def vanilla():
    if var22.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.focus()
        textvanilla.delete(0, END)
    elif var22.get() == 0:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')


def banana():
    if var23.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.focus()
        textbanana.delete(0, END)
    elif var23.get() == 0:
        textbanana.config(state=DISABLED)
        e_banana.set('0')


def brownie():
    if var24.get() == 1:
        textbrownie.config(state=NORMAL)
        textbrownie.focus()
        textbrownie.delete(0, END)
    elif var24.get() == 0:
        textbrownie.config(state=DISABLED)
        e_brownie.set('0')


def pineapple():
    if var25.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.focus()
        textpineapple.delete(0, END)
    elif var25.get() == 0:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')


def chocolate():
    if var26.get() == 1:
        textchocolate.config(state=NORMAL)
        textchocolate.focus()
        textchocolate.delete(0, END)
    elif var26.get() == 0:
        textchocolate.config(state=DISABLED)
        e_chocolate.set('0')


def blackforest():
    if var27.get() == 1:
        textblackforest.config(state=NORMAL)
        textblackforest.focus()
        textblackforest.delete(0, END)
    elif var27.get() == 0:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')



root=Tk()

root.geometry('1270x690+0+0')

root.resizable(0,0)

root.title('RESTAURANT MANAGEMENT SYSTEM')

root.config(bg='firebrick4')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='black')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Yummy In My Tummy',font=('arial',30,'bold'),fg='#0ba322',bd=9,
                 bg='orange1',width=51)
labelTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='black')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='white',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

#Variables

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_roti=StringVar()
e_daal=StringVar()
e_sabji = StringVar()
e_chawal = StringVar()
e_fish = StringVar()
e_mutton = StringVar()
e_kebab = StringVar()
e_chicken = StringVar()
e_paneer = StringVar()

e_lassi=StringVar()
e_coffee = StringVar()
e_faluda = StringVar()
e_shikanji = StringVar()
e_roohafza = StringVar()
e_jaljeera = StringVar()
e_masalatea = StringVar()
e_badammilk = StringVar()
e_coldrinks = StringVar()

e_oreo=StringVar()
e_kitkat = StringVar()
e_vanilla = StringVar()
e_apple = StringVar()
e_blackforest = StringVar()
e_banana = StringVar()
e_brownie = StringVar()
e_pineapple = StringVar()
e_chocolate = StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

e_roti.set('0')
e_daal.set('0')
e_sabji.set('0')
e_fish.set('0')
e_kebab.set('0')
e_chawal.set('0')
e_mutton.set('0')
e_chicken.set('0')
e_paneer.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_roohafza.set('0')
e_shikanji.set('0')
e_jaljeera.set('0')
e_masalatea.set('0')
e_badammilk.set('0')
e_coldrinks.set('0')

e_kitkat.set('0')
e_banana.set('0')
e_pineapple.set('0')
e_apple.set('0')
e_chocolate.set('0')
e_oreo.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_vanilla.set('0')

##FOOD

roti=Checkbutton(foodFrame,text='Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1
                 ,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text='Daal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2
                 ,command=daal)
daal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='Fish',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3
                 ,command=fish)
fish.grid(row=2,column=0,sticky=W)

sabji=Checkbutton(foodFrame,text='Sabji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4
                  ,command=sabji)
sabji.grid(row=3,column=0,sticky=W)

kebab=Checkbutton(foodFrame,text='kebab',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5
                  ,command=kebab)
kebab.grid(row=4,column=0,sticky=W)

chawal=Checkbutton(foodFrame,text='Chawal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6
                   ,command=chawal)
chawal.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(foodFrame,text='Mutton',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,
                   command=mutton)
mutton.grid(row=6,column=0,sticky=W)

paneer=Checkbutton(foodFrame,text='Paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8
                   ,command=paneer)
paneer.grid(row=7,column=0,sticky=W)

chicken=Checkbutton(foodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9
                    ,command=chicken)
chicken.grid(row=8,column=0,sticky=W)

#Entry Fields for Food Items

textroti=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textfish=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textsabji = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_sabji)
textsabji.grid(row=3, column=1)

textkebab = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kebab)
textkebab.grid(row=4, column=1)

textchawal = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chawal)
textchawal.grid(row=5, column=1)

textmutton = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_mutton)
textmutton.grid(row=6, column=1)

textpaneer = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_paneer)
textpaneer.grid(row=7, column=1)

textchicken = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chicken)
textchicken.grid(row=8, column=1)

#Drinks

lassi=Checkbutton(drinksFrame,text='Lassi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10
                  ,command=lassi)
lassi.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11
                   ,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text='Faluda',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12
                   ,command=faluda)
faluda.grid(row=2,column=0,sticky=W)

shikanji=Checkbutton(drinksFrame,text='Shikanji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13
                     ,command=shikanji)
shikanji.grid(row=3,column=0,sticky=W)

jaljeera=Checkbutton(drinksFrame,text='Jaljeera',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14
                     ,command=jaljeera)
jaljeera.grid(row=4,column=0,sticky=W)

roohafza=Checkbutton(drinksFrame,text='Roohafza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15
                     ,command=roohafza)
roohafza.grid(row=5,column=0,sticky=W)

masalatea=Checkbutton(drinksFrame,text='Masala Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16
                      ,command=masalatea)
masalatea.grid(row=6,column=0,sticky=W)

badammilk=Checkbutton(drinksFrame,text='Badam Milk',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17
                      ,command=badammilk)
badammilk.grid(row=7,column=0,sticky=W)

colddrinks=Checkbutton(drinksFrame,text='Cold Drinks',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18
                       ,command=colddrinks)
colddrinks.grid(row=8,column=0,sticky=W)

#entry fields for drink items

textlassi = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_lassi)
textlassi.grid(row=0, column=1)

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1, column=1)

textfaluda = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_faluda)
textfaluda.grid(row=2, column=1)

textshikanji = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_shikanji)
textshikanji.grid(row=3, column=1)

textjaljeera = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_jaljeera)
textjaljeera.grid(row=4, column=1)

textroohafza = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_roohafza)
textroohafza.grid(row=5, column=1)

textmasalatea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_masalatea)
textmasalatea.grid(row=6, column=1)

textbadammilk = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_badammilk)
textbadammilk.grid(row=7, column=1)

textcolddrinks = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coldrinks)
textcolddrinks.grid(row=8, column=1)

#Cakes

oreocake=Checkbutton(cakesFrame,text='Oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19
                     ,command=oreo)
oreocake.grid(row=0,column=0,sticky=W)

applecake=Checkbutton(cakesFrame,text='Apple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20
                      ,command=apple)
applecake.grid(row=1,column=0,sticky=W)

kitkatcake=Checkbutton(cakesFrame,text='Kitkat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21
                       ,command=kitkat)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(cakesFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22
                        ,command=vanilla)
vanillacake.grid(row=3,column=0,sticky=W)

bananacake=Checkbutton(cakesFrame,text='Banana',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23
                       ,command=banana)
bananacake.grid(row=4,column=0,sticky=W)

browniecake=Checkbutton(cakesFrame,text='Brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24
                        ,command=brownie)
browniecake.grid(row=5,column=0,sticky=W)

pineapplecake=Checkbutton(cakesFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25
                          ,command=pineapple)
pineapplecake.grid(row=6,column=0,sticky=W)

chocolatecake=Checkbutton(cakesFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26
                          ,command=chocolate)
chocolatecake.grid(row=7,column=0,sticky=W)

blackforestcake=Checkbutton(cakesFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27
                            ,command=blackforest)
blackforestcake.grid(row=8,column=0,sticky=W)

#entry fields for cakes

textoreo = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=0, column=1)

textapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_apple)
textapple.grid(row=1, column=1)

textkitkat = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkat)
textkitkat.grid(row=2, column=1)

textvanilla = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vanilla)
textvanilla.grid(row=3, column=1)

textbanana = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_banana)
textbanana.grid(row=4, column=1)

textbrownie = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_brownie)
textbrownie.grid(row=5, column=1)

textpineapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pineapple)
textpineapple.grid(row=6, column=1)

textchocolate = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_chocolate)
textchocolate.grid(row=7, column=1)

textblackforest = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=8, column=1)

#costlabels & entry fields

labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg="white",fg='black')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='white',fg='black')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='white',fg='black')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='white',fg='black')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='white',fg='black')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='white',fg='black')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5
                     ,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5
                  ,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                   command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt

textReceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#Calculator
operator='' #7+9
def buttonClick(numbers): #9
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''



calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='black',bg='orange1',bd=6,width=6,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='black',bg='orange1',bd=6,width=6,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='black',bg='orange1',bd=6,width=6
               ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='black',bg='orange1',bd=6,width=6
                  ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6
               ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6
               ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
                   ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6
               ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6
               ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6
                  ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='black',bg='green1',bd=6,width=6,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='black',bg='green1',bd=6,width=6
                   ,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='black',bg='green1',bd=6,width=6
               ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='black',bg='green1',bd=6,width=6,
                 command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()'''
