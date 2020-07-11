#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
void Algorithm1(int a, int b, int *resul);
int main(int argc, char *argv[]) {
	int a, b;
	int resul[3];
	printf ("Ingrese el valor de a:\t");
	scanf ("%d", &a);
	printf ("Ingrese el valor de b:\t");
	scanf ("%d", &b);
	Algorithm1(a, b, resul);
	printf ("%d %d %d",resul[0],resul[1],resul[2]);
	return 0;
}

void Algorithm1 (int a, int b, int *resul){
	int u,v,q,r,x1,x2,y1,y2,x,y, d;
	u=a;
	v=b;
	x1=1;
	y1=0;
	x2=0;
	y2=1;
			printf ("u\tv\tq\tr\tx1\tx2\ty1\ty2\tx\ty\n");
	while(u!=0)
	{
		q=v/u;
		r=v-(q*u);
		x=x2-(q*x1);
		y=y2-(q*y1);
		
		v=u;
		u=r;
		x2=x1;
		x1=x;
		y2=y1;
		y1=y;
		
		printf ("%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n",u,v,q,r,x1,x2,y1,y2,x,y);
	}
	d=v;
	x=x2;
	y=y2;
	resul[0]=d;
	resul[1]=x;
	resul[2]=y;
	
}
