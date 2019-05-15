from tkinter import *
from tkinter.font import Font
import wikipedia

def search_me():
    text.delete(1.0,END)
    entered_data = entry1.get()
    try:
        answer_data = wikipedia.summary(entered_data)
    except:
        answer_data = "plzz check your input or enternet connection"
    finally:
        text.insert(INSERT,answer_data)

root = Tk()
root.geometry("500x500+200+200")


fr1 = Frame(root,width=500,bg="black",bd=3)
entry1 = Entry(fr1,width=60,bg="lightblue")
entry1.pack()
btn1 = Button(fr1,text="search",command=search_me)
btn1.pack()
fr1.pack(side=TOP)

lbl = Label(root,text="",height=3)
lbl.pack()

fr2 = Frame(root,width=500,height=500,bg="black",bd=2)

scroll = Scrollbar(fr2)
scroll.pack(side=RIGHT,fill=Y)

# text = Text(fr2,yscrollcommand=scroll.set)

my_font = Font(size=16,)
text = Text(fr2,width=40,height=20,bg="black",fg="green",selectbackground="orange",yscrollcommand=scroll.set,wrap=WORD)
text.configure(font="my_font")
text.pack()
scroll.config(command = text.yview)
fr2.pack()

root.mainloop()

