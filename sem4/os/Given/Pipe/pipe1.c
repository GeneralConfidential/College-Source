// C program to illustrate
// pipe system call in C
#include <stdio.h>
#include <unistd.h>
#define MSGSIZE 16
char* msg1 = "hello, world #1";
char* msg2 = "hello, world #2";
char* msg3 = "hello, world #3";

int main()
{
	char inbuf[MSGSIZE];
	int p[2], i;

        /*
          int pipe(int fds[2]);

	  Parameters :
	  fd[0] will be the fd(file descriptor) for the read end of pipe.
	  fd[1] will be the fd for the write end of pipe.

          Returns : 0 on Success. -1 on error.        
        */

	if (pipe(p) < 0)
		exit(1);

	/* continued */
	/* write pipe */

	write(p[1], msg1, MSGSIZE); // "hello, world #1" written to pipe from end 1
	write(p[1], msg2, MSGSIZE); // "hello, world #2" written to pipe from end 1
	write(p[1], msg3, MSGSIZE); // "hello, world #3" written to pipe from end 1

	for (i = 0; i < 3; i++) {
		/* read pipe */
		read(p[0], inbuf, MSGSIZE); // Message read into inbuf array from end 0 of pipe
		printf("% s\n", inbuf);     // Print string from inbuf
	}
	return 0;
}

