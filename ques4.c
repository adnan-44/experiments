#include<stdio.h>
int main(){
	int cars[50];
	int fine=100, day,no,check;
	scanf("%d %d",&no,&day);
	for(int i=0; i<no; i++)
	scanf("%d",&cars[i]);

	int tot_fine = 0;

	//traversing elements
    for (int i = 0; i < no; i++)
			//condition if date and car are even or not
        if (((cars[i] ^ day) & 1) == 1){
					check = cars[0];
					for(int j=0;j<i;j++){
						if(cars[j]==check){
							tot_fine += 200;
							break;
						}
						else{
							tot_fine += fine;
							break;}
					}
				}

    printf("Fine is %d\n",tot_fine );
}
