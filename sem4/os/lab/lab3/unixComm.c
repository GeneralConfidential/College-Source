#include<stdio.h>
void main(){
    printf("For ls:\n\n");
    system("ls");
    printf("\nFor cp:\n\n");
    system("touch copyMe.file");
    system("ls");
    system("cp copyMe.file copiedMe.file");
    system("ls");
    system("rm copyMe.file");
    system("rm copiedMe.file");
    printf("\nFor grep:\n(Finding llo in file woth text 'Hello World')\n\n");
    system("echo \"Hello World\" > file.dat ");
    system("grep llo file.dat");
}