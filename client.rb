require 'socket'
socket = TCPSocket.open('69.244.201.56',8091)
loop do
	puts socket.recv(1024)
	socket.print(gets())
	Gem.win_platform? ? (system "cls") : (system "clear")
end
