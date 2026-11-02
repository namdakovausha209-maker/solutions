def insertion_sort(arr):
    sorted_arr = arr.copy()

    for i in range(1, len(sorted_arr)):
        current_value = sorted_arr[i]
        position = i

        while position > 0 and sorted_arr[position - 1] > current_value:
            sorted_arr[position] = sorted_arr[position - 1]
            position -= 1

        sorted_arr[position] = current_value

    return sorted_arr

if __name__ == "__main__":
    print(insertion_sort([1,2,4,5,7,8,9]))
    print(insertion_sort([7, 3, 3, 4, 1]))
    print(insertion_sort([]))