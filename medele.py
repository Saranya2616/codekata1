import statistics
arr=[]
d=int(input())
arr = map(int,input().split())
num=statistics.median(arr)
print(num)
