#!/usr/bin/env python
import numpy as np
import time

#zad1

print("Zadanie 1:")
def Naive_Cut_Rod(p, n):
    if n == 0:
        return 0
    q = -np.inf
    for i in range(1, n+1):
        q = max(q, p[i-1] + Naive_Cut_Rod(p, n-i))
    return q


def generate_input_data(size):
    return np.random.randint(1, 10000, size=size)

print("Testy dla funkcji Naive_Cut_Rod:")
def test():
    for size in range(1, 24, 1):
        input_data = generate_input_data(size)
        
        start_time = time.time()
        result = Naive_Cut_Rod(input_data, size)
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"Rozmiar danych wejściowych: {size}, Wynik: {result}, Czas wykonania: {execution_time} sekund")
test()
print("Dla tablic rozmiarów większych niż 24 algorytm działa nieoptymalnie.")

#zad2

print("Zadanie2:")
def Cut_Rod_Aux(p, r, n):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -np.inf
    for i in range(1, n+1):
        q = max(q, p[i], Cut_Rod_Aux(p, r, n-i))
    r[n] = q
    return q

def New_Cut_Rod(p, n):
    r = np.zeros(n + 1)
    for i in range(n+1):
        r[i] = -np.inf
    return Cut_Rod_Aux(p, r, n)


print("Testy dla funkcji New_Cut_Rod:")
def test2():
    for size in range(100, 901, 100):
        input_data = generate_input_data(size)
        
        start_time = time.time()
        result = New_Cut_Rod(input_data, size-1)
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"Rozmiar danych wejściowych: {size}, Wynik: {int(result)}, Czas wykonania: {execution_time} sekund")
test2()
print("Zatem widać, że z zapamiętywaniem wyników algorytm działa dużo szybciej.")

#zad3
print("Zadanie 3:")
def Cut_Rod(p, n):
    r = np.zeros(n + 1)  
    for j in range(1, n + 1):
        q = -np.inf
        for i in range(1, j + 1):
            q = max(q, p[i - 1] + r[j - i])
        r[j] = q
    return r[n]

def Ext_Cut_Rod(p, n):
    r = np.zeros(n + 1)
    s = np.zeros(n + 1)
    for j in range(1, n + 1):  
        q = -np.inf
        for i in range(1, j + 1):  
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j] = i
        r[j] = q  
    return r, s

def Print_Solution(p, n):
    r, s = Ext_Cut_Rod(p, n)
    result = []
    while n > 0:
        result.append(int(s[int(n)]))  
        n = n - int(s[int(n)])
    return result


print("Testy dla funkcji Cut_Rod:")
def test3():
    for size in range(100, 901, 100):
        input_data = generate_input_data(size)
        
        start_time = time.time()
        result = Cut_Rod(input_data, size)
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"Rozmiar danych wejściowych: {size}, Wynik: {int(result)}, Czas wykonania: {execution_time} sekund")
test3()

#zad4
print("Zadanie 4:")
def Naive_Recurency_Algorythm(X, Y, m, n):
    """
    Algorytm szukający największego wspólnego podciągu,
    gdzie X jest tablicą długości m, a Y jest tablicą długości n.
    """
    if m == 0 or n == 0:
        return 0
    if m > 0 and n > 0 and X[m-1] == Y[n-1]:
        return Naive_Recurency_Algorythm(X, Y, m-1, n-1) + 1  
    return max(Naive_Recurency_Algorythm(X, Y, m-1, n), Naive_Recurency_Algorythm(X, Y, m, n-1))

# m = 10
# n = 10
# X = np.random.randint(1, 10, size=(m,))
# Y = np.random.randint(1, 10, size=(n,))
X = "SANIE"
Y = "BASI"
m = len(X)
n = len(Y)  

print("X:", X)
print("Y:", Y)
print("Wynik:", Naive_Recurency_Algorythm(X, Y, len(X), len(Y)))

#zad5
print("Zadanie 5:")
def Memorized_LCS(X, Y, m, n, memory):
    """
    Algorytm szukający największego wspólnego podciągu,
    gdzie X jest tablicą długości m, a Y jest tablicą długości n
    oraz zapamiętuje wyniki w celu przyśpieszenia algorytmu. Dane
    są zapamiętywane w pustym słowniku memory = {}.
    """
    memory = {}
    if m == 0 or n == 0:
        return 0
    if (m, n) in memory:
        return memory[(m, n)]
    if m > 0 and n > 0 and X[m-1] == Y[n-1]:
        return Memorized_LCS(X, Y, m-1, n-1, memory) + 1  
    return max(Memorized_LCS(X, Y, m-1, n, memory), Memorized_LCS(X, Y, m, n-1, memory))

memory = {} 
print("X:", X)
print("Y:", Y)
print("Wynik:", Memorized_LCS(X, Y, len(X), len(Y), memory))

#zad6

print("Zadanie 6:")
def Length_LCS(X, Y):
    """
    Iteracyjny algorytm szukający
    najdłuższego wspólnego podciągu
    dla tablicy X długości m oraz dla
    tablicy Y długości n.
    """
    m = len(X)
    n = len(Y)
    #b = b[len(X), len(Y)]
    c = np.zeros((m+1, n+1), dtype=int)
    for i in range(len(X)):
        c[i, 0] = 0
    for j in range(len(Y)):
        c[0, j] = 0
    for i in range(1, len(X)):
        for j in range(1, len(Y)):
            if X[i] == Y[j]:
                c[i, j] = c[i-1, j-1] + 1
                #b[i, j] = '↖'
            elif c[i-1, j] <= c[i, j-1]:
                c[i, j] = c[i, j-1]
                #b[i, j] = '←'
            else:
                c[i, j] = c[i-1, j]
                #b[i, j] = '↑'
    return c[i, j]

X = "SANIE"
Y = "BASI"
print("X:", X)
print("Y:", Y)
print("Wynik:", Length_LCS(X, Y))