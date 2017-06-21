import Tkinter,tkFileDialog
global filenm;
def openfile():
	global filenm;
	file = tkFileDialog.askopenfile(parent=root,mode='r+',title='Choose a file')
	if file != None:
		text1.delete("1.0", Tkinter.END)
		text1.insert('1.0', file.read())
		filenm=file.name
	file.close
def savefile():
	global filenm;
	file=open(filenm, "w")
	thetext = text1.get('1.0', Tkinter.END)
	file.write(thetext)
	file.close
root=Tkinter.Tk()
root.title=("TEXTEDIT")
text1= Tkinter.Text(root)
text1.pack(fill=Tkinter.BOTH, expand=Tkinter.YES)
btn = Tkinter.Button(root, text="Chose File", command=openfile)
btn.pack()
btn1 = Tkinter.Button(root, text="Save File", command=savefile)
btn1.pack()
root.mainloop()