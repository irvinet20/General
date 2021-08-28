lim = list(input().split())
cap = int(lim[0])
cur = 0
n = 0
for i in range(0,int(lim[-1])):
  event = list(input().split())
  if event[0] == 'enter':
    if int(event[-1]) + cur <= cap:
      cur = cur + int(event[-1])
    else:
      n = n + 1
  if event[0] == 'leave':
    cur = cur - int(event[-1])
print(n)
