#!/usr/bin/env python
import numpy as np
import os
import time 



def read_matrix():
    """
    Funkcja tworząca macierz.
    Kolejne elementy macierzy podaje 
    użytkownik.
    """
    N = int(input("Podaj rozmiar tablicy (N): "))
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    print("Podaj elementy tablicy (po jednym wierszu):")
    for i in range(N):
        for j in range(N):
            matrix[i][j] = int(input(f"Podaj a[{i}][{j}]: "))

    return matrix
#print(read_matrix())


def read_file(file_name):
    '''
    Funkcja, któa odczytuje elementy
    z pliku. Plik podaje użytkownik.
    '''
    file_handle = open(file_name)
    print(file_handle.read())
    file_handle.close()

#file_dir = os.path.dirname(os.path.realpath('__file__'))
#print(file_dir)

#file_name = input("Podaj plik: ")
#read_file(file_name)


#A = read_matrix()
A = [3, 7, 2, 1]
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
#print(Insertion_Sort(A))


#zad4
m, sigma = 0, 0.1 # mean and standard deviation
B = np.random.normal(m, sigma, 1000000)
#print(B)

#zad5
B = time.time()
print(B)

#zad6
Bi = [np.random.normal(m, sigma) for _ in range(1000000)]
def czy_posort_ros(Bi):
    '''
    Funkcja sprawdza czy lista lub
    tablica jest posortowana rosnąco.
    '''
    n = len(Bi)
    for i in range(n-1):
        if Bi[i] > Bi[i+1]:
            return False
    return True
#print(czy_posort_ros(Bi))

#zad7
