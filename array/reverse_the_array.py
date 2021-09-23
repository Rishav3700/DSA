def reverse1(a):
    return a[::-1]

def reverse2(a,start,end):
    while start<end:
        a[start],a[end]=a[end],a[start]
        start+=1
        end-=1
    return a


array=[1,2,3]
print(reverse1(array))
print(reverse2(array,0,2))