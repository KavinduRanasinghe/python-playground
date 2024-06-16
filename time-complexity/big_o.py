#O(1)  - Constant time
#The runtime is constant
#Therefore it is denoted as O(1)

def access_element(arr,index):
    return arr[index]


#O(n) -Linear Time
#When the input size doubles the output is also doubled
def linear_search(arr,target):
    for item in arr:
        if item==target:
            return True
    return False

#O(n^2) - Quadratic time
#when the input size increases , the runtime increseas quadratically
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr[j] , arr[j+1]=arr[j+1],arr[j]
         
                
#O(log n) - Logarithmic Time
#Runtimes grow logarithmically with the size of the input data
#Binary search drastically reduces the search time as the size of the sorted list
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            left  = mid -1
    return -1