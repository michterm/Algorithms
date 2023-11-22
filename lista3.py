#!/usr/bin/env python
import matplotlib as plt
import numpy as np

A = [round(np.random.normal(0, 1), 2) for _ in range(10)]
print("Losowa 10 elementowa z zaookrągleniem do 2 miejsc po przecinku tablica z rozkładu normalnego A := ", A)

#Zad1

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

przypisania = 0
porównania = 0
def Heapify_Plus(A, i, heap_size):
    '''
    Funkcja budująca kopiec.
    '''
    l = left(i)
    r = right(i)
    global przypisania, porównania
    porównania = porównania + 1
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    porównania = porównania + 1
    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        przypisania = przypisania + 2
        Heapify_Plus(A, largest, heap_size)

def Heap_Sort_Plus(A):
    '''
    Funkcja sortująca 
    przez kopcowanie.
    '''
    global przypisania, porównania
    A = A.copy()
    Heap_Build(A)
    A_heapsize = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        przypisania = przypisania + 1
        A_heapsize = A_heapsize - 1
        Heapify_Plus(A, 0, A_heapsize)
    return A, przypisania, porównania

print("Zad1 Heap Sort: ", Heap_Sort(A))
#print("Zad1 Heap Sort: ", Heap_Sort(B))
#print("Zad1 Heap Sort: ", Heap_Sort(xd))

print("Zad1 Heap Sort Plus: ", Heap_Sort_Plus(A))
#print("Zad1 Heap Sort Plus: ", Heap_Sort_Plus(B))
#print("Zad1 Heap Sort Plus: ", Heap_Sort_Plus(xd))
print("Zad1 Liczba przypisań i porównań: ", przypisania, porównania)

#Zad2

def left3(i):
    '''
    Funkcja zwraca indeks lewego dziecka 
    elementu o indeksie "i" w tablicy.
    '''
    return 3*i + 1

def middle(i):
    '''
    Funkcja zwraca indeks środkowego 
    dziecka elementu o indeksie "i" w 
    tablicy.
    '''
    return 3*i + 2


def right3(i):
    '''
    Funkcja zwraca indeks prawego dziecka 
    elementu o indeksie "i" w tablicy.
    '''
    return 3*i + 3

def Heapify3(A, i, heap_size):
    '''
    Funkcja budująca kopiec.
    '''
    l = left3(i)
    r = right3(i)
    m = middle(i)
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if m < heap_size and A[m] > A[largest]:
        largest = m

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        Heapify3(A, largest, heap_size)

def Heap_Build3(A):
    n = len(A)
    for i in range(n//3 - 1, -1, -1):
        Heapify3(A, i, n)

def Heap_Sort3(A):
    '''
    Funkcja sortująca 
    przez kopcowanie.
    '''
    A = A.copy()
    Heap_Build3(A)
    A_heapsize = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        A_heapsize = A_heapsize - 1
        Heapify3(A, 0, A_heapsize)
    return A

przypisania3 = 0
porównania3 = 0
def Heapify_Plus3(A, i, heap_size):
    '''
    Funkcja budująca kopiec.
    '''
    l = left3(i)
    r = right3(i)
    m = middle(i)
    global przypisania3, porównania3
    porównania3 = porównania3 + 1
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if m < heap_size and A[m] > A[largest]:
        largest = m

    porównania3 = porównania3 + 1
    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        przypisania3 = przypisania3 + 2
        Heapify_Plus3(A, largest, heap_size)

def Heap_Sort_Plus3(A):
    '''
    Funkcja sortująca 
    przez kopcowanie.
    '''
    global przypisania3, porównania3
    A = A.copy()
    Heap_Build3(A)
    A_heapsize = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        przypisania3 = przypisania3 + 1
        A_heapsize = A_heapsize - 1
        Heapify_Plus3(A, 0, A_heapsize)
    return A, przypisania3, porównania3

print("Zad2 Heap Sort3: ", Heap_Sort3(A))
#print("Zad2 Heap Sort3: ", Heap_Sort3(B))
#print("Zad2 Heap Sort3: ", Heap_Sort3(xd))

print("Zad2 Heap Sort3 Plus: ", Heap_Sort_Plus3(A))
#print("Zad2 Heap Sort3 Plus: ", Heap_Sort_Plus3(B))
#print("Zad2 Heap Sort3 Plus: ", Heap_Sort_Plus3(xd))
print("Zad2 Liczba przypisań i porównań: ", przypisania3, porównania3)


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

przypisanie = 0
porównanie = 0
def Partition_Plus(A, p, k):
    '''
    Funkcja dzieląca tablicę
    na dwie części.
    '''
    global przypisanie, porównanie
    x = A[k]
    przypisanie = przypisanie + 1
    i = p-1
    for j in range(p, k):
        porównanie = porównanie + 1
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
            przypisanie = przypisanie + 2
    A[i + 1], A[k] = A[k], A[i + 1]
    przypisanie = przypisanie + 2
    return i+1

def Quick_Sort_Plus(A, p, k):
    '''
    Funkcja sortująca.
    '''
    if p<k:
        s = Partition_Plus(A, p, k)
        Quick_Sort_Plus(A, p, s-1)
        Quick_Sort_Plus(A, s+1, k)
    return A, przypisanie, porównanie

print("Zad3 Quick Sort: ", Quick_Sort(A, 0, len(A)-1))
#print("Zad3 Quick Sort: ", Quick_Sort(B, 0, len(B)-1))
#print("Zad3 Quick Sort: ", Quick_Sort(xd, 0, len(xd)-1))

print("Zad3 Quick Sort Plus: ", Quick_Sort_Plus(A, 0, len(A)-1))
#print("Zad3 Quick Sort Plus: ", Quick_Sort_Plus(B, 0, len(B)-1))
#print("Zad3 Quick Sort Plus: ", Quick_Sort_Plus(xd, 0, len(xd)-1))
print("Zad3 Liczba przypisań i porównań: ", przypisanie, porównanie)

#Zad4

def partition(arr, low, high, pivot1, pivot2):
    i = low
    j = low
    k = high

    while j <= k:
        if arr[j] < pivot1:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif pivot1 <= arr[j] <= pivot2:
            j += 1
        else:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1

    return i, k


def quicksort3(arr, low, high):
    while low < high:
        pivot1 = arr[low]
        pivot2 = arr[high]

        i, k = partition(arr, low, high, pivot1, pivot2)
        if i - low < high - k:
            quicksort3(arr, low, i - 1)
            low = k + 1
        else:
            quicksort3(arr, k + 1, high)
            high = i - 1


def quicksort3_plus(arr):
    quicksort3(arr, 0, len(arr) - 1)


def partition(arr, low, high, pivot1, pivot2, comparisons, assignments):
    i = low
    j = low
    k = high

    while j <= k:
        comparisons += 1
        if arr[j] < pivot1:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
            assignments += 3
        elif pivot1 <= arr[j] <= pivot2:
            j += 1
            comparisons += 2
        else:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
            assignments += 3

    return i, k, comparisons, assignments


def quicksort3(arr, low, high, comparisons, assignments):
    while low < high:
        pivot1 = arr[low]
        pivot2 = arr[high]

        i, k, comparisons, assignments = partition(arr, low, high, pivot1, pivot2, comparisons, assignments)
        if i - low < high - k:
            quicksort3(arr, low, i - 1, comparisons, assignments)
            low = k + 1
        else:
            quicksort3(arr, k + 1, high, comparisons, assignments)
            high = i - 1

    return comparisons, assignments


def quicksort3_plus(arr):
    comparisons, assignments = 0, 0
    comparisons, assignments = quicksort3(arr, 0, len(arr) - 1, comparisons, assignments)
    return comparisons, assignments

quicksort3_plus(A)
print("Zad4 Quick Sort3: ", A)


comparisons, assignments = quicksort3_plus(A)
print("Zad4 Quick Sort3 Plus: ", A)
print("Liczba porównań:", comparisons)
print("Liczba przypisań:", assignments)
