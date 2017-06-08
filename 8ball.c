//Include those things
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//Clear screen
void clear()
{
    system("@cls||clear");
}

//Let the games begin
void eightball()
{
//Define the stuff
int rand1=rand()%4;
char userChar;
//clear(); I don't really need this do I?
printf("Enter question: ");
scanf("%c",&userChar);
while(getchar() != '\n')
{
    //do nothing
}
printf("%i",rand1);
if (rand1==0)
{
printf("Yes");
}
else if (rand1==1)
{
printf("No");
}
else if (rand1==2)
{
printf("Maybe");
}
else if (rand1==3)
{
printf("Try again later");
}
printf("\n");
eightball();
}
//Code starts here
int main()
{
srand(time(NULL));
//Goto 8 ball
eightball();
}
