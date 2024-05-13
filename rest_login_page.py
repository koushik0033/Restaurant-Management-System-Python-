from email import message
from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk, Image
#from PIL import ImageTk, Image
ws = Tk()
ws.title(' Admin Login Page')
ws.geometry('1750x1400+0+0')
#ws.resizable(400,300)
ws.config(bg='#E2D1F9')
#validation function
def validation():
 

#PASSWORD
    name = name_tf.get()
    pss = ''
    password = pwd.get()
    pss = "" #Turn off validation.
    if len(password) == 0 or len(name) == 0:
        messagebox.showinfo('message', 'fill the empty field!!!')
    else:
        # if name=="":
        #     messagebox.showerror('Error','Username cannot be Empty')
        # elif password=='':
        #     messagebox.showerror('Error','Password field cannot be Empty')
        if password=='' or name=='':
             messagebox.showinfo('message', 'fill the empty field!!!')
        elif name=="Admin" and password=="Admin":
            messagebox.showinfo('message', 'Admin Verified Successfully!!! Have Nice Day')
            ws.destroy()
            import rest_pgm
        else:
            #messagebox.showinfo('message', 'Wrong username or password!!!')
            messagebox.showerror('error','Wrong username or password!!!')

    
frame = Frame(
    ws,
    bd=2,
    bg='#8AAAE5',
    padx=60,
    pady=320

)
frame.pack(pady=50)

#login image
logoImage=PhotoImage(file="D:\SOFTWARE COMPT\SOFTWARE COMPT\imag1.png")
label=Label(frame,image=logoImage)
label.place(x=80,y=-280)#pack(pady=5)


'''lImage=PhotoImage(file="C:\SYCS\SOFTWARE COMPT\img_1.png")
label=Label(ws,image=lImage)
label.place(x=0,y=0)'''
#label.config(height=1750,width=1400)


Label(
    frame,
    bg='#8AAAE5',
    text='UserName',
    font = ('Bebas Neue', 19)
).grid(row=0, column=0,padx=0)
Label(
    frame,
    bg='#8AAAE5',
    text='Password',
    font = ('Bebas Neue', 19)
).place(x=5,y=80)

pwd = Entry(
    frame,
    font = ('sans-serif', 14),
    show= '*'
)
pwd.place(x=135,y=85)

name_tf = Entry(
    frame,
    font = ('sans-sherif', 14),
    fg='black'
)
name_tf.grid(row=0, column=5,padx=8)

submit = Button(
    frame,
    text='Submit',
    width=15,
    height=1,
    bg="#CCCCCC",
    #font=f, 
    relief=SOLID,
    cursor='hand2',
    font = ('Times', 14),
    command=  validation ,
    pady=10
)
submit.place(x=100,y=180)#grid(row=8, columnspan=2, pady=20)

ws.mainloop()

