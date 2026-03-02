def insertion_sort(arr):
    '''
    For every iteration, we take one element and insert it into the correct position 
    in the already sorted left part of the array.
    Copy function is added to prevent the original data from any change.
    '''
    arr = arr.copy()
    n = len(arr)
    
    for i in range(1, n):  
        key = arr[i]                    # element to be inserted
        j = i - 1
        
        while j >= 0 and arr[j] > key:  # shift elements greater than key
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key                # place key in correct position
    
    return arr


# Example:
# arr = [64, 25, 12, 22, 11]

# First iteration (i = 1):
# [25, 64, 12, 22, 11]

# Second iteration (i = 2):
# [12, 25, 64, 22, 11]

# Third iteration (i = 3):
# [12, 22, 25, 64, 11]

# Fourth iteration (i = 4):
# [11, 12, 22, 25, 64]

# and so on


# Complexity:
# Best Case: O(n)   (already sorted, only one comparison per iteration)
# Average Case: O(n²)
# Worst Case: O(n²) (reverse sorted, maximum shifting)
# Space Complexity: O(1) (in-place, but a copy in front)