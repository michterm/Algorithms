#!/usr/bin/env python


#Zad1

#A = [2, 1, 4, 3]
A = [16, 4, 10, 14, 7, 8, 3, 2, 8, 1]
xd = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 6]

def left(i):
    '''
    Funckja zwraca indeks lewego dziecka 
    elementu o indeksie i w tablicy.
    '''
    return 2*i+1

def right(i):
    '''
    Funckja zwraca indeks prawego dziecka 
    elementu o indeksie i w tablicy.
    '''
    return 2*i+2

def Heapify(A, i):
    '''
    Funkcja budująca kopiec.
    '''
    l = left(i)
    r = right(i)
    A_heapsize = len(A)
    if l < A_heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < A_heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[largest],A[i] = A[i],A[largest]
        Heapify(A, largest)

def Heap_Build(A):
    n = len(A)
    for i in range(n//2, -1, -1):
        Heapify(A, i)

def Heap_Sort(A):
    '''
    Funkcja sortująca 
    przez kopcowanie.
    '''
    Heap_Build(A)
    A_heapsize = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0],A[i] = A[i],A[0]
        A_heapsize = A_heapsize - 1
        Heapify(A, 0)
    return A
print("Heap Sort: ", Heap_Sort(xd))

def Heapsortt_Plus(A):
    ...

#Zad3

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
print("Zad3 Quick sort: ", Quick_Sort(A, 0, len(A)-1))