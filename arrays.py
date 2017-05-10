import Tkinter
import csv

global state
global dict
dict1={}
state=1

def appendfunc():
	global state
	searchbtn.pack(side='top')
	state =2
	search.pack_forget()
	append.pack()
	entrybox1.delete(0, 'end')
	entrybox2.delete(0, 'end')

def enterfunc():
	global dict1
	global state
	if state == 1:
		try:
			with open('example.csv', 'rb') as csv_file:
				reader = csv.reader(csv_file)
				mydict = {rows[0]:rows[1] for rows in reader}
				lbl1.config(text=mydict[searchbox1.get()])
		except:
			lbl1.config(text="Invalid Search Entry")
	elif state==2:
		try:
			dict1[entrybox1.get()]=entrybox2.get();
			with open('example.csv', 'wb') as csv_file:
				writer = csv.writer(csv_file)
				for key, value in dict1.items():
				   writer.writerow([key, value])
		except:
			lbl1.config(text="Invalid Append Entry")
		csv_file.close()
def searchfunc():
	global state
	state=1
	searchbtn.pack_forget()
	search.pack()
	append.pack_forget()
	searchbox1.delete(0, 'end')
	

root=Tkinter.Tk()
root.title("Array Manipulator v1.0")
search=Tkinter.Frame(root)
search.pack()
append=Tkinter.Frame(root)
enterbtn=Tkinter.Button(root, text="Enter", command=enterfunc)
enterbtn.pack(side='bottom')
lbl1=Tkinter.Label(root)
lbl1.pack()
searchbox1=Tkinter.Entry(search)
searchbox1.grid(column=1, row =2)
appendbtn=Tkinter.Button(search, text="Append Mode", command=appendfunc)
appendbtn.grid(column=1,row =1)
searchbtn=Tkinter.Button(root, text="Search Mode", command=searchfunc)
entrybox1=Tkinter.Entry(append)
entrybox1.grid(column=1, row =2)
entrybox2=Tkinter.Entry(append)
entrybox2.grid(column=2,row=2)
root.mainloop()