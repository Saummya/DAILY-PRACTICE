power=[]
for i in range(100):
    power.append(3**i)
t= int(input())
for _ in range(t):
    n = int(input())
    count=0
    i=0
    while(power[i]<=n):
        count+=1
        i+=1
    
            
    print(count)
