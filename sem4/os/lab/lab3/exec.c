#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
void main(){
    char * args[] = {"ls","-la",".",NULL};
    execvp("ls",args);
    wait(NULL);
    exit(0);
}
