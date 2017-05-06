import sys
import httplib
# i did that
print("RokuRemote Version 1.0| type help for more info")
rokuip = raw_input('What is your rokus ip: ')
if rokuip == "":
	rokuip = "192.168.200.9"
def sendclear():
	url = '/keypress/'+ 'backspace'
	h = httplib.HTTPConnection(rokuip + ':8060')
	h.request('POST', url)
def mainrequest():
	commandinput = raw_input('Enter Command: ')
	
	cips = 0
	cips2 = 0
	if commandinput == 'help':
		print("Commands are as follows:")
		print("Home, Rev, Fwd, Play, Select, Left, Right, Down, Up, Back,")
		print("InstantReplay, Info, Backspace, Search, Enter.")
		print("Special command: keyboard:(TEXT)")
		print("BETA:Special command: launch/(APP_ID) for example 12 is the id of the app netflix so launch/12 would launch netflix")
		print("For more information goto:", "https://sdkdocs.roku.com/display/sdkdoc/External+Control+Guide")
		print("quit to quit")
		mainrequest()
	elif commandinput[:6] == 'clear:':
		while cips < 50:
			sendclear()
			cips = cips + 1	
		mainrequest()
	elif commandinput[:9] == 'keyboard':
		while 1:
			keyinput = raw_input('/quit and to return or /clear to clear ')
			if keyinput == '/quit': break
			if keyinput =='/clear': 
				while cips2 < 50:
					sendclear()
					cips2 = cips + 1	
			while cips < (len(keyinput)):
				h = httplib.HTTPConnection(rokuip + ':8060')
				if keyinput[-1*(len(keyinput)):][cips] == ' ':
					url = '/keypress/'+ "lit_"+'%20'
				else:
					url = '/keypress/'+ "lit_"+keyinput[-1*(len(keyinput)):][cips]
				h.request('POST', url)
				cips = cips +1
		mainrequest()
			
	elif commandinput == 'quit':
		sys.exit("Bye!")
	elif commandinput[:6] == 'launch':
		h = httplib.HTTPConnection(rokuip + ':8060')
		url = '/'+ commandinput
		h.request('POST', url)
		mainrequest()
		
	else:
		h = httplib.HTTPConnection(rokuip + ':8060')
		url = '/keypress/'+ commandinput
		h.request('POST', url)
		mainrequest()
mainrequest()
