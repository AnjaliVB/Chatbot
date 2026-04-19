
import tkinter as tk
from tkinter import *
from tkinter import font
import nltk
from nltk.chat.util import Chat,reflections
import time
import re
import datetime

global i,j
i=3.0
j=3.39
window=Tk()                                        #creating main window 
user_var=tk.StringVar()

window.title("Site Assistant")
s="          "      #spaces

pairs=[
    #["--queries--",["--responses--"]],
    ["hi|hello|hey|hey there|all good|m fine 2|m fine|m fine too|i am ok|m ok|am ok|im ok|fine too|fine",["How can I help you?"]],#"Hey user !"+s+s+s+s+s+s+"How can I help you ? "+s+s+s+s+"o Past Projects  "+s+s+s+s+s+"o Our Clients     "+s+s+s+s+s+"o Our Vision & Mission      "+s+s+s+"o Client Reviews         "+s+s+s+s+"o Careers  "+s+s+s+s+s+s+"o Work hours              "+s+s+s+s+"o Costing & Pricing    "+s+s+s+s+"o Our Contact    "+s+s+s+s+s+"o Technologies "+s+s+s+s+s+"o Services"+s+s+s+s+s+s+" o Roles and Responsibilities \n"]],
    [r"how are you?|What's up ?|how r u|whats up",["I'm fine! How are you doing?"]],
    ["who are you?|who r u?|who r you|who are u|Where are you|where r u|where are u|whats your name|what is ur name|what is your name|whats ur name",["I'm a bot. How can I help you?"]],
    ["ok|alright|np|no problem",["Anything else I can help you with?"]],
    ["service|services|what services do u provide|what services do you provide|tell me abt your services|tell me about ur services",["Main services we provide include:     "+s+"o Blockchain"+s+s+s+s+s+"      o Web Applications Development"+s+"      o Mobile Application Development"+s+"     and many more....."]],
    ["trending techs|trending technologies|technologies|trending technology|technology|techs",["Advanced technologies we use"+s+s+"o DevOps  "+s+s+s+s+s+s+"o Apache Pig      "+s+s+s+s+s+"o Java         "+s+s+s+s+s+s+"o React      "+s+s+s+s+s+s+"o MongoDB"+s+s+s+s+s+s+"and many more....."]],
    ["contact|how can i contact you",["You can write to us at"+s+s+s+s+"info@shreeinfotech.com"+s+s+s+s+"Or call us on:     "+s+s+s+s+s+"9876543212"]],
    ["valuable customers|eminent clients|list of clients|clients|client|customers",["Our Happy Clients      "+s+s+s+s+"o Microsoft"+s+s+s+s+s+"        o LinkedIn"+s+s+s+s+s+s+"o Oracle"+s+s+s+s+s+s+"    o Wipro"+s+s+s+s+s+s+"     o Cisco"]],
    ["shree infotech|tell your history|tell me about your company|tell me abt ur company|tell me abt your company|tell me about your company|tell me about ur company|tell me about the company|about shree infotech|about",[" We devote ourselves to digitizing      "+s+" our client's businesses for the "+s+s+"rising  tide of technological needs. "+s+"   From the founder to the new "+s+s+"    recruit, passion drives everybody  "+s+"   to excel at Shree Infotech.  Rising"+s+"     customer satisfaction is one of our "+s+"  key performance indicators."]],
    ["charges|rate|how do you charge a service|cost|cost of service|price of product|price of service|pricing",["For pricing, contact us : "+s+s+s+"    info@shreeinfotech.com    "+s+s+s+s+"or call us on      "+s+s+s+s+s+" 9876543212"]],
    ["established",["It has been 10 years since we are"+s+s+"delivering good services to our "+s+s+" clients."]],
    ["info on|tell me about iot|tell me about blockchain|tell me about amp|tell me about vso|tell me something about iot|iot|vso|amp|blockchain|tell me something about blockchain|tell me something about amp|tell me something about vso|tell me something about internet of things|tell me something about accelerated mobile pages|tell me something about voice search optimization",["For more information, visit the"+s+s+"home page"]],
    ["vision and mission|vision|mission|your vision and mission|ur vision & mission",["Our Vision is to create a world "+s+s+"where our solutions redefine    "+s+s+"standards, and we lead with"+s+s+"      creativity to shine.Our Mission is "+s+"      empowering with unrivaled digital "+s+"  expertise, we innovate and guide,"+s+"      shaping brighter futures. "]],
    ["past projects|past projs|projs|projects",["We build customized CRMs,      "+s+s+" e-learning platforms,video "+s+s+"        streaming platforms,chatting "+s+s+"  applications,chatbots,Authenticator "+s+"apps, and many more. Contact us for"+s+"more information."]],
    ["working hrs|working hours|work hours|hours|work hrs|hrs|work days|time",["We work from Monday to Friday,"+s+"      from 9am to 8pm."]],
    ["job vacancy|vacancies|vacancy|salary|job|internships|internship|careers|career|jobs|job opennings|current jobs|current opennings|hirings|hiring|are you hiring",["We do not have current openings."]],
    ["roles and responsibilities|roles|responsibilities|designations|designation|employees",["We have Software Developers  "+s+s+"Security Testers         "+s+s+s+s+"Penetration Testers "+s+s+s+s+" UI/UX Developers "+s+s+s+s+"    Backend Developers"]],
    ["nope|no|not needed|thanks|thnx|thx|tnx",["You're Welcome"+s+s+s+s+s+"Bye"]],
    ["customer reviews|customer review|reviews|feedback|customer response|testimonials|customer testimonials",["For client reviews and testimonials,"+s+" visit 'Our Clients' tab."]],
    ["awards|which awards |what awards",["NATIONAL AWARD FOR "+s+s+s+s+" TECHNOLOGY START-UPS"+s+s+"  Best ERP Solution Provider"+s+s+"        Best Digital Transformation"+s+s+"      Best Use of AI/Bots"+s+s+s+s+"   Best use of Technology "+s+s+s+s+"for Scalable Solution"+s+s+s+"     Best use of Mobile for Social and"+s+s+" Economic Development"]],
    ["your address|your location|location|address|where is your company|where is ur company",[" Shree Infotech,"+s+s+s+s+s+"Vishwakarma Techno Park,       "+s+s+"Ganeshpur,"+s+s+s+s+s+"        Maharashtra,     "+s+s+s+s+s+"India."]],
    ["number of employees|employee no.|emp no.|employee number|employee count|company size|staff",["We have 60-80 employees"]],
    ["vacation|off days|leave|weekends|weekend",["We have two-day weekend-"+s+s+s+"Saturday and Sunday"]],
    ["branches|offices|headquarters|hq",["We are situated in Mumbai and are"+s+"   looking forward to leap in other"+s+s+"cities of India."]],
    ["social media|social media links",["Just search for Shree_Info on "+s+s+s+" LinkedIn and Facebook."]],
    ["courses|do you offer any courses",["We do not offer any courses."+s+s+"    We are purely a Software "+s+s+s+"Development Company."]]
    ]

chatbot=Chat(pairs,reflections)     #Chat is in-built class
                                    #reflections and pairs are functions in nltk.chat.util file

def send(event):
    global i,j
    text1.config(state=NORMAL)          #editable text
    reply=user_var.get().lower()
    text1.insert(tk.END,"You : "+reply+"\n")
    text1.tag_add("start",i,j)
    text1.tag_config("start",foreground="blue")
    response=chatbot.respond(reply)
    
    i=i+2
    j=j+2
    
    if response:
        text1.insert(tk.END,"Bot : "+response+"\n")
    else:
        text1.insert(tk.END,"Bot : I did not understand that."+s+s+s+s+"Can you rephrase it ?\n")
        
    text1.config(state=DISABLED)        #readonly text
    user_var.set("")
    
    if reply.lower()=="bye":
        window.destroy()


#window configuration
window.geometry("350x450+1130+250")
window.resizable(False,False)

boticon=PhotoImage(file="C:\\Users\\Vijay\\OneDrive\\Desktop\\Chatbot_project\\chatbot_icon.png")     #selecting image for icon on title bar
window.iconphoto(False,boticon)         #setting image

#gui for the bot
text1=Text(window)

sendbutton=Button(window,text="Send",height=2,width=8,activebackground="white",
                  activeforeground="maroon",bg="maroon",fg="white",font=("",10,"bold"),command=send)

userentry=Entry(window,fg="maroon",relief="solid",textvariable=user_var)

font_=font.Font(family="cambria",size=13,weight="bold")             #defining font
text1.config(font=font_,fg="maroon",spacing3=10)                #setting font

#inserting text in textbox
#text1.insert(tk.END,"\nBot : Hey user !"+s+s+s+s+s+s+"How can I help you ? "+s+s+s+s+"o Past Projects  "+s+s+s+s+s+"o Our Clients     "+s+s+s+s+s+"o Our Vision & Mission      "+s+s+s+"o Testimonials            "+s+s+s+s+"o Careers  "+s+s+s+s+s+s+"o Work hours              "+s+s+s+s+"o Costing & Pricing    "+s+s+s+s+"o Our Contact    "+s+s+s+s+s+"o Technologies "+s+s+s+s+s+"o Services"+s+s+s+s+s+s+" o Roles and Responsibilities \n")
text1.insert(tk.END,"\nBot : Welcome to Shree Infotech"+s+s+s+"How can I help you?\n")

#placing all of them on the window
userentry.place(x=15,y=390,height=41)
userentry.configure(width=42)
userentry.focus()                       # focus() will place the cursor on typing area to send queries
sendbutton.place(x=270,y=388)

text1.place(x=10,y=5,height=380,width=325)
text1.config(state=DISABLED)        #readonly text

window.bind("<Return>",send)            #send button will be clicked on pressing enter

window.mainloop()
