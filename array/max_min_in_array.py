def max_min(arr,low,high):
    arr_max=arr[low]
    arr_min=arr[low]
    #if there is only one element
    if low==high:
        arr_max=arr[low]
        arr_min=arr[high]
        return (arr_max,arr_min)
    #if there is only two element
    elif high == low+1:
        if arr[low]>arr[high]:
            arr_min=arr[high]
            arr_max=arr[low]
        else:
            arr_min=arr[low]
            arr_max=arr[high]
        return arr_max,arr_min
    #more than two elements
    else:
        mid=int((low+high)/2)
        arr_max1,arr_min1=max_min(arr,low,mid)
        arr_max2,arr_min2=max_min(arr,mid+1,high)
    return (max(arr_max1,arr_max2),min(arr_min1,arr_min2))


a=[1333,0,23,657,888]
low=0
high=len(a)-1
arr_max,arr_min=max_min(a,low,high)
print(arr_min,arr_max)
#print(max(a))
#print(min(a))