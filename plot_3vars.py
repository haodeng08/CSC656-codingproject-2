"""
E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt


fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

# First chart: Original runtime chart
plt.figure(figsize=(10, 6))
plt.title("Comparison of 3 Codes")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

# here, we are plotting the raw values read from the input .csv file, which
# we interpret as being "time" that maps directly to the y-axis.
#
# what if we want to plot MFLOPS instead? How do we compute MFLOPS from
# time and problem size? You may need to add some code here to compute
# MFLOPS, then modify the plt.plot() lines below to plot MFLOPS rather than time.

plt.plot(code1_time, "r-o")
plt.plot(code2_time, "b-x")
plt.plot(code3_time, "g-^")

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("runtime")

varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')
plt.savefig('runtime_chart.png', dpi=300)
plt.show()

# Second chart: MFLOP/s 
# Calculate MFLOP/s for each method
code1_mflops = [(ps/1000000)/t for ps, t in zip(problem_sizes, code1_time)]
code2_mflops = [(ps/1000000)/t for ps, t in zip(problem_sizes, code2_time)]
code3_mflops = [(ps/1000000)/t for ps, t in zip(problem_sizes, code3_time)]

plt.figure(figsize=(10, 6))
plt.title("Computational Performance (MFLOP/s)")

plt.xticks(xlocs, problem_sizes)

plt.plot(code1_mflops, "r-o")
plt.plot(code2_mflops, "b-x")
plt.plot(code3_mflops, "g-^")

plt.xlabel("Problem Sizes")
plt.ylabel("MFLOP/s")

plt.legend(varNames, loc="best")
plt.grid(axis='both')
plt.savefig('mflops_chart.png', dpi=300)
plt.show()

# Third chart: Memory Bandwidth Utilization
# Calculate memory bandwidth utilization (% of peak)
peak_bandwidth = 205  # GB/s for Perlmutter CPU
code1_bandwidth = [0] * len(problem_sizes)  # Direct sum has minimal memory access
code2_bandwidth = [(ps*8)/(t*1e9)*100/peak_bandwidth for ps, t in zip(problem_sizes, code2_time)]
code3_bandwidth = [(ps*8*2)/(t*1e9)*100/peak_bandwidth for ps, t in zip(problem_sizes, code3_time)]

plt.figure(figsize=(10, 6))
plt.title("Memory Bandwidth Utilization")

plt.xticks(xlocs, problem_sizes)

plt.plot(code1_bandwidth, "r-o")
plt.plot(code2_bandwidth, "b-x")
plt.plot(code3_bandwidth, "g-^")

plt.xlabel("Problem Sizes")
plt.ylabel("% of Peak Memory Bandwidth")

plt.legend(varNames, loc="best")
plt.grid(axis='both')
plt.savefig('bandwidth_chart.png', dpi=300)
plt.show()

# Fourth chart: Memory Latency
# Calculate memory latency in nanoseconds
# Direct sum doesn't have access(0) to memory latency
# so they will have minimum memory latency
code2_latency = [(t*1e9)/ps for ps, t in zip(problem_sizes, code2_time)]
code3_latency = [(t*1e9)/(ps*2) for ps, t in zip(problem_sizes, code3_time)]  

plt.figure(figsize=(10, 6))
plt.title("Memory Latency")

plt.xticks(xlocs, problem_sizes)

# Only plot code2 and code3 for latency (code1 has no significant memory access)
plt.plot(code2_latency, "b-x")
plt.plot(code3_latency, "g-^")

plt.xlabel("Problem Sizes")
plt.ylabel("Memory Latency (ns)")

# Only show legend for code2 and code3
latencyVarNames = [var_names[2], var_names[3]]
plt.legend(latencyVarNames, loc="best")
plt.grid(axis='both')
plt.savefig('latency_chart.png', dpi=300)
plt.show()

# EOF