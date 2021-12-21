def is_prime(n):
    if(n==1):
        print("prime")
        break
    for i in range(2,n):
        if(n%i==0):
            print("non prime")
        else:
            print("prime")

int n=3
is_prime(n)