import random, time
# import matplotlib.pyplot as plt

# random function which returns list of random numbers
def rand_gen(quantity):
    l = []
    for i in range(quantity):
        x = random.randint(0, quantity)
        l.append(x)
    return l

def partition(data, lb, ub):
    p = data[lb]
    i = lb + 1
    j = ub
    while i <= j:
        while i <= j and data[i] <= p:
            i += 1
        while i <= j and data[j] >= p:
            j -= 1
        if i <= j:
            data[i], data[j] =  data[j], data[i]

    data[lb], data[j] = data[j], data[lb]
    return j

def quick_sort(data, lb, ub):
    if lb < ub:
        p = partition(data, lb, ub)
        quick_sort(data, lb, p-1)
        quick_sort(data, p+1, ub)

def main():
    data = rand_gen(5)
    quick_sort(data, 0, len(data)-1)
    print(data)

if __name__ == "__main__":
    main()


# x1 = []
# y1 = []
# for i in range(0, 10000, 100):
#     array1 = rand_gen(i)
#     start_t1 = time.time()
#     quick_sort(array1, 0, len(array1)-1)
#     end_t1 = time.time()
#     x1.append(i)
#     y1.append(end_t1-start_t1)
    

# plt.plot(x1,y1)
# print(y1)
# print(sum(y1))
# plt.show()