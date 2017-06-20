import java.awt.*;  
import javax.swing.*;
import java.awt.event.*;
import java.io.*;
import java.nio.file.*;
public class textedit{
JFrame f;  
textedit(){  
	f=new JFrame();		
	final Runtime rt = Runtime.getRuntime();
	f.setLayout(new GridLayout(2,1));
	f.setTitle("Awesome CodeEditor");
	JTextArea txt1=new JTextArea("");
	f.add(txt1);
	JPanel menus =new JPanel();
	menus.setLayout(new GridLayout(2,2));
	JTextField displaypath = new JTextField("File Dir");
	menus.add(displaypath);
	JTextField file = new JTextField("File");
	menus.add(file);
	JButton btn1=new JButton("Open File");
	menus.add(btn1);
	JButton btn2=new JButton("Save File");
	btn2.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e){
		try{
		File currentfile = new File(displaypath.getText()+file.getText());
		FileOutputStream filestream = new FileOutputStream(currentfile, false);
		filestream.write(txt1.getText().getBytes());
		filestream.close();
		}
		catch(IOException ioex){
		txt1.setText(ioex.getMessage());
		}
		}});
	menus.add(btn2);
	btn1.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e){  
		FileDialog fd = new FileDialog(f, "Choose a file", FileDialog.LOAD);
		fd.setDirectory("C:\\");
		fd.setVisible(true);
		String filename = fd.getFile();
		String filedir = fd.getDirectory();
		try{
        String content = new String(Files.readAllBytes(Paths.get(filedir+filename)));
		txt1.setText(content);
		displaypath.setText(filedir);
		file.setText(filename);
		}
		catch(IOException ioex){
		txt1.setText(ioex.getMessage());
		}
		;}});
	JTextField command = new JTextField("");
	menus.add(command);
	String[] languages = {"Java","C/C++","Other"};
	JComboBox langselect = new JComboBox(languages);
	langselect.setSelectedIndex(2);
	langselect.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e){
		switch(langselect.getSelectedItem().toString()){
			case "Java" :
				command.setText("javac $filepath$filename;;;jar -cfe $filename.jar $filename.class $filename.class");
				break;
			case "C/C++":
				command.setText("gcc $filepath$filename -o $filename.bin;;;./$filename.bin");
				break;
			case "Other":
				command.setText("");
				break;
		}
		;}});
	menus.add(langselect);
	JButton compilebtn = new JButton("Compile as "+langselect.getSelectedItem().toString()+" code");
	compilebtn.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e){
		try{
		rt.exec(command.getText().split(";;;")[0].replace("$filepath",displaypath.getText()).replace("$filename",file.getText()));
		}
		catch(IOException ioex){
		txt1.setText(ioex.getMessage());}
		;}});
	menus.add(compilebtn);
	JButton runbtn = new JButton("Make class .jar (JAVA ONLY) //BROKEN");
	runbtn.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e){
		try{
		rt.exec(command.getText().split(";;;")[1].replace("$filepath",displaypath.getText()).replace("$filename",file.getText()));
		}
		catch(IOException ioex){
		txt1.setText(ioex.getMessage());}
		;}});
	menus.add(runbtn);
	f.add(menus);
	menus.setSize(300, 300);
	menus.setVisible(true);
	f.setSize(300,300);  
	f.setVisible(true);  
}
public static void main(String[] args) {  
	new textedit();
}
}