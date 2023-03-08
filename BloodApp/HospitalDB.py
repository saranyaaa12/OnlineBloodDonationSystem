from tkinter import *

window = Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
#window.geometry('1200x800')
window.resizable(True,True)
#window.config(bg='spring green')

#FRAME FOR ADD HOSPITAL / CHECK BLOOD REQUEST / CHECK DONOR REQUEST / SEND DONOR REQUEST / USERS -- BUTTONS
#Column 1

frame1 =Frame(window,height=5,highlightthickness=0,bg='#B22222',border=5)
frame1.grid(row=1,column=0,sticky='w')

btn = Button(frame1 ,text='Add Hospitals',font=('Garamond',16),bg='white',border=2,width=21)
btn.grid(row=13,column=0,pady=30)
