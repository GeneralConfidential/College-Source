#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
    //define loop iterator variable outside parallel region
    int i;
    int thread_id;
    omp_set_num_threads(2);
    #pragma omp parallel
    {
        thread_id = omp_get_thread_num();
        printf("Hello from thread: %d\n", thread_id);
        
    }
    return 0;
}
