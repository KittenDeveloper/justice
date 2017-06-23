import subprocess
outp = subprocess.Popen("ifconfig")
print "Content-Type: text/html"
print
import re
m = re.search('/(?=inet addr:)(192\.\d+\.\d+\.\d+)(?=   Bcast:192\.\d+\.\d+\.\d+)/', outp)
print """
<html>
<head>
<title>IPV4</title>
</head>
<h1>Server's IP:"""+m.group(0)+"""</h1>
<body></body bgcolor="blue">
</html>
"""
