#PyRokuRemote
import httplib
import Tkinter
import socket
import time
import os
from time import sleep

os.system('sudo apt-get install python-tk')

rootmn = Tkinter.Tk()
rootmn.title=("Roku Remote")

global commandinput
global rokuip
rokuip=""
def ipfunc():
	global rokuip
	rokuip = rokubox.get()
	try:
		socket.inet_aton(rokuip)
		allowedip = 1
		#correct
	except socket.error:
		# Not valid
		allowedip=0
	if allowedip==1:
		root.pack()
	else:
		root.pack_forget()

def sendcmd():
	global commandinput
	h = httplib.HTTPConnection(rokuip + ':8060')
	url = '/keypress/'+ commandinput
	h.request('POST', url)
def upbtn():
	global commandinput
	commandinput = 'up'
	sendcmd()
def downbtn():
	global commandinput
	commandinput = 'down'
	sendcmd()
def leftbtn():
	global commandinput
	commandinput = 'left'
	sendcmd()
def rightbtn():
	global commandinput
	commandinput = 'right'
	sendcmd()
def selectbtn():
	global commandinput
	commandinput = 'select'
	sendcmd()
def playbtn():
	global commandinput
	commandinput = 'play'
	sendcmd()
def fwdbtn():
	global commandinput
	commandinput = 'fwd'
	sendcmd()
def revbtn():
	global commandinput
	commandinput = 'rev'
	sendcmd()
def backbtn():
	global commandinput
	commandinput = 'back'
	sendcmd()
def homebtn():
	global commandinput
	commandinput = 'home'
	sendcmd()
def keyloop():
	cips=0
	keyinput = keyenter.get()	
	while cips < (len(keyinput)):
		h = httplib.HTTPConnection(rokuip + ':8060')
		if keyinput[-1*(len(keyinput)):][cips] == ' ':
			url = '/keypress/'+ "lit_"+'%20'
		else:
			url = '/keypress/'+ "lit_"+keyinput[-1*(len(keyinput)):][cips]
		h.request('POST', url)
		cips = cips +1
		sleep(0.1)
def clearfunc():
	cips2=0
	while cips2 < 50:
		sendclear()
		cips2 = cips2 + 1
def sendclear():
	url = '/keypress/'+ 'backspace'
	h = httplib.HTTPConnection(rokuip + ':8060')
	h.request('POST', url)

enteripbtn1 = Tkinter.Button(rootmn, text="Enter Roku IP:", command=ipfunc, bg="black", fg="white" )
enteripbtn1.pack()

rokubox = Tkinter.Entry(rootmn)
rokubox.pack()

root = Tkinter.Frame(rootmn)
root.pack_forget()

keyenter= Tkinter.Entry(root)
keyenter.grid(column=2, row=7)

clearbtn1=Tkinter.Button(root, text="Clear", command=clearfunc)
clearbtn1.grid(column=3,row=7)

typebtn1=Tkinter.Button(root, text="Type", command=keyloop)
typebtn1.grid(column=1,row=7)

homebtn1 = Tkinter.Button( root, text="Home", command=homebtn, bg="black", fg="white" )
homebtn1.grid(column=1, row=1)

backbtn1 = Tkinter.Button( root, text="Back", command=backbtn, bg="black", fg="white" )
backbtn1.grid(column=3, row=1)

upbtn1 = Tkinter.Button( root, text="UP", command=upbtn, bg="purple" , fg="white")
upbtn1.grid(column=2, row=2)

downbtn1 = Tkinter.Button ( root, text="DOWN", command=downbtn , bg="purple", fg="white")
downbtn1.grid(column=2, row=4)

rightbtn1 = Tkinter.Button ( root, text="RIGHT", command=rightbtn , bg="purple", fg="white")
rightbtn1.grid(column=3, row=3)

leftbtn1 = Tkinter.Button ( root, text="LEFT", command=leftbtn , bg="purple", fg="white")
leftbtn1.grid(column=1, row=3)

selectbtn1 = Tkinter.Button ( root, text="OK", command=selectbtn, bg="purple" , fg="white")
selectbtn1.grid(column=2, row=3)

fwdbtn1 = Tkinter.Button ( root, text=">>", command=fwdbtn, bg="black", fg="white" )
fwdbtn1.grid(column=3, row=5)

revbtn1 = Tkinter.Button ( root, text="<<", command=revbtn, bg="black" , fg="white")
revbtn1.grid(column=1, row=5)

playbtn1 = Tkinter.Button ( root, text="PLAY", command=playbtn, bg="black", fg="white" )
playbtn1.grid(column=2, row=5)


root.mainloop()
