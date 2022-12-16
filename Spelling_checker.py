

from tkinter import *
from textblob import TextBlob

def check_spelling():
    a=TextBlob(spell_check.get())
    spell=Label(window,text="The Correct Spelling is:",font=('Arial',30,"bold"),bg="lightblue")
    spell.pack()
    correct_text=Label(window,text=str(a.correct()),font=("Arial",40,"bold"),bg="lightpink")
    correct_text.pack()


window=Tk()
window.title("My Spelling Checker")
window.geometry("800x600")

window.config(background="green")
text_heading=Label(window,text="Spelling Check",font=("Times new roman",50,'bold'),bg="black",fg="White")
text_heading.pack()

text_check=Label(window, text="Enter the Text",font=("Arial",30,"bold"),bg="yellow",fg="black")
text_check.pack()

spell_check=Entry(window, font=("Arial",45,"bold"),width=500,bg="lightpink")
spell_check.pack()

check_button=Button(window,text="check !!",font=("Arial",30,"bold"),fg='blue',bg='yellow',command=check_spelling)
check_button.pack()
window.mainloop()