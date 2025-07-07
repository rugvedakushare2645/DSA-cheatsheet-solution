def min(arr):
    min = arr[0]
    i = arr[1]
    for i in arr:
        if i < min:
            min = i
    return min

def max(arr):
    max = arr[0]
    i = arr[1]
    for i in arr:
        if i > max:
            max = i
    return max


if __name__ == "__main__":
    n = int(input("Enter the length of the array: "))
    arr = [0]*n
    for i in range(n):
        arr[i] = int(input(f"Enter the {i} th element"))

    print("the array elements are: ", arr)
    print("the min is: ",min(arr))
    print("the ,ax is: ",max(arr))



"""val = input("Enter elements separated by space: ").split()

# Convert input elements to a NumPy array
# Convert to integer array, change dtype as needed

arr = np.array(val, dtype=int)"""

"""def getMinMax(arr):
    arr.sort()
    minmax = {"min": arr[0], "max": arr[-1]}
    return minmax"""

""""""