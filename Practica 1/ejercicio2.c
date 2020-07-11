//segundo ejercicio de algoritmos 
#include<stdio.h>


int main(){
	int n,i,k,j;
	
	printf("ingrese el tamaño de matriz que quiera:\t");
	scanf("%d",&n);
	int a[n];
	int aux=0;
	for(int i=0;i<n;i++){
		printf("introduce el valor que quieres:\t");
		scanf("%d",&a[i]);
	}
	int A[n][n];
	for(i=0;i<n;i++){
		aux=a[i];
		for(j=0;j<n;j++){
			A[i][j]=0;
			if (i<j){
				aux=aux + a[j];
				A[i][j]=aux;

			}
			printf("%d\t",A[i][j]);
		}
		aux=0;
		printf ("\n");
	}
	
}
