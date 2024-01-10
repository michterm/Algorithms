#!/usr/bin/env python
import numpy as np
import random
import time

#Zad1
def Generated_Time(n):
    s = np.zeros(n)
    f = np.zeros(n)
    for i in range(n):
        s[i] = round(random.uniform(0, 24), 3)
    for i in range(n):
        f[i] = round(random.uniform(s[i], 24), 3)
    sorted_time = sorted(zip(s, f), key=lambda x:x[1])
    s, f = zip(*sorted_time)
    return s, f

s0, f0 = Generated_Time(4)
print("Zadanie 1:")
print("Czasy rozpoczęcia zajęć:", s0)
print("Czasy zakończenia zajęć", f0)

#Zad2


#Zad3
def Recursive_Activity_Selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m = m + 1
    if m <= n:
        return [m] + Recursive_Activity_Selector(s, f, m, n)
    else:
        return []
    
def Activity_Selector(s, f):
    n = len(s)
    zajecia = []
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            zajecia.append(m)
            k = m
    return zajecia

def Czas_działania0():
    s, f = Generated_Time(100)
    start_time = time.time()
    result = ...
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time
    

def Czas_działania1():
    s, f = Generated_Time(200000)
    start_time = time.time()
    result = Recursive_Activity_Selector(s, f, 0, len(s)-1)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time
    

def Czas_działania2():
    s, f = Generated_Time(200000)
    start_time = time.time()
    result = Activity_Selector(s, f)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

print("Zadanie 3:")
#print("Czas działania ...")
print("Czas działania Recursive_Activity_Selector:", Czas_działania1())
print("Czas działania Activity_Selector", Czas_działania2())
print("Niestety nie udało mi się zrobic całej listy.")