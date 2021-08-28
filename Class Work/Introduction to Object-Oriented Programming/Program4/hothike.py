n = int(input())
d = -1
high = 41
temps = list(input().split())
temps = list(map(int, temps)) 
for i in range(0,n-2):
  lhigh = max(temps[i],temps[i+2])
  if high > lhigh:
    high = lhigh
    d = i
print(d+1)
print(high)
