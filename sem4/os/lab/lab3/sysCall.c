#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
void main(){
	int pid;
	pid = fork();
	if(pid==-1){
		printf("Error");
		exit(1);
	}
	pid = fork();
	if(pid==-1){
		printf("Error");
		exit(1);
	}
	if(pid==0){
		printf("Parent PID = %d\n",getppid());
	}
	else{
		printf("Child PID = %d\n",pid);
	}
	exit(0);
}

