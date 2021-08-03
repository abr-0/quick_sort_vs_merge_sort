import random, time

def rand_gen(quantity):
    start = time.time()
    l = []
    for i in range(quantity):
        x = random.randint(0, 1000)
        l.append(x)
    return l

start = time.time()
def partition(array, lb, ub):
    pivot = array[lb]
    start = lb + 1
    end = ub

    while True:
        while start <= end and array[start] <= pivot:
            start = start + 1
        while start <= end and array[end] >= pivot:
            end = end - 1
        if start <= end:
            array[start], array[end] = array[end], array[start]
        else:
            break

    array[lb], array[end] = array[end], array[lb]
    return end

def quick_sort(array, lb, ub):
    if lb >= ub:
        return

    p = partition(array, lb, ub)
    quick_sort(array, lb, p-1)
    quick_sort(array, p+1, ub)

array1 = rand_gen(100000)
quick_sort(array1, 0, len(array1)-1)
print(f'Time taken for {len(array1)} numbers: {time.time()-start}')