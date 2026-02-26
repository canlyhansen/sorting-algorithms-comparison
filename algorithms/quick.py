def quick_sort(arr):
    '''
    Choose one number as pivot, divide array into 3 parts then order left and right part recursively.
    left: number < pivot
    middle: number == pivot
    right: number > pivot
    '''

    if len(arr) <= 1:                                      # to prevent endless recursion
        return arr

    pivot = arr[len(arr) // 2]                             # pivot is in the middle
    left = [x for x in arr if x < pivot]                   # smaller than pivot
    middle = [x for x in arr if x == pivot]                # if there is any duplicate
    right = [x for x in arr if x > pivot]                  # larger than pivot

    return quick_sort(left) + middle + quick_sort(right)

# example:
# arr = [5, 3, 8, 4, 2]

# pivot = 8  (middle element)
# left   = [5, 3, 4, 2]
# middle = [8]
# right  = []

# quick_sort([5,3,4,2])
# pivot = 4
# left = [3,2]
# middle = [4]
# right = [5]

# keep recursion until array is sorted: [2,3,4,5]
# combine [2,3,4,5] + [8] + [] = [2,3,4,5,8]
