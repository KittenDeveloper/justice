import Tkinter
import time

def drawfunc():
	loc=50
	loc2=250
	while 1:
		time.sleep(0.001)
		CANV.move(circle1,1,0)
		CANV.update()
root=Tkinter.Tk()
root.title("Draw Circle")
CANV=Tkinter.Canvas(root, bg="green",height=300,width=300)
circle1 =CANV.create_oval(50,50,250,250,fill="blue")
CANV.pack(fill='both')
btn1=Tkinter.Button(root,text='Draw Circle',command=drawfunc)
btn1.pack(side='bottom',fill='x')
root.mainloop()
