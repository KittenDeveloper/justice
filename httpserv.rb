begin
require 'socket'
require 'date'
logfile = File.open("serverlog.log", "a+")
Signal.trap("TERM"){
	logfile.syswrite("\n|Closing Server at: #{Time.now}|\n")
	puts ("\n|Closing Server at: #{Time.now} (Logged)|\n")
	abort("Bye!")
}
Signal.trap("INT") {
	logfile.syswrite("\n|Closing Server at: #{Time.now}|\n")
	puts ("\n|Closing Server at: #{Time.now} (Logged)|\n")
	abort("Bye!")
}
if (!(File.file?("server_settings.config")))
server = TCPServer.new('', 0)
port = server.addr[1]
configfile = File.open("server_settings.config", "a+")
configfile.syswrite(port.to_s+";;;")
configarr=configfile.read.split(";;;")
else
configfile = File.open("server_settings.config", "a+")
configarr=configfile.read.split(";;;")
port = configarr[0]
server = TCPServer.new('', port)
end
	mimeconf = File.open("mime.config", "r")
	mimearr=mimeconf.read.split(";;;")
puts ("Settings: " + configarr.join(";;;"))
puts ("Mode is: " + configarr[1].to_s)

puts "Port is: #{port}"
puts ""
accepted_formats=[".html",".gif",".png",".jpeg",".jpg",".bmp",".txt",".js","mp3",".ogg",".wav","mp4"]
def web_throw(errortype, socket)
if errortype==404
	socket.print "HTTP/1.1 200 OK\r\n" +
	"Content-Type: text/html\r\n" +
	"Content-Length: #{"<html><head><title>404 Error</title><h1>404 Page not found.</h1></head><br><body bgcolor=\"red\">This is not the page you are looking for.</body></html>".bytesize}\r\n" +
	"Connection: close\r\n"
	socket.print "\r\n"
	socket.print "<html><head><title>404 Error</title><h1>404 Page not found.</h1></head><br><body bgcolor=\"red\">This is not the page you are looking for.</body></html>"
	socket.close
	logfile.syswrite("(Sending 404)")
end
if errortype==403
	socket.print "HTTP/1.1 200 OK\r\n" +
	"Content-Type: text/html\r\n" +
	"Content-Length: #{"<html><head><title>403 Error</title><h1>403 Forbidden.</h1></head><br><body bgcolor=\"red\">You shouldn't be here, pal.</body></html>".bytesize}\r\n" +
	"Connection: close\r\n"
	socket.print "\r\n"
	socket.print "<html><head><title>403 Error</title><h1>403 Forbidden.</h1></head><br><body bgcolor=\"red\">You shouldn't be here, pal.</body></html>"
	socket.close
	logfile.syswrite("(Sending 403)")
end
end
loop do
	socket = server.accept
	request = socket.recv(1024)
	puts request;
	getreq = request[(/(?=GET \/)(.*)(?= HTTP)/)][5..-1]
	exten = File.extname(getreq).downcase
	if (accepted_formats.include?(exten))
	if configarr[1]=="diag"
	puts "REQINF"
	puts getreq
	puts exten
	end
	type="text/html"
	if File.file?(getreq)
	if File.exists?(getreq)
	if exten ==".html"
	webpage = File.open(getreq, "r")
	response=webpage.read
	elsif exten == ".png"
	type="image/png"
	puts "IMGREQ"
	webpage=File.open(getreq,"rb")
	response=webpage.read
	elsif exten == ".jpeg"||exten==".jpg"
	type="image/jpeg"
	webpage=File.open(getreq,"rb")
			response=webpage.read
	elsif exten == ".gif"
	webpage=File.open(getreq,"rb")
			response=webpage.read
			type="image/gif"
	elsif exten == ".bmp"
	webpage=File.open(getreq,"rb")
			response=webpage.read
			type="image/bmp"
	elsif exten == ".mp3"
	webpage=File.open(getreq,"rb")
			response=webpage.read
	type="audio/mpeg"
	elsif exten == ".ogg"
	webpage=File.open(getreq,"rb")
			response=webpage.read
	type="audio/ogg"
	elsif exten == ".wav"
	webpage=File.open(getreq,"rb")
			response=webpage.read
	type="audio/wav"
	end
	end
	end
	elsif request.include?("GET /favicon.ico HTTP/1.1")
		type="image/png"
		if (!(configarr[2] rescue false) || configarr[2]=='def')
		if File.file?("favicon.ico") 
		response = File.open("favicon.ico")
		type=configarr[2].split("::")[1]
		else
		puts "No favicon found (Sending 404)"
		web_throw(404, socket)
		redo
		end
		else
		webpage=File.open(configarr[2].split("::")[0], "rb")
		response=webpage.read
		end
	elsif request.include?("GET / HTTP/1.1")
	type="text/html"
	puts "GENREQ"
	webpage = File.open("index.html", "r")
	response=webpage.read
	elsif mimearr.include?(exten)
	for i in 0..mimearr.size-1
		if exten==mimearr[i].split("::")[0]
		type = mimearr[i].split("::")[1]
		if !(['text/plain', 'text/html', 'text/css', 'text/javascript'].include?(type))
		webpage=File.open(getreq,"rb")
		response=webpage.read
		else
		webpage = File.open(getreq, "r")
		response=webpage.read
		end
		break
		end
		end

	
	elsif (exten==".pl"&&File.file?("perl-cgi-enable-linux"))
	system("QUERY_STRING='#{getreq.split("?")[1]}'")
	perlout=(IO.popen("sudo -H -u rbserveruser perl #{getreq.split("?")[0]}").readlines.join("\n"))
	socket.print "HTTP/1.1 200 OK\r\n" +
	"Connection: close" +
	"Content-Length: #{perlout.to_s.bytesize}\r\n"
	socket.print(perlout)
	puts perlout
	redo
	elsif (exten==".py"&&File.file?("python-cgi-enable-linux"))
	pythonout=(IO.popen("sudo -H -u rbserveruser python #{getreq.split("?")[0]}").readlines.join("\n"))
	socket.print "HTTP/1.1 200 OK\r\n" +
	"Connection: close" +
	"Content-Length: #{pythonout.to_s.bytesize}\r\n"
	socket.print(pythonout)
	redo
	elsif File.file?(getreq)
	web_throw(403, socket)
	puts "(Sending 403)"
	redo
	else
	web_throw(404, socket)
	puts "(Sending 404)"
	redo
	end
	puts "Bytesize: '#{response.to_s.bytesize}'"
	if (response.to_s.bytesize.to_i <= 0)
	puts "ByteError (Sending 404)"
	web_throw(404, socket)
	redo
	end
	logfile.syswrite(request +"\n#{Time.now}\n\n")
	socket.print "HTTP/1.1 200 OK\r\n" +
	"Content-Type: #{type}\r\n" +
	"Content-Length: #{response.to_s.bytesize}\r\n" +
	"Connection: close\r\n"
	socket.print "\r\n"
	socket.print response
	socket.close
end
rescue StandardError => err
	#Main Error Handler
	logfile.syswrite("\n|EXCEPTION OCCURRED|\n \n|CHECK SERVER_ERROR.LOG FOR DETAILS|\n")
	errlog = File.open("server_error.log", "a+")
	errlog.syswrite("\n|EXEPTION AT #{Time.now}|\nIn: #{err.backtrace}\nMessage: #{err.message}\n|END EXEPTION|\n")
	errlog.close
	puts ("\n|EXEPTION|\nIn: #{err.backtrace}\nMessage: #{err.message}\n|END EXEPTION|\n")
	abort("Error written to log, Exiting")
end
