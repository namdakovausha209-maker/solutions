import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) < 2:
        return sorted(arr)
    supporting_element = random.randint(0, len(arr) - 1)
    support = arr[supporting_element]

    less = []
    equal = []
    greater = []
    
    for element in arr:
        if element < support:
            less.append(element)
        elif element > support:
            greater.append(element)
        else:
            equal.append(element)
    return quick_sort(less) + equal + quick_sort(greater)

if __name__ == "__main__":
    print(quick_sort([4, 2, 7, 1, 3, 5]))
    print(quick_sort([7, 3, 3, 4, 1]))
    print(quick_sort([]))
