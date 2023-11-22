#!/usr/bin/env python
import numpy as np
import random
import time

# Liczba przypisań i porównań jest podana za posortowaną tablicą.
# Chwilkę może trwać czas liczenia z powodu dużych danych.


#zad1

A = [np.random.normal(0, 1) for _ in range(5)]
print(A)

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
print("Zadanie 1a: ", Insertion_Sort(A))

B = [np.random.normal(0, 1) for _ in range(5)]
print(B)

def Insertion_Sort_Plus(B):
    """
    Algorytm sortowania. Zwraca liczbę porównań i 
    liczbę przypisań wykonanych w trakcie algorytmu. 
    """  
    przypisanie = 0
    porównanie = 0
    for j in range(len(B)):
        key = B[j]
        i = j-1
        while i>=0 and B[i]>=key:
            B[i], B[i+1] = B[i+1], B[i]
            i = i-1
            porównanie = porównanie + 1
        B[i+1] = key
        przypisanie = przypisanie + 1
    return B,przypisanie,porównanie  
print("Zadanie 1b: ", Insertion_Sort_Plus(B))

#zad2

C = [np.random.normal(0, 1) for _ in range(5)]
print(C)

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
print("Zadanie 2a: ", Bubble_Sort(C))

def Bubble_Sort_Plus(C):
    '''
    Algorytm sortowania. Zwraca liczbę porównań i 
    liczbę przypisań wykonanych w trakcie algorytmu. 
    '''
    N = len(C)
    przypisanie = 0
    porównanie = 0
    for i in range(N-1):
        porównanie = porównanie + 1
        for j in range(N-1, i, -1):
            if C[j]<C[j-1]:
                C[j], C[j-1] = C[j-1], C[j]
                przypisanie = przypisanie + 1
    return C,przypisanie,porównanie
print("Zadanie 2b: ", Bubble_Sort_Plus(C))

#zad3

D = [np.random.normal(0, 1) for _ in range(5)]
#print(D)

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

Merge_Sort(D, 0, len(D) - 1)  
print("Zadanie 3a: ", D)   

przypisania = 0
porównania = 0
def Merge_Plus(D, p, s, k):
    n1 = s - p + 1
    n2 = k - s
    global przypisania, porównania
    L = []
    R = []
    for i in range(n1):
        L.append(D[p + i])
        przypisania = przypisania + 1
    for j in range(n2):
        R.append(D[s + j + 1])
        przypisania = przypisania + 1

    L.append(float("inf"))
    R.append(float("inf"))
    i = 0
    j = 0
    for c in range(p, k + 1):
        porównania = porównania + 1
        if L[i] <= R[j]:
            D[c] = L[i]
            i = i + 1
            przypisania = przypisania + 1
        else:
            D[c] = R[j]
            j = j + 1
            przypisania = przypisania + 1
    return D,przypisania,porównania 

def Merge_Sort_Plus(D, p, k):
    '''
    Algorytm sortowania. Zwraca liczbę porównań i 
    liczbę przypisań wykonanych w trakcie algorytmu. 
    '''
    if p < k:
        q = (p + k) // 2
        Merge_Sort_Plus(D, p, q)
        Merge_Sort_Plus(D, q + 1, k)
        Merge_Plus(D, p, q, k)
    return D,przypisania,porównania

print("Zadanie 3b: ", Merge_Sort_Plus(D, 0, len(D) - 1))
print("Liczba przypisań: ", przypisania)
print("Liczba porównań: ", porównania)

#zad4

D2 = [np.random.normal(0, 1) for _ in range(5)]
przypisanie = 0
porównanie = 0
def Merge21(D2, p, s, k):
    n1 = s - p + 1
    n2 = k - s
    global przypisanie, porównanie
    L = []
    R = []
    for i in range(n1):
        L.append(D2[p + i])
        przypisanie = przypisanie + 1
    for j in range(n2):
        R.append(D2[s + j + 1])
        przypisanie = przypisanie + 1

    L.append(float("inf"))
    R.append(float("inf"))
    i = 0
    j = 0
    for c in range(p, k + 1):
        porównanie = porównanie + 1
        if L[i] <= R[j]:
            D2[c] = L[i]
            i = i + 1
            przypisanie = przypisanie + 1
        else:
            D2[c] = R[j]
            j = j + 1
            przypisanie = przypisanie + 1
    return D2,przypisanie,porównanie 

def Merge_Sort21_Plus(D2, p, k):
    '''
    Algorytm sortowania. Zwraca liczbę porównań i 
    liczbę przypisań wykonanych w trakcie algorytmu. 
    '''
    if p < k:
        q = p + (k - p) // 3
        Merge_Sort21_Plus(D2, p, q)
        Merge_Sort21_Plus(D2, q + 1, k)
        Merge21(D2, p, q, k)
    return D2,przypisanie,porównanie

print("Zadanie 4: ", Merge_Sort21_Plus(D2, 0, len(D2) - 1))
print("Liczba przypisań: ", przypisanie)
print("Liczba porównań: ", porównanie)


#zad5

def testIS():
    '''
    Testy dla Insertion Sort Plus
    dla 1000, 10000, 20000.
    '''
    tablica1000 = np.array([random.randint(1, 1000) for x in range(1000)])
    start= time.time()
    lista,przypisanie,porównanie = Insertion_Sort_Plus(tablica1000)
    koniec = time.time()
    pomiar = koniec - start
    tablica10000 = np.array([random.randint(1, 2000) for x in range(2000)])
    start2 = time.time()
    lista2,przypisanie2,porównanie2 = Insertion_Sort_Plus(tablica10000)
    koniec2 = time.time()
    pomiar2 = koniec2 - start2
    tablica20000 = np.array([random.randint(1, 3000) for x in range(3000)])
    start3 = time.time()
    lista,przypisanie3,porównanie3 = Insertion_Sort_Plus(tablica20000)
    koniec3 = time.time()
    pomiar3 = koniec3 - start3
    return np.array([[pomiar,przypisanie,porównanie],
                    [pomiar2,przypisanie2,porównanie2],
                    [pomiar3,przypisanie3,porównanie3]])


def testBS():
    '''
    Testy dla Bubble Sort Plus
    dla 1000, 10000, 20000.
    '''
    tablica1000 = np.array([random.randint(1, 1000) for x in range(1000)])
    start= time.time()
    lista,przypisanie,porównanie = Bubble_Sort_Plus(tablica1000)
    koniec = time.time()
    pomiar = koniec - start
    tablica10000 = np.array([random.randint(1, 2000) for x in range(2000)])
    start2 = time.time()
    lista2,przypisanie2,porównanie2 = Bubble_Sort_Plus(tablica10000)
    koniec2 = time.time()
    pomiar2 = koniec2 - start2
    tablica20000 = np.array([random.randint(1, 3000) for x in range(3000)])
    start3 = time.time()
    lista,przypisanie3,porównanie3 = Bubble_Sort_Plus(tablica20000)
    koniec3 = time.time()
    pomiar3 = koniec3 - start3
    return np.array([[pomiar,przypisanie,porównanie],
                    [pomiar2,przypisanie2,porównanie2],
                    [pomiar3,przypisanie3,porównanie3]])

def testMS():
    '''
    Testy dla Merge Sort Plus
    dla 1000, 10000, 20000.
    '''
    tablica1000 = np.array([random.randint(1, 1000) for x in range(1000)])
    start= time.time()
    lista,przypisanie,porównanie = Merge_Sort_Plus(tablica1000, 0, len(tablica1000) - 1)
    koniec = time.time()
    pomiar = koniec - start
    tablica10000 = np.array([random.randint(1, 2000) for x in range(2000)])
    start2 = time.time()
    lista2,przypisanie2,porównanie2 = Merge_Sort_Plus(tablica10000, 0, len(tablica10000) - 1)
    koniec2 = time.time()
    pomiar2 = koniec2 - start2
    tablica20000 = np.array([random.randint(1, 3000) for x in range(3000)])
    start3 = time.time()
    lista,przypisanie3,porównanie3 = Merge_Sort_Plus(tablica20000, 0, len(tablica20000) - 1)
    koniec3 = time.time()
    pomiar3 = koniec3 - start3
    return np.array([[pomiar,przypisanie,porównanie],
                    [pomiar2,przypisanie2,porównanie2],
                    [pomiar3,przypisanie3,porównanie3]])

def testMS21():
    '''
    Testy dla Merge Sort21 Plus
    dla 1000, 10000, 20000.
    '''
    tablica1000 = np.array([random.randint(1, 1000) for x in range(1000)])
    start= time.time()
    lista,przypisanie,porównanie = Merge_Sort21_Plus(tablica1000, 0, len(tablica1000) - 1)
    koniec = time.time()
    pomiar = koniec - start
    tablica10000 = np.array([random.randint(1, 2000) for x in range(2000)])
    start2 = time.time()
    lista2,przypisanie2,porównanie2 = Merge_Sort21_Plus(tablica10000, 0, len(tablica10000) - 1)
    koniec2 = time.time()
    pomiar2 = koniec2 - start2
    tablica20000 = np.array([random.randint(1, 3000) for x in range(3000)])
    start3 = time.time()
    lista,przypisanie3,porównanie3 = Merge_Sort21_Plus(tablica20000, 0, len(tablica20000) - 1)
    koniec3 = time.time()
    pomiar3 = koniec3 - start3
    return np.array([[pomiar,przypisanie,porównanie],
                    [pomiar2,przypisanie2,porównanie2],
                    [pomiar3,przypisanie3,porównanie3]])

def funkcja():
    '''
    Funkcja testująca i zwracająca
    macierz 3 stopnia. 
    '''
    wynik = np.array([testIS(), testBS(), testMS()])
    return wynik

print("Zadanie 5: ", funkcja())
