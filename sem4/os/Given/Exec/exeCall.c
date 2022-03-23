#include<stdio.h>
#include<dirent.h>
struct dirent *dptr;
int main(){
    char dir[100];
    DIR *dirp;
    printf("\nInput Directory:");
    scanf("%s", dir);
    if((dirp=opendir(dir))==NULL){
        printf("Error. Given directory not found.\n");
        exit(1);
    }
    while(dptr=readdir(dirp)){
        printf("%s\n",dptr->d_name);
    }
}