def buy_sell(arr):
    n=len(arr)
    count=[]
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                mini=arr[i]
                maxi=arr[j]
            

    return maxi-mini

pirnt(buy_sell())
