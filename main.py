import random, time
import matplotlib.pyplot as plt

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

def merge_sort(data):
    if len(data) > 1:
        mid = len(data)//2
        # slicing
        lh = data[:mid]
        rh = data[mid:]

        merge_sort(lh)
        merge_sort(rh)
        i=j=k=0
        while i < len(lh) and j < len(rh):
            if lh[i] < rh[j]:
                data[k]=lh[i]
                i=i+1
            else:
                data[k]=rh[j]
                j=j+1
            k=k+1

        while i < len(lh):
            data[k]=lh[i]
            i=i+1
            k=k+1

        while j < len(rh):
            data[k]=rh[j]
            j=j+1
            k=k+1

def main():
    x1 = [] # no. of elements to sort
    y1 = [] # time for quick sort
    y2 = [] # time for merge sort
    for i in range(1, 10000, 100):
        data1 = data2 = rand_gen(i)
        x1.append(i)
        # quick sort
        start_t1 = time.time()
        quick_sort(data1, 0, len(data1)-1)
        end_t1 = time.time()
        y1.append(end_t1-start_t1)
        
        # merge sort
        start_t2 = time.time()
        merge_sort(data2)
        end_t2 = time.time()
        y2.append(end_t2-start_t2)

    # plotting graph
    plt.plot(x1,y1, label = "quick sort")
    plt.plot(x1,y2, label = "merge sort")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()