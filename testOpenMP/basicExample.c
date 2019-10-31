#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#define NTHREADS 4

int main()
{
    int numberTd = NTHREADS, idThread = -1;
#pragma omp parallel if (numberTd >= 1) num_threads(numberTd) default(none) private(idThread) shared(numberTd)
    {
        // Obtem o identificador de thread
        idThread = omp_get_thread_num();
        printf("Thread %d: Hello!\n", idThread);
        if (numberTd != omp_get_num_threads())
            printf("Error: NTHREADS\n");
    }
    printf("Thread %d: Bye!\n", idThread);
}