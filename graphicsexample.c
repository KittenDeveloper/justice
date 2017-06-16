#include <stdio.h>
//define struct
typedef struct grids{
	int x;
	int y;
	int xmouse;
	int ymouse;
	char cursorchar;
	char stanchar;
} grid_info;
//Grid size rows columns
char grid[10][10];
//Add main grid (discussed later)
grid_info maingrid;
//Tell c to use the library
#include "conemod.c"
int main(){
	
	//Define properties of main grid
	//Rows and columns - 1
	maingrid.x=9;
	maingrid.y=9;
	//Default position of mouse ((0, 0) is start)
	maingrid.xmouse=0;
	maingrid.ymouse=0;
	//Cursor apperance
	maingrid.cursorchar='X';
	//Background
	maingrid.stanchar='_';
	
	//Define new graphic object
	GraphObj object1;
	//Location of object (starting from 0,0)
	object1.xpos=2;
	object1.ypos=2;
	//apperance of object
	object1.objchar='S';
	
	printf("WASD to move, Get to the S");
	printf("Press any key to start");
	//Clear screen
	cleargrid();
	//Main loop
	while(1){
	//Initialize our object
	initObj(object1);
	//Wait for input and change cursor accordingly (Automatic)
	acursor();
	//Write screen
	writegrid();
	//Check if cursor is within 1 position our object
	if (cursorcmp(object1, 0)==1){printf("You Win"); exit(0);}
	}
	}
	// There are many things about this library
// for example getch() is included by defualt (*nix compatible).
// this example only showed a basic example. here's a list other things 
// you may need to know:
// objcmp(Object1, Object2, range)
// this takes two objects and checks if they are within x range
// the screen can be accesed directly though the grid[][] array
// for instance grid[2][3]='K'; makes 3,2 K or you can get values
// grid[2][3] will return the current value of 3,2 so you could put

// grid[1][2]='G';
// writegrid();
// printf("\nValue of (2,1) is: %c",grid[1][2]);

// This example will write G to the screen at (2,1) and print
// Value of (2,1) is: G

//In this library you do not 