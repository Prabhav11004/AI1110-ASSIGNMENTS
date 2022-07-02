// Calculates the mean and variance of a uniform distribution



#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "mean_var.h"

#define NUM 1000000

int main() {
	double *data = readData("uni.dat", 1000000);
	
	printf("Empirical Mean = %lf\n", mean(data, 1000000));
	

	printf("Empirical Variance = %lf\n", variance(data, 1000000));
	

	return 0;
}