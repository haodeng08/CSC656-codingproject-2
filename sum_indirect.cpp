#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>

#include "sums.h"

// Global array for indices
static std::vector<int64_t> indices;

void 
setup(int64_t N, double A[])
{
   printf(" inside sum_indirect problem_setup, N=%lld \n", N);
   
   // Fill A[] with values from 0 to N-1
   for (int64_t i = 0; i < N; i++) {
       A[i] = (double)i;
   }
   
   // Initialize and fill indices array with random values in range 0..N-1
   indices.resize(N);
   for (int64_t i = 0; i < N; i++) {
       indices[i] = lrand48() % N;  // Using lrand48() as specified in the assignment
   }
}

double
sum(int64_t N, double A[])
{
   printf(" inside sum_indirect perform_sum, N=%lld \n", N);
   
   double result = 0.0;
   
   // Indirect sum: follow random indices to access values in A[]
   for (int64_t i = 0; i < N; i++) {
       result += A[indices[i]];
   }
   
   return result;
}