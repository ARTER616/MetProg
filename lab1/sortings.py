def shaker_sort_algorithm(data):
    """! Perform the shaker (cocktail) sorting algorithm on the given list of data.

    @data (List): A list of elements to be sorted.
    """
    left = 0
    right = len(data) - 1
    while left < right:
        # loop through the data from left to right
        for i in range(left, right):
            # compare two adjacent elements and swap them if necessary
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
        # decrease the right bound of the list
        right -= 1
        # loop through the data from right to left
        for i in range(right, left, -1):
            # compare two adjacent elements and swap them if necessary
            if data[i-1] > data[i]:
                data[i-1], data[i] = data[i], data[i-1]
        # increase the left bound of the list
        left += 1
    return data

def quicksort(data, low, high):
    """! Quicksort - performs quick sorting algorithm

    @data: list of items to be sorted
    @low: index of the first item in the list
    @high: index of the last item in the list

    Returns sorted list of items
    """
    if low < high:
        pivot_index = partition(data, low, high)
        quicksort(data, low, pivot_index - 1)
        quicksort(data, pivot_index + 1, high)
    return data

def partition(data, low, high):
    """! Partition - helper function for quicksort

    @data: list of items to be sorted
    @low: index of the first item in the list
    @high: index of the last item in the list

    Returns pivot index
    """
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1

def merge_sort(data):
    """
    This function performs merge sort algorithm

    @param data: list of elements to sort
    @return: sorted list of elements
    """
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
    return data
    