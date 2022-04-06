#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *prt( void *ptr ){
     sleep(10);
     char *message;
     message = (char *) ptr;
     printf("%s \n", message);
}

void main(){
     pthread_t t1, t2;
     char *message1 = "Thread 1";
     char *message2 = "Thread 2";
     int  iret1, iret2;

     iret1 = pthread_create( &t1, NULL, prt, (void*) message1);
     iret2 = pthread_create( &t2, NULL, prt, (void*) message2);

     pthread_join( t1, NULL);
     pthread_join( t2, NULL); 

     printf("Thread 1 returns: %d\n",iret1);
     printf("Thread 2 returns: %d\n",iret2);
     exit(0);
}