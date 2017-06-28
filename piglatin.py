import sys
if (len(sys.argv)>2):
	print("Usage: "+sys.argv[0]+" \"string to convert\"")
	exit()
def convertword(x):
	firstchar=x[0]
	modifiedword=x[1:]
	return modifiedword+firstchar+"ay"
def convertstring(x):
	return list(map(convertword,x.split(" ")))
print(convertstring(sys.argv[1]).join(" "))
