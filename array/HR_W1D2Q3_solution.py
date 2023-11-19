def countingSort(arr):
    # Write your code here
    frequencyArr = [0]*100
    i=0
    while i<len(arr):
        index=arr[i]
        frequencyArr[index]+=1
        i+=1
    return frequencyArr