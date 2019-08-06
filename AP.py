[a,n,d]=list(map(int,input().split()))

def sumOfAP( a, n, d) : 
    num = n + ((a-1)*d);
    res = a*(n+num);
    res //= 2;
    return res;
      
 



print (sumOfAP(a, n, d),end=" ")
