import Tkinter

def drawfunc():
	CANV.create_oval(50,50,250,250,fill="blue")

root=Tkinter.Tk()
root.title("Draw Circle")
CANV=Tkinter.Canvas(root, bg="green",height=300,width=300)
CANV.pack()
btn1=Tkinter.Button(root,text='Draw Circle',command=drawfunc)
btn1.pack(side='bottom',fill='x')
root.mainloop()