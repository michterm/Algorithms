#!/usr/bin/env python
import numpy as np
import time
from roboczy3 import Bubble_Sort, Merge_Sort, Quick_Sort, Heap_Sort, Insertion_Sort

#Zad1

print("Zadanie 1:")
data = np.random.randint(9, size=10)

def Counting_Sort(A, k):
    """
    Algorytm sortujący przez
    zliczanie.
    """
    k = max(A) + 1
    C = np.zeros(k,dtype=int)
    B = np.zeros(len(A), dtype=int)
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B

def Radix_Sort(A, k):
    """
    Algorytm sortujący pozycyjnie. 
    A jest tablicą, a k jest podstawą.
    """
    d_max = max(A)
    d = 1
    for _ in range(d):
        if d_max//d>0:
            A = Counting_Sort(A, k)
            d = d + k
    return A

data2 =[20, 12, 40, 32, 50]
print("Nieposortowana tablica:", data)
print("Posortowana tablica Radix_Sort: ", Radix_Sort(data, 10))

def Test_Radix_Sort():
    tablica = np.random.rand(100000)
    start = time.time()
    sorted_array = Radix_Sort(tablica, 1)
    end = time.time()
    measure = end - start
    return measure
print("Czas działania Radix_Sort dla podstawy 1: ", Test_Radix_Sort(),"s")

def Test_Radix_Sort2():
    tablica = np.random.rand(100000)
    start = time.time()
    sorted_array = Radix_Sort(tablica, 10)
    end = time.time()
    measure = end - start
    return measure
print("Czas działania Radix_Sort dla podstawy 10: ", Test_Radix_Sort2(),"s")

def Test_Radix_Sort3():
    tablica = np.random.rand(100000)
    start = time.time()
    sorted_array = Radix_Sort(tablica, 20)
    end = time.time()
    measure = end - start
    return measure
print("Czas działania Radix_Sort dla podstawy 20: ", Test_Radix_Sort2(),"s")

#Zad2

print("Zadanie 2:")
def Bucket_Sort(A):
    """
    Algorytm sortowania kubełkowego dla liczb z przedziału [0, 1).
    """
    n = len(A)
    B = [np.array([]) for _ in range(n)]
    for i in range(len(A)):
        index = int(n*A[i])
        B[index] = np.append(B[index], A[i])
    for i in range(n):
        B[i] = Insertion_Sort(B[i])
    złączenie_kubełków = np.concatenate(B)
    return złączenie_kubełków

losowa_tablica = np.random.rand(8)
print("Nieposortowana tablica: ", losowa_tablica)
print("Posortowana tablica Bucket_Sort: ", Bucket_Sort(losowa_tablica))

print("Czas działania algorytmów na losowej liście 5000 elementowej w sekundach:")
def Test_Bucket_Sort():
    tablica = np.random.rand(5000)
    start = time.time()
    sorted_array = Bucket_Sort(tablica)
    end = time.time()
    measure = end - start
    return measure
print("Czas działania Bucket_Sort: ", Test_Bucket_Sort(),"s")

def Test_Insertion_Sort():
    tablica = np.random.rand(5000)
    start = time.time()
    sorted_array = Insertion_Sort(tablica)
    end = time.time()
    measure = end - start
    return measure
print("Czas działania Insertion_Sort: ", Test_Insertion_Sort(),"s")

def Test_Buble_Sort():
    tablica = np.random.rand(5000)
    start = time.time()
    sorted_array = Bubble_Sort(tablica)
    end = time.time()
    measure = end - start
    return measure
print("Czas działania Buble_Sort: ", Test_Buble_Sort(),"s")

def Test_Merge_Sort():
    tablica = np.random.rand(5000)
    start = time.time()
    sorted_array = Merge_Sort(tablica, 0, len(tablica)-1)
    end = time.time()
    measure = end - start
    return measure
print("Czas działania Merge_Sort: ", Test_Merge_Sort(),"s")

def Test_Heap_Sort():
    tablica = np.random.rand(5000)
    start = time.time()
    sorted_array = Heap_Sort(tablica)
    end = time.time()
    measure = end - start
    return measure
print("Czas działania Heap_Sort: ", Test_Heap_Sort(),"s")

def Test_Quick_Sort():
    tablica = np.random.rand(5000)
    start = time.time()
    sorted_array = Quick_Sort(tablica, 0, len(tablica)-1)
    end = time.time()
    measure = end - start
    return measure
print("Czas działania Quick_Sort: ", Test_Quick_Sort(),"s")