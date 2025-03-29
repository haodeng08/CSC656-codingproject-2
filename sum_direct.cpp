#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>

#include "sums.h"

void 
setup(int64_t N, double A[])
{
   printf(" inside direct_sum problem_setup, N=%lld \n", N);
}

double
sum(int64_t N, double A[])
{
   printf(" inside direct_sum perform_sum, N=%lld \n", N);
   
   double result = 0.0;
   
   for (int64_t i = 0; i < N; i++) {
       result += i;
   }
   
   return result;
}