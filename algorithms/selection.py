def selection_sort(arr): 
    '''
    For every iteration, we search for the smallest number in the array, then put it in front position.
    Copy function is added to prevent the original data from any change.
    '''
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):                    # i+1 is because this left part is ordered
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # order is switched, so that the front position is the smallest number
    return arr
