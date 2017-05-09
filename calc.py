import Tkinter

def solveit():
	label1.config(text=eval(input1.get()))

root= Tkinter.Tk()
root.title("Calculator")
label1=Tkinter.Label(root)
label1.grid(column=2,row=1)
input1=Tkinter.Entry(root)
input1.grid()
solvebtn=Tkinter.Button(root, text="Solve", command=solveit)
solvebtn.grid(column=2)
root.mainloop()