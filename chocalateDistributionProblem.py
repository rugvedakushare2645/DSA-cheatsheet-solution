def choc(arr, m):
    n = len(arr)

    minDiff = float('inf')

    arr.sort()

    for i in range(n-m+1):
        diff = arr[i-m+1] - arr[i]

        if(diff<minDiff):
            minDiff = diff

    return minDiff

if __name__ == "__main__":
    arr = [7,3,2,5,6,9]
    m=4

    print(choc(arr, m))
