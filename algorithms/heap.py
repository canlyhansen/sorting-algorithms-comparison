import heapq  

def heap_sort(arr):
    '''
    Convert list to heap structure then take the smallest element one by one.
    '''
    arr = arr.copy()  
    heapq.heapify(arr)                                    # convert list to heap
    return [heapq.heappop(arr) for _ in range(len(arr))]  # repeat the step of taking the smallest element

# Example: 
# arr = [4, 1, 3, 2]
# heapify:
# [1, 2, 3, 4]

# pop → 1
# Heap becomes [2, 4, 3]
# pop → 2
# Heap becomes [3, 4]
# pop → 3
# Heap becomes [4]
# pop → 4

# Complexity:
# Heapify: O(n)
# Pop n times: O(n log n)
# Total: 
# Time Complexity = O(n log n)
# Space:
# O(n) because we make a new list from pop
