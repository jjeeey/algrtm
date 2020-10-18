from random import randint
N = 20
arr = [randint(0, 100) for i in range(N)]
print(arr)
for i in range(1, N):
    temp = arr[i]  # запоминаем ссылку на индекс для последующей подстановки
    j = i - 1
    while ((j>= 0) and (temp < arr[j])):
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = temp
print(arr)
