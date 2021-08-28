sets = int(input())
for s in range(0,sets):
  locations = []
  trips = int(input())
  for t in range(0,trips):
    city = input()
    if city not in locations:
      locations.append(city)
  print(len(locations))
