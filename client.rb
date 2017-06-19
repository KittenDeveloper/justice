require 'socket'
socket = TCPSocket.open('69.244.201.56',8091)
puts "Enter name: "
name = gets.chomp+": "
loop do
	puts socket.recv(1024)
	socket.print(name+gets())
	Gem.win_platform? ? (system "cls") : (system "clear")
end
