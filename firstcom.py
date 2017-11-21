n = input("Enter no of process?")
burst=[];
waiting=[];
total=[];
def forsum(wait):
    sum=0;
    for x in wait:
        sum+=x;
    return sum;
for i in range(0,int(n)):
    x=input("Enter burst time for process no "+str(i+1)+" ")
    burst.append(int(x))
waiting.append(0)
for i in range (1,int(n)):
    waiting.append(waiting[i-1]+burst[i-1])
for i in range(0,int(n)):
    total.append(waiting[i]+burst[i])
print("Burst time  Waiting time  total time")
for i in range(0,int(n)):
    print(burst[i],"        ",waiting[i],"       ",total[i])
avg = forsum(waiting)/int(n)

print("The avg waiting time is " , avg)

