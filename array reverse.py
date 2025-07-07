import numpy as np

def reverse(arr):
    n = len(arr)

    temp= [0]*n

    for i in range(n):
        temp[i] = arr[n - i -1]

    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    val = input("enter elemnets separated by space").split()
    arr = np.array(val,dtype = int)

    reverse(arr)
    for i in range(len(arr)):
        print(arr[i],end=" ")

"""def reverseArray(arr):
    
    # Initialize left to the beginning and right to the end
    left = 0
    right = len(arr) - 1
  
    # Iterate till left is less than right
    while left < right:
        
        # Swap the elements at left and right position
        arr[left], arr[right] = arr[right], arr[left]
      
        # Increment the left pointer
        left += 1
      
        # Decrement the right pointer
        right -= 1"""
"""arr.reverse()"""