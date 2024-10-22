def second_smallest_and_largest(arr):
    # Remove duplicates and sort the array
    arr = sorted(set(arr))
    
    # If the array has fewer than two unique elements
    if len(arr) < 2:
        return -1, -1
    
    # The second smallest is the second element in the sorted unique array
    second_smallest = arr[1]
    
    # The second largest is the second last element in the sorted unique array
    second_largest = arr[-2]
    
    return second_smallest, second_largest


arr1 = [1, 2, 4, 7, 7, 5]
arr2 = [1]
print("Second Smallest and largest for arr1:", second_smallest_and_largest(arr1))
print("Second Smallest and largest for arr2:", second_smallest_and_largest(arr2))