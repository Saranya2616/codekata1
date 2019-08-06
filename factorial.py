d=int(input())
g=1;  
if d<0:
   print("Invalid input");
else:
    while(d>0):
        g=g*d
        d=d-1
    print(g)
