# Insertion Sort
# Best: O(n) | Average: O(n^2) | Worst: O(n^2)
# Loop through elements. Each loop between i-1th and 0th element, if this is > than main loop, j+1 = j, j = main loop

def insertionSort(array):
    for i in range(1, len(array)):
        to_sort = array[i]
        for j in range(i - 1, -1, -1):
            if array[j] > to_sort:
                array[j + 1], array[j] = array[j], to_sort
            else:
                break


# SelectionSort
# Best: O(n^2) | Avg: O(n^2) | Worst: O(n^2)
# Loop da len-1 a 0 (i). Trovo l'indice del maggiore, scambio a[i] e a[max_index]

def selectionSort(array):
    for fillslot in range(len(array) - 1, 0, -1):
        max_index = 0
        for i in range(1, fillslot + 1):
            if array[i] > array[max_index]:
                max_index = i

        array[fillslot], array[max_index] = array[max_index], array[fillslot]


# BubbleSort
# Best: O(n) | Avg: O(n^2) | Worst: O(n^2)
# Loop da len-1 a 0 (i), loop da 0 a i (j), se j > j+1 scambio j e j+1

def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


# QuickSort
# Best: O(n log(n)) | Avg: O(n log(n)) | Worst: O(n^2)
# Less, equal, greater []. If len(arr) > 1, prendo a[0] come pivot e divido elementi in less, equal or greater
# Return qs(l) + equal + qs(r); else return array

def quickSort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quickSort(less) + equal + quickSort(greater)
    else:
        return array


# MergeSort
# Best: O(n log(n)) | Avg: O(n log(n)) | Worst: O(n log(n))
# Inizializzo result []. Se len(arr) < 2 return. Altrimenti mid = len/2, l = ms(a[mid:]), r = ms(a[:mid]) ricorsivamente.
# Uso i, j come indici e finche' i < len(l) e j < len(r) confronto elementi, appendo quello minore a result e aumento di 1 l'indice
# di quello da cui abbiamo aggiunto. A fine loop aggiungo a result l[i:] e r[j:].

def mergeSort(array):
    result = []
    if len(array) < 2:
        return array
    mid = int(len(array) / 2)
    y = mergeSort(array[:mid])
    z = mergeSort(array[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result


# Counter Sort (k = max value)
# Best: O(n+k) | Avg: O(n+k) | Worst: O(n+k)
# Inizializzo un array di k+1 elementi dove k e' il maggiore nell'array. Loop tra elementi, aumento di 1 a[elemento]. Per j nell'array
# del counter, appendo a result [j] * counter[j]

def counterSort(array, k):
    length = len(array)
    counter = [0] * (k + 1)
    for i in array:
        counter[i] += 1
    result = [] * length
    for j in range(0, k + 1):
        if counter[j] > 0:
            result += [j] * counter[j]
    return result