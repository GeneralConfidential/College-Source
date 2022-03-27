#include<stdio.h> 
#include<string.h> 
#include<unistd.h> 
#include<fcntl.h> 

int main(){
    int fd = open("file.dat", O_RDWR); 
    char c;
    read(fd, &c, 1);   
    printf("fd = %d\n", fd);
    printf("c = %c\n", c); 
    write(fd,"hello\n",6);
    read(fd, &c, 1);
    printf("New c = %c\n", c);
}