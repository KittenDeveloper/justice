function import(newfile){
   elem = document.createElement("div");
   elem.id = 'myImports';
   elem.innerHTML += '<script type="text/javascript" src="'+newfile+'"></script>'
   document.body.insertBefore(elem,document.body.childNodes[0]);
}