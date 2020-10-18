from random import randint
N = 20
arr = [randint(0, 100) for i in range(N)]  # заполняем массив случайными числами
print(arr)
# Метод сортировки пузырьком
for i in range(N-1):  # представляем худший вариант, поэтому такое количество перестановок
    for m in range(N-1-i):
        if arr[m] > arr[m+1]:
            temp = arr[m]
            arr[m] = arr[m+1]
            arr[m+1] = temp
print(arr)            


