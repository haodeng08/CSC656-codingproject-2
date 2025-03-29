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
   printf(" inside sum_vector problem_setup, N=%lld \n", N);
   
   // Initialize array A with values from 0 to N-1
   for (int64_t i = 0; i < N; i++) {
       A[i] = (double)i;
   }
}

double
sum(int64_t N, double A[])
{
   printf(" inside sum_vector perform_sum, N=%lld \n", N);
   
   double result = 0.0;
   
   // Sum all elements in the array sequentially
   for (int64_t i = 0; i < N; i++) {
       result += A[i];
   }
   
   return result;
}