#code
t = int(input())
for k in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    for i in range(n):
        print(p.pop(),end=' ')
    print()