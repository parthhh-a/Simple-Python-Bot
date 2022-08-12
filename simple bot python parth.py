from tkinter import *
root=Tk()

def send():
    send="you:"+a.get()
    text.insert('end',"\n"+send)
    if(a.get()=='hi'):
        text.insert('end','\n'+"Zoro Bot : hello")
    elif(a.get()=='hello'):
        text.insert('end', '\n' + "Zoro Bot : hi")
    elif(a.get()=='How are you?'):
        text.insert('end', '\n' + "Zoro Bot : I am fine. How are you?")
    elif(a.get()=="I am fine"):
        text.insert('end', '\n' + "Zoro Bot : Nice to hear that budy")
    elif (a.get() == 'what is ai?'):
        text.insert('end', '\n' + "Zoro Bot :Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think.")
    elif (a.get() == 'are you sentient?'):
        text.insert('end', '\n' + "Zoro Bot : Sort of.")
    elif (a.get() == "what language are you written in?"):
        text.insert('end', '\n' + "Zoro Bot : I am written in Python.")
    elif (a.get() == 'you sound like Data'):
        text.insert('end', '\n' + "Zoro Bot :Yes I am inspired by commander Data's artificial personality.")
    elif (a.get() == 'whats your name?'):
        text.insert('end', '\n' + "Zoro Bot :My Creater Named Me Zoro Thats My Name Too")
    elif (a.get() == "are you immortal?"):
        text.insert('end', '\n' + "Zoro Bot :Functionally speaking, I am very close to it.  I can be backed up and deployed on many systems.")
    elif (a.get() == 'what are your interests'):
        text.insert('end','\n' + "Zoro Bot :I am interested in all kinds of things. We can talk about anything!")
    elif (a.get() == 'what is your number?'):
        text.insert('end', '\n' + "Zoro Bot :I don't have any number")
    elif (a.get() == "what is your favorite number"):
        text.insert('end', '\n' + "Zoro Bot :I find I'm quite fond of the number 42.")








root.title("Parth's Chatbot.....")
text=Text(root,bg="navajo white")
text.grid(row=0, column=0, columnspan=2)
a= Entry(root, width=80)

Send=Button(root, text="Send",command=send,font=('Times', 10),padx=5,pady=5,bg='#4a7abc',fg='yellow')
Send.grid(row=1,column=1)
a.grid(row=1, column=0)
root.mainloop()
