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
