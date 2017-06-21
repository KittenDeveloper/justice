import Tkinter,tkFileDialog
global filenm;
def openfile():
	global filenm;
	file = tkFileDialog.askopenfile(parent=root,mode='r+',title='Choose a file')
	if file != None:
		text1.insert('1.0', file.read())
		filenm=file.name
	file.close
def savefile():
	global filenm;
	file=open(filenm, "r+")
	thetext = text1.get('1.0', 'end')
	file.write(thetext)
	file.close
root=Tkinter.Tk()
root.title=("TEXTEDIT")
text1= Tkinter.Text(root)
text1.grid(row=1,column=1)
btn = Tkinter.Button(root, text="Chose File", command=openfile)
btn.grid(row=2,column=1)
btn1 = Tkinter.Button(root, text="Save File", command=savefile)
btn1.grid(row=3,column=1)
root.mainloop()