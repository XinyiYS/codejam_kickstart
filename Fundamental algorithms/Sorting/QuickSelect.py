# Python program for implementation of Quicksort Sort 
  
# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSelect(arr,low,high,k): 
    if k > 0 and k <= high - low + 1:
        if low==high:return arr[low]
        pi = low

        pi = partition(arr,low,high)
        
        if  k - 1 == pi - low: 
            return arr[pi]
        elif k - 1 < pi - low:
            return quickSelect(arr,low,pi-1,k)
        else:
            return quickSelect(arr,pi+1,high,k - pi + low -1)
    else:
        return float('Inf')
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
kthSmallest = quickSelect(arr,0,n-1,k=1) 
print ("Sorted array is:", arr)
print("kthSmallest is :", kthSmallest)   
# This code is contributed by Mohit Kumra 