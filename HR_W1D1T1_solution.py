def findMedian(arr):
    # Write your code here
    sortedArr=sorted(arr)
    length=len(arr)
    return sortedArr[length//2]