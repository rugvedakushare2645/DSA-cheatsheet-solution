def maxsub(arr):
    n= len(arr)
    maxSum= currSum = arr[0]
    for i in range(0,n):
        currSum = currSum +arr[i]

        if currSum>maxSum:
            maxSum = currSum

        if currSum<0:
            currSum = 0
    print(maxSum)
    
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxsub(arr)

"""def maximumSubarraySum(arr):
    maxSum = currSum = arr[0]
    for i in range(1, len(arr)):
        currSum = max(arr[i], currSum + arr[i])  # Compare starting new vs continuing
        maxSum = max(maxSum, currSum)
    return maxSum"""
"""def maximumSubarrayWithIndices(arr):
    if not arr:
        return [], 0  # Handle empty input

    maxSum = currSum = arr[0]
    start = end = tempStart = 0

    for i in range(1, len(arr)):
        if arr[i] > currSum + arr[i]:
            currSum = arr[i]
            tempStart = i  # Start new subarray
        else:
            currSum += arr[i]

        if currSum > maxSum:
            maxSum = currSum
            start = tempStart
            end = i

    return arr[start:end + 1], maxSum"""