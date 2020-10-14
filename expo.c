#include<stdio.h>
int main(){
	long n=10;
	int i;
	for(i = 0; i< n; i++)
	{
		printf("Hello %d\n",n);
		n=2*n;
	}
	return 0;
}
