import math
import multiprocessing
import random
import sys
import numpy as np

def readfile(fname): # Abrir y leer el archivo
    with open(fname) as f:
        contenido = f.readlines()

    contenido = [x.strip() for x in contenido]
    return contenido

def writefile(fname): # Función para escribir sobre el archivo
    with open("write.txt", "a") as f:
        for x in range(len(fname)):
            f.write(fname[x]+"\n")


def asciid(file):
    arreglo = []
    for x in range(len(file)):
        arreglo.append([(ord(c)) for c in file[x]])
    return arreglo

def charrd(file):
    array = []
    for x in range(len(file)):
        array.append(''.join(chr(i) for i in file[x]))
    return array

def merge(*args): # Comparación y unión de arrays para el merge sort
    left, right = args[0] if len(args) == 1 else args
    left_length, right_length = len(left), len(right)
    left_index, right_index = 0, 0
    merged = []
    while left_index < left_length and right_index < right_length:
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    if left_index == left_length:
        merged.extend(right[right_index:])
    else:
        merged.extend(left[left_index:])
    return merged


def merge_sort(data): # Checkea si el array es de tamaño uno, y separa los arrays para el merge sort
    length = len(data)
    if length <= 1:
        return data
    middle = int(length / 2)
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)


def merge_sort_parallel(data): # Crea la piscina de trabajadores para el procesamiento en paraleloS
    processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=processes)
    size = int(math.ceil(float(len(data)) / processes))
    data = [data[i * size:(i + 1) * size] for i in range(processes)]
    data = pool.map(merge_sort, data)

    while len(data) > 1:
        extra = data.pop() if len(data) % 2 == 1 else None
        data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        data = pool.map(merge, data) + ([extra] if extra else [])
    return data[0]


if __name__ == "__main__":
    s = str(input("Ingrese el nombre del archivo: \n"))
    data_unsorted = s+".txt"
    data_semisorted = readfile(data_unsorted)
    data_ascii = asciid(data_semisorted)
    for sort in merge_sort, merge_sort_parallel:
        data_sorted = sort(data_ascii)
    writefile(charrd(data_sorted))
    print("Las oraciones ordenadas se encuentran en: write.txt")