n = 1
while n > 0:
  SetNum = int(input())
  if SetNum == 0:
    break
  names1 = []
  names2 = []
  for i in range(0,SetNum):
    if i%2 == 0:
      names1.append(input())
    else:
      names2.append(input())
  names2 = names2[::-1]
  print('SET',n)
  n = n+1
  for a in names1:
    print(a)
  for b in names2:
    print(b)
