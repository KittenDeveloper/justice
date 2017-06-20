require 'socket'
require 'digest/sha1'
require "base64"
server = TCPServer.new('localhost', 0)
port = server.addr[1]
statserver = TCPServer.new('localhost', 0)
statport = statserver.addr[1]
statserver.close

filenm=(0...50).map { ('a'..'z').to_a[rand(26)] }.join;
guifilec = File.new(filenm+".html", "w")
guifilec.close
egg= <<-HTMLGUI
<html>
<head>
<title>Chat App</title>
</head>
<div id="myDIV">Element</div>
<script>
function wait(ms){
   var start = new Date().getTime();
   var end = start;
   while(end < start + ms) {
     end = new Date().getTime();
  }
}
function send(req)
{
	var xhr = new XMLHttpRequest();
	xhr.open("GET", "https://localhost:#{port}/"+req, true);
	xhr.send();
	return xhr.statusText;
}
function end()
{
for (i=0; i < 12; i++){
send('QUIT:STOP:END');
wait(500);
}
window.close();
}
function hiruby(){
for (i=0; i < 5; i++){
document.getElementById("myDIV").innerHTML= send('HELLO:RUBY');
wait(500);
}
}
</script>
<body>
<button onclick="end()">END</button><br>
<button onclick="hiruby()">Hello Ruby</button></br>
</body>
</html>
HTMLGUI
IO.write(Dir.pwd+"/"+filenm+".html", egg)
httpthr = Thread.new {
system("ruby -run -e httpd . -p #{statport}")
}
system("open http://localhost:#{statport}/#{filenm}.html")
system("xdg-open http://localhost:#{statport}/#{filenm}.html")
system("start http://localhost:#{statport}/#{filenm}.html")

loop do
  socket = server.accept
  request = socket.recv(1024)
  puts request;
  if request.include? "HELLO:RUBY"
  response= "Hi JavaScript";
  end
  if request.include? "QUIT:STOP:END"
  socket.close
  httpthr.exit
  File.delete(filenm+".html");
  abort("RECIEVED QUIT:STOP:END; Exiting");
  end
  response = "Hello World!\n"
  socket.print "HTTP/1.1 200 OK\r\n" +
				"Access-Control-Allow-Origin: *\r\n"+
				"Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE\r\n"+
				"Access-Control-Max-Age: 86400\r\n"+
               "Content-Type: text/plain\r\n" +
               "Content-Length: #{response.bytesize}\r\n" +
               "Connection: close\r\n"
  socket.print "\r\n"
  socket.print response
  socket.close
end
