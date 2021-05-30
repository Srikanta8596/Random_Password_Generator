from random import *
from tkinter import *

num = "0123456789"
alphanum = "abcdefghijklmnopqrstuvxwyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spalphanum = "abcdefghijklmnopqrstuvxwyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'#@(){}[]/<>!$%^&*+-_"
# passlen= int(input("Enter password length \n"))
# randPass= []
# print('Select the type of password \n1. Number \n2. Aphanumeric \n3. Special Alphanumeric')
# Selecttype= int(input())
# if Selecttype ==1:
#     for i in range(passlen):
#         randPass.append(choice(num))
# elif Selecttype==2:
#     for i in range(passlen):
#         randPass.append(choice(alphanum))
# else:
#     for i in range(passlen):
#         randPass.append(choice(spalphanum))
# result = "".join(randPass)
# print(" Your random password " + result)

def Create_Pass():
    TheChoice=Tchoice.get()

    if TheChoice=="":
        resultBox.delete(0.0,END)
        resultBox.insert(END,"\n Select the type of password you'd like")

    length=int(Pass_length.get())
    randPass = []
    for i in range(length):
        randPass.append(choice(TheChoice))
    result="".join(randPass)
    TheResult="\n *** Your Password is : " +result+" *** \n"

    resultBox.delete(0.0, END)
    resultBox.insert(END, TheResult)







window = Tk()
window.geometry("800x500")

ProgName = Label(window,font=('Kristen ITC',15,'bold'),text="Password Generator (^_^)",fg="blue")
ProgName.grid(row=1,column=3,padx=200,pady=30)

ChooseType=Label(window,font=('Kristen ITC',15,'bold'),text="Choose a type among the 3")
ChooseType.place(relx=.03,rely=0.25)

Tchoice=StringVar()
NumChoice=Radiobutton(window,font=('corbel',10,'italic'),text="Numeric",variable= Tchoice,value=num)
NumChoice.place(relx=.03,rely=0.32)
AlphaNumChoice=Radiobutton(window,font=('corbel',10,'italic'),text="Alphanumeric",variable= Tchoice,value=alphanum)
AlphaNumChoice.place(relx=.03,rely=0.38)
SpecialChoice=Radiobutton(window,font=('corbel',10,'italic'),text="Special Alphanumeric",variable= Tchoice,value=spalphanum)
SpecialChoice.place(relx=.03,rely=0.44)


size= Label(window,text='Size',font=('Copperplate Gothic',10,'bold'))
size.place(relx=0.65,rely=0.4)

Pass_length=Spinbox(window,from_=8,to=100)
Pass_length.place(relx=0.73,rely=0.4)
Pass_length.config(state="readonly")

GenButton=Button(window,text='Generator',command=Create_Pass)
GenButton.place(relx=0.45,rely=0.60)

resultBox= Text(window,height =6,width=70)
resultBox.place(relx=0.15,rely=0.70)





window.mainloop()