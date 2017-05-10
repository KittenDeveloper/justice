import Tkinter
import time

def drawfunc():
	loc=50
	loc2=250
	while 1:
		time.sleep(0.01)
		loc=loc+1
		loc2=loc2+1
		CANV.create_oval(loc,50,loc2,250,fill="blue")
		root.update()
		if loc ==1000: break

root=Tkinter.Tk()
root.title("Draw Circle")
CANV=Tkinter.Canvas(root, bg="green",height=300,width=300)
CANV.pack(fill='both')
btn1=Tkinter.Button(root,text='Draw Circle',command=drawfunc)
btn1.pack(side='bottom',fill='x')
root.mainloop()
