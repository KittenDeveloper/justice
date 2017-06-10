var http = require('http');
var fs = require('fs');
function write(input)
{
fs.appendFile('chat.txt', input+'<br>\n', function (err) {
	if (err) throw err;
});
}
http.createServer(function (req, res) {
	fs.readFile('form.html', function(err, data){
	fs.readFile('chat.txt', function(err1, chatdata){
	res.writeHead(200, {'Content-Type': 'text/html'});
	res.write(chatdata+'<br>'); //write a response to the client		
	res.write(data); //write a response to the client
	var input =req.url.slice(1);
	if (input.substring(0,11)=='favicon.ico'){input=input.slice(11)};
	if (input!=''){write(input); res.write('<meta http-equiv="refresh" content="0; url=http://jcode.selfip.com:34113/" />');}
	res.end(); //end the response
});});}).listen(34113);