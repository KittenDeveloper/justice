#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32
#include <conio.h>
void clrscr()
{
	system("@cls");
}
#endif

#ifndef _WIN32
#include <termios.h>
#include <unistd.h>

void clrscr()
{
    system("clear");
}
/* reads from keypress, doesn't echo */
int getch(void)
{
    struct termios oldattr, newattr;
    int ch;
    tcgetattr( STDIN_FILENO, &oldattr );
    newattr = oldattr;
    newattr.c_lflag &= ~( ICANON | ECHO );
    tcsetattr( STDIN_FILENO, TCSANOW, &newattr );
    ch = getchar();
    tcsetattr( STDIN_FILENO, TCSANOW, &oldattr );
    return ch;
}
#endif
int i=0;
int y=0;
int xpos =0;
int ypos =0;
char grid[10][10];
char uinp;

void coordmaker(uinp)
{
if (uinp=='w'&&ypos != 0)
{
--ypos;
}
if (uinp=='a'&&xpos !=0)
{
--xpos;
}
if (uinp=='s'&&ypos !=10)
{
++ypos;
}
if (uinp=='d'&&xpos != 10)
{
++xpos;
}
writer();
}
int writer(){
clrscr();
while(1){
if (y==11){break;}
while(1){
if (i==11){break;}
grid[i][y]='O';
i++;
}
y++;
i=0;
}
i=0;
y=0;
grid[ypos][xpos]='X';
for(int i = 0; i < 10; i++) {
    for(int y = 0; y <10; y++) {
        printf("%c", grid[i][y]);
    }
    printf("\n");
} 
printf("%i,%i",xpos,ypos);
return 1;
}
void main(){
writer();
while (1){
char ch;
ch = getch();
coordmaker(ch);
}
}