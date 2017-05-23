function import(newfile){
document.body.innerHTML += '<div id="imports"></div>';
document.getElementById("imports").innerHTML += '<script type="text/javascript" src="'+newfile+'"></script>'
}