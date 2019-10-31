#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include<time.h>
#define NTHREADS 20
#define faninSize 50000
#define fanoutSize 20000

int main()
{

	double fanin_cost = 0;
	double fanout_cost = 0;
    int numberTd = NTHREADS;
    int idThread = -1;
    double inicio, fim;

    inicio = omp_get_wtime();
#pragma omp parallel for reduction(+: fanin_cost) num_threads(numberTd) private(idThread)
	for (int i = 0; i < faninSize; i++)
	{
        //22 * faninSize
        idThread = omp_get_thread_num();
        // printf("Thread %d: Hello!\n", idThread);
        if (numberTd != omp_get_num_threads()) printf("Error: NTHREADS\n");
		int fanin_loc = 10;
		fanin_cost += pow(fanin_loc,2);
		fanin_cost += pow(fanin_loc,5);
	}

    // printf("Segundo for\n");
#pragma omp parallel for reduction(+: fanout_cost) num_threads(numberTd)
	for (int i = 0; i < fanoutSize; i++)
	{
        //12 * fanoutSize
        idThread = omp_get_thread_num();
        // printf("Thread %d\n", idThread);
        if (numberTd != omp_get_num_threads()) printf("Error: NTHREADS\n");
        int fanout_loc = 5;
		fanout_cost += pow(fanout_loc,10);
		fanout_cost += pow(fanout_loc,15);
	}
    int total_cost = fanin_cost + fanout_cost;
    fim = omp_get_wtime();
	printf("Custo total: %d",total_cost);
    printf("The elapsed time = %e seconds\n", fim-inicio);

}
