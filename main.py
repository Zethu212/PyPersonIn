# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *

from Person import *


class MyWindow:
    def __init__(self, win):
        self.lbl0f = Label(win, text='First name')
        self.lbl0s = Label(win, text='Surname')
        self.lbl1 = Label(win, text='Id number')
        self.lbl2 = Label(win, text='Birth date')
        self.lbl3 = Label(win, text='Full report')
        self.t0f = Entry()
        self.t0s = Entry()
        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Text(height=10, width=40)
        self.lbl0f.place(x=100, y=50)
        self.lbl0s.place(x=100, y=100)
        self.lbl1.place(x=100, y=150)
        self.lbl2.place(x=100, y=200)
        self.t0f.place(x=200, y=50)
        self.t0s.place(x=200, y=100)
        self.t1.place(x=200, y=150)
        self.t2.place(x=200, y=200)
        self.v0 = IntVar()
        self.v0.set(1)
        self.r1 = Radiobutton(text="PhD Student", variable=self.v0, value=1)
        self.r2 = Radiobutton(text="PhD Examiner", variable=self.v0, value=2)
        self.r1.place(x=100, y=245)
        self.r2.place(x=260, y=245)
        self.lbl4 = Label(win, text='Student no')
        self.lbl5 = Label(win, text='Internal mark')
        self.lbl8 = Label(win, text='External mark')
        self.lbl6 = Label(win, text='Staff no')
        self.lbl7 = Label(win, text='rate per hour')
        self.lbl9 = Label(win, text='no of hours worked')
        self.t4 = Entry()
        self.t5 = Entry()
        self.t8 = Entry()
        self.t6 = Entry()
        self.t7 = Entry()
        self.t9 = Entry()
        self.lbl4.place(x=100, y=330)
        self.lbl5.place(x=100, y=360)
        self.lbl8.place(x=100, y=390)
        self.lbl6.place(x=350, y=330)
        self.lbl7.place(x=350, y=360)
        self.lbl9.place(x=350, y=390)
        self.t4.place(x=200, y=330)
        self.t5.place(x=200, y=360)
        self.t8.place(x=200, y=390)
        self.t6.place(x=430, y=330)
        self.t7.place(x=430, y=360)
        self.t9.place(x=470, y=390)
        self.b1 = Button(win, text='OK', command=self.showReport)
        self.b1.place(x=280, y=450)
        self.lbl3.place(x=100, y=500)
        self.t3.place(x=150, y=500)

    def showReport(self):
        fn = self.t0f.get()
        sn = self.t0s.get()
        id = self.t1.get()
        db = self.t2.get()
        r = ""
        if self.v0.get() == 1:
            stdn = self.t4.get()
            im = self.t5.get()
            em = self.t8.get()
            tt = Student()
            tt.firstname = fn
            tt.surname = sn
            tt.idnumber = id
            tt.birthdate = db
            tt.studentno = stdn
            tt.internalmark = im
            tt.externalmark = em
            r = tt.reportLines()
        self.t3.delete('1.0', END)
        self.t3.insert(INSERT, r)
        if self.v0.get() == 2:
            stf = self.t6.get()
            rh = self.t7.get()
            nh = self.t9.get()
            ee = Examiner()
            ee.firstname = fn
            ee.surname = sn
            ee.idnumber = id
            ee.birthdate = db
            ee.staffno = stf
            ee.hourrate = rh
            ee.hours = nh
            r = ee.reportLines()
        self.t3.delete('1.0', END)
        self.t3.insert(INSERT, r)
def draw_win():
    window = Tk()
    MyWindow(window)
    window.title("PhD Inheritance")
    window.geometry("600x700+10+10")
    window.mainloop()

if __name__ == '__main__':
    draw_win()