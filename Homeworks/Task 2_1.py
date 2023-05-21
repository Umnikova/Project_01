from random import randint
def create_list():
    n = 10
    arr = []
    for i in range(n):
        arr.append(randint(-100, 100))
    return arr
data = create_list()
print(data)

def minimum(data):
    for i in range(len(data)):
        j = i - 1
        k = data[i]
        while data[j] > k and j >= 0:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = k
    return data
print(minimum(data))
print("Минимальное значение равно:", minimum(data)[0])

def maximum(data):
    for i in range(len(data)):
        j = i - 1
        k = data[i]
        while data[j] > k and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = k
    return data
print(maximum(data))
print("Максимальное значение равно:", maximum(data)[-1])
