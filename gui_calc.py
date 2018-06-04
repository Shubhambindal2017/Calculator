from __future__ import division
from Tkinter import *
from tkMessageBox import *

class Calc(Frame):

    string=""

    def __init__(self):

        Frame.__init__(self)
        self.master.title("CALCULATOR")
        #self.master.config("1500x1000")
        self.master.rowconfigure(0,weight=1)
        self.master.columnconfigure(0,weight=1)

        self.grid(sticky=W+E+N+S)

        self.text=Entry(self,width=60)
        self.text.grid(row=0,column=0,columnspan=4,sticky=W+E+N+S)
        self.text.insert(INSERT,"ENTER YOUR NUMBERS")

        self.button1=Button(self,text="7",command=self.seven)
        self.button1.grid(row=1,column=0,sticky=E+W+N+S)

        self.button2=Button(self,text="8",command=self.eight)
        self.button2.grid(row=1,column=1,sticky=E+W+N+S)

        self.button2=Button(self,text="9",command=self.nine)
        self.button2.grid(row=1,column=2,sticky=E+W+N+S)

        self.button4=Button(self,text="/",command=self.divide)
        self.button4.grid(row=1,column=3,sticky=E+W+N+S)

        self.button5=Button(self,text="4",command=self.four)
        self.button5.grid(row=2,column=0,sticky=E+W+N+S)

        self.button6=Button(self,text="5",command=self.five)
        self.button6.grid(row=2,column=1,sticky=E+W+N+S)

        self.button7=Button(self,text="6",command=self.six)
        self.button7.grid(row=2,column=2,sticky=E+W+N+S)

        self.button8=Button(self,text="-",command=self.diff)
        self.button8.grid(row=2,column=3,sticky=E+W+N+S)

        self.button9=Button(self,text="1",command=self.one)
        self.button9.grid(row=3,column=0,sticky=E+W+N+S)

        self.button10=Button(self,text="2",command=self.two)
        self.button10.grid(row=3,column=1,sticky=E+W+N+S)

        self.button11=Button(self,text="3",command=self.three)
        self.button11.grid(row=3,column=2,sticky=E+W+N+S)

        self.button12=Button(self,text="*",command=self.multiply)
        self.button12.grid(row=3,column=3,sticky=E+W+N+S)

        self.button13=Button(self,text="0",command=self.zero)
        self.button13.grid(row=4,column=0,sticky=E+W+N+S)

        self.button14=Button(self,text=".",command=self.decimal)
        self.button14.grid(row=4,column=1,sticky=E+W+N+S)

        self.button15=Button(self,text="=",command=self.equal)
        self.button15.grid(row=4,column=2,sticky=E+W+N+S)

        self.button16=Button(self,text="+",command=self.plus)
        self.button16.grid(row=4,column=3,sticky=E+W+N+S)

        self.button17=Button(self,text="CE",command=self.ce)
        self.button17.grid(row=5,column=0,columnspan=2,sticky=E+W+N+S)

        self.button18=Button(self,text="C",command=self.c)
        self.button18.grid(row=5,column=2,sticky=E+W+N+S)

        self.button19=Button(self,text="**",command=self.power)
        self.button19.grid(row=5,column=3,sticky=E+W+N+S)


    def seven(self):

        Calc.string+="7"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def eight(self):

        Calc.string+="8"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def nine(self):

        Calc.string+="9"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def four(self):

        Calc.string+="4"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def three(self):

        Calc.string+="3"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def five(self):

        Calc.string+="5"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def six(self):

        Calc.string+="6"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def one(self):

        Calc.string+="1"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)
    def two(self):

        Calc.string+="2"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def multiply(self):

        Calc.string+="*"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def plus(self):

        Calc.string+="+"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def decimal(self):

        Calc.string+="."
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def divide(self):

        Calc.string+="/"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def diff(self):

        Calc.string+="-"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def zero(self):

        Calc.string+="0"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)

    def equal(self):

        ans=eval(Calc.string)
        answer=str(ans)
        self.text.delete(0,END)
        self.text.insert(INSERT,(answer))
        (Calc.string)=""
        
        Calc.string+=answer

    def ce(self):

        self.text.delete(0,END)
        Calc.string=""
        self.text.insert(INSERT,"ENTER YOUR NUMBERS")

    def c(self):

        string_temp=Calc.string[0:len(Calc.string)-1]
        Calc.string=""
        self.text.delete(0,END)
        self.text.insert(INSERT,string_temp)
        Calc.string=string_temp
        
    def power(self):

        Calc.string+="**"
        self.text.delete(0,END)
        self.text.insert(INSERT,Calc.string)




    

        


Calc().mainloop()
