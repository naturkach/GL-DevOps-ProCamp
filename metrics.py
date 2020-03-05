#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import psutil

if len(sys.argv)<=1:
    print("use arg: cpu|mem")
    exit(1)
arg = str(sys.argv[1])


if (arg=='cpu'):
    cpu_param = psutil.cpu_times(percpu=False)
    print ('system.cpu.idle',  cpu_param.idle)
    print ('system.cpu.user',  cpu_param.user)
    print ('system.cpu.guest', cpu_param.guest)
    print ('system.cpu.iowait',cpu_param.iowait)
    print ('system.cpu.stolen',cpu_param.steal)
    print ('system.cpu.system',cpu_param.system)
elif (arg=='mem'):
    mem_param = psutil.virtual_memory()
    print('virtual total', mem_param.total)
    print('virtual used',  mem_param.used)
    print('virtual free',  mem_param.free)
    print('virtual shared',mem_param.shared)
    mem_swap = psutil.swap_memory()
    print('swap total', mem_swap.total)
    print('swap used',  mem_swap.used)
    print('swap free',  mem_swap.free)
    print(mem_swap)
else:
    print("use arg: cpu|mem")
    exit(1)
