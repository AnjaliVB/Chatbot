import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from nltk.chat.util import Chat, reflections
import chatterbot
import time
from threading import Timer
import customtkinter

#from tkinter import PhotoImage

botui=tk.Tk()
user_var=tk.StringVar()

i=90
j=60

def send(event):    
    global i,j
    user_reply=Label(second_frame,text=user_var.get(),
               relief="groove",bg="white",fg="maroon",font=("Comic Sans ms",11,"bold"))
    user_reply.place(x=25+i,y=20+j,height=45,width=200)
    #user_reply.place(expand=1,fill=BOTH)
    chatreply()
    #botui.after(1000,chatreply)
    i=90
    j=j+40
    user_var.set("")


def chatreply():
    print("chatreply()")
    global j,i
    i=25
    j=j+70
    if user_var.get().lower()=="bye":
        reply=Label(second_frame,text="Bye\nHave a nice day !", bd=1,relief="solid",bg="maroon",fg="white",font=("Comic Sans ms",11,"bold"))
        reply.place(x=i,y=j+10,height=45,width=200)
    print("i=",i,"j=",j)
    j=j+10
    #reply = PhotoImage(file="Untitled.png")-----to insert image
    #bot=Label(botui,image=reply)

    
#######     botui credits   #######
botui.geometry("350x450+1130+250")
botui.resizable(False,False)
botui.title("Site Assistant")

#####   botframe in botui  ####
botframe=ttk.Frame(botui,width=200,height=500)
botframe.pack(expand=True,fill=BOTH)#place(x=0,y=0,height=380,width=350)

#####   botcanvas in botframe   ####
botcanvas=tk.Canvas(botframe,bg='pink',width=200,height=500,scrollregion=(0,0,500,500))

#####   scrollbar   #####
scrollbar=ttk.Scrollbar(botcanvas,orient='vertical',command=botcanvas.yview)
scrollbar.pack(side=RIGHT,fill=Y)

######  scrollregion    #####
botcanvas.configure(yscrollcommand=scrollbar.set)
botcanvas.bind("<Configure>",lambda e: botcanvas.config(scrollregion=botcanvas.bbox('ALL')))

######  second_frame in botcanvas   ######
second_frame=Frame(botcanvas)

######  creating second_frame in botcanvas  #####
botcanvas.create_window((0,0),window=second_frame,anchor='nw')

####    placing botcanvas   ####
botcanvas.place(x=0,y=0,height=380,width=350)
second_frame.place(x=0,y=0,height=300,width=300)

#########################################


botreply=Label(second_frame,text="Hey, I am a Site Assistant\n How can I help you ?",
          bd=1,relief="solid",bg="maroon",fg="white",font=("Comic Sans ms",11,"bold"))

sendbutton=Button(botframe,text="Send",height=2,width=8,activebackground="white",
                  activeforeground="maroon",bg="maroon",fg="white",font=("",10,"bold"),command=send)
userentry=Entry(botframe,textvariable=user_var,fg="maroon",relief="solid")




botreply.place(x=25,y=20,height=45,width=200)
userentry.place(x=15,y=390,height=41)
userentry.configure(width=42)
sendbutton.place(x=270,y=388)




botui.bind("<Return>",send)         #send button will be clicked on pressing enter

#botcanvas.config(scrollregion=botcanvas.bbox('all'))
botui.mainloop()
   

'''pairs=[ [r"my name is (.*)",["Hello %1 , How are you doing? "]],]

def bot():
    print("Hi ! \nWhat's your name?")
    cb=Chat(pairs,reflections)
    cb.converse()

bot()'''

