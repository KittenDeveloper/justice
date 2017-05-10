import Tkinter

global state
global dict
dict1={}
state=1

def appendfunc():
	global state
	state =2
	search.pack_forget()
	append.pack()
def enterfunc():
	global dict1
	global state
	if state == 1:
		try:
			lbl1.config(text=dict1[searchbox1.get()])
		except:
			lbl1.config(text="Invalid Search Entry")
	elif state==2:
		try:
			dict1[entrybox1.get()]=entrybox2.get();
		except:
			lbl1.config(text="Invalid Append Entry")
def searchfunc():
	global state
	state=1
	search.pack()
	append.pack_forget()
	

root=Tkinter.Tk()
root.title("Array Manipulator v1.0")
search=Tkinter.Frame(root)
search.pack()
appendbtn=Tkinter.Button(search, text="Append Mode", command=appendfunc)
appendbtn.pack()
append=Tkinter.Frame(root)
searchbtn=Tkinter.Button(append, text="Search Mode", command=searchfunc)
searchbtn.pack()
searchbox1=Tkinter.Entry(search)
searchbox1.pack()
enterbtn=Tkinter.Button(root, text="Enter", command=enterfunc)
enterbtn.pack()
lbl1=Tkinter.Label(root)
lbl1.pack()
entrybox1=Tkinter.Entry(append)
entrybox1.pack()
entrybox2=Tkinter.Entry(append)
entrybox2.pack()
root.mainloop()