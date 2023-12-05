#!/usr/bin/env python

def Insertion_Sort(A):
    """
    Algorytm sortowania.
    """  
    for j in range(len(A)):
        key = A[j]
        i = j-1
        while i>=0 and A[i]>=key:
            A[i], A[i+1] = A[i+1], A[i]
            i = i-1
        A[i+1] = key
    return A 

def Bubble_Sort(C):
    '''
    Algorytm sortowania.
    '''
    N = len(C)
    for i in range(N-1):
        for j in range(N-1, i, -1):
            if C[j]<C[j-1]:
                C[j], C[j-1] = C[j-1], C[j]
    return C

def Merge(D, p, s, k):
    '''
    Funkcja z wykładu.
    '''
    n1 = s - p + 1
    n2 = k - s
    L = []
    R = []
    for i in range(n1):
        L.append(D[p + i])
    for j in range(n2):
        R.append(D[s + j + 1])  

    L.append(float("inf"))
    R.append(float("inf"))
    i = 0
    j = 0
    for c in range(p, k + 1):  
        if L[i] <= R[j]:
            D[c] = L[i]
            i = i + 1
        else:
            D[c] = R[j]
            j = j + 1
    return D

def Merge_Sort(D, p, k):
    '''
    Rekurencyjny algorytm sortowania.
    '''
    if p < k:
        q = (p + k) // 2
        Merge_Sort(D, p, q)
        Merge_Sort(D, q + 1, k)
        Merge(D, p, q, k)
    return D

def left(i):
    '''
    Funkcja zwraca indeks lewego dziecka 
    elementu o indeksie "i" w tablicy.
    '''
    return 2*i + 1

def right(i):
    '''
    Funkcja zwraca indeks prawego dziecka 
    elementu o indeksie "i" w tablicy.
    '''
    return 2*i + 2

def Heapify(A, i, heap_size):
    '''
    Funkcja budująca kopiec.
    '''
    l = left(i)
    r = right(i)

    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        Heapify(A, largest, heap_size)

def Heap_Build(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        Heapify(A, i, n)

def Heap_Sort(A):
    '''
    Funkcja sortująca 
    przez kopcowanie.
    '''
    A = A.copy()
    Heap_Build(A)
    A_heapsize = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        A_heapsize = A_heapsize - 1
        Heapify(A, 0, A_heapsize)
    return A

def Partition(A, p, k):
    '''
    Funkcja dzieląca tablicę
    na dwie części.
    '''
    x = A[k]
    i = p-1
    for j in range(p, k):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[k] = A[k], A[i + 1]
    return i+1

def Quick_Sort(A, p, k):
    '''
    Funkcja sortująca.
    '''
    if p<k:
        s = Partition(A, p, k)
        Quick_Sort(A, p, s-1)
        Quick_Sort(A, s+1, k)
    return A

