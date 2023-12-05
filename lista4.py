#!/usr/bin/env python
import numpy as np
import time
from roboczy3 import Bubble_Sort, Merge_Sort, Quick_Sort, Heap_Sort, Insertion_Sort

#Zad1

data = [4, 2, 2, 8, 3, 3, 1]

def Counting_Sort(A):
    """
    Algorytm sortujący przez
    zliczanie.
    """
    k = max(A) + 1
    B = [0]*len(A)
    C = [0]*k
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B
print("Counting Sort: ", Counting_Sort(data))

#Zależeć od podstawy to d.
def Radix_Sort(A):
    """
    Algorytm sortujący
    pozycyjnie.
    """
    d = max(A)
    for i in range(d):
        A[i] = Counting_Sort(A)
    return A
print(Radix_Sort(data))

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