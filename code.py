import tkinter
import tkinter.font as font
import socket
import os
top = tkinter.Tk()
top.title("SWS IP blocker")

#setting tkinter window size
top.geometry("%dx%d" % (550, 300))

top.configure(bg='black')
myFont1 = font.Font(size=20,weight='bold') 

label = tkinter.Label(top, text = "SWS IP blocker",fg='red',bg='black')
label.pack()
label['font'] = myFont1
label.place(x = 20,y = 20)
label1 = tkinter.Label(top, text = "Enter ip/domain name",font=2,fg='red',bg='black')
label1.pack()
label1.place(x = 50,y = 100)

name_var=tkinter.StringVar()

en=tkinter.Entry(top,textvariable = name_var,width=50,bg='red',font=2)
en.pack()
en.place(x = 50,y = 150,height=30,width=350)

def block():
    name=name_var.get()
    addr1 = socket.gethostbyname(name)
    os.system('iptables -I INPUT -s ' +str(addr1)+' -j DROP')
def unblock():
    name=name_var.get()
    addr1 = socket.gethostbyname(name)
    os.system('iptables -I INPUT -s ' +str(addr1)+' -j ACCEPT')

bt=tkinter.Button(top,text='Block',fg='red',bg='black',command = block)
bt.pack()
bt.place(x = 50,y = 190,height=30,width=60)

bt=tkinter.Button(top,text='Unblock',fg='red',bg='black',command = unblock)
bt.pack()
bt.place(x = 150,y = 190,height=30,width=60)

top.mainloop()
