#PyRokuRemote
import httplib
import Tkinter
from Tkinter import *


root = Tk()
root.title=("Roku Remote")
global commandinput
global rokuip
rokuip=""
def ipfunc():
	global rokuip
	rokuip = rokubox.get()
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
rokubox = Entry(root)
rokubox.grid(column=1, row=6)

enterip = Button(root, text="Enter IP", command=ipfunc)

homebtn1 = Button( root, text="Home", command=homebtn, bg="black", fg="white" )
homebtn1.grid(column=1, row=1)

backbtn1 = Button( root, text="Back", command=backbtn, bg="black", fg="white" )
backbtn1.grid(column=3, row=1)

upbtn1 = Button( root, text="UP", command=upbtn, bg="purple" , fg="white")
upbtn1.grid(column=2, row=2)

downbtn1 = Button ( root, text="DOWN", command=downbtn , bg="purple", fg="white")
downbtn1.grid(column=2, row=4)

rightbtn1 = Button ( root, text="RIGHT", command=rightbtn , bg="purple", fg="white")
rightbtn1.grid(column=3, row=3)

leftbtn1 = Button ( root, text="LEFT", command=leftbtn , bg="purple", fg="white")
leftbtn1.grid(column=1, row=3)

selectbtn1 = Button ( root, text="OK", command=selectbtn, bg="purple" , fg="white")
selectbtn1.grid(column=2, row=3)

fwdbtn1 = Button ( root, text=">>", command=fwdbtn, bg="black", fg="white" )
fwdbtn1.grid(column=3, row=5)

revbtn1 = Button ( root, text="<<", command=revbtn, bg="black" , fg="white")
revbtn1.grid(column=1, row=5)

playbtn1 = Button ( root, text="PLAY", command=playbtn, bg="black", fg="white" )
playbtn1.grid(column=2, row=5)


root.mainloop()