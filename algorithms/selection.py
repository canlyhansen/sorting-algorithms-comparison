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

# Example:
# arr = [64, 25, 12, 22, 11]
# First iteration: 
# [11, 25, 12, 22, 64]
# Second iteration: 
# [11, 12, 25, 22, 64]
# Third iteration: 
# [11, 12, 22, 25, 64]
# and so on

# Complexity: 
# Time Complexity: O(n²) (loop in loop)
# Space Complexity: O(1) (in-place, but a copy in front)
