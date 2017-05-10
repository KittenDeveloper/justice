import Tkinter
import __future__
def solveit():
	label1.config(text=eval(compile(input1.get(),'<string>','eval', __future__.division.compiler_flag)))

root= Tkinter.Tk()
root.title("Calculator")
label1=Tkinter.Label(root)
label1.grid(column=2,row=1)
input1=Tkinter.Entry(root)
input1.grid()
solvebtn=Tkinter.Button(root, text="Solve", command=solveit)
solvebtn.grid(column=2)
root.mainloop()