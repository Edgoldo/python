import collections

nums = ["one", "two", "three"]
numDict = {2: "two", 3: "three", 1: "one"}
cities = {2848: 'PANAMÁ', 4001: 'PANAMÁ OESTE', 2850: 'VERAGUAS', 4003: 'Comarca Ngäbe-Buglé', 4004: 'Comarca Emberá-Wounaan', 4002: 'Comarca Guna Yala', 1719: 'COLON', 2841: 'BOCAS DEL TORO', 2842: 'CHIRIQUI', 2843: 'COCLE', 2844: 'COLON', 2845: 'DARIEN', 2846: 'HERRERA', 2847: 'LOS SANTOS'}

for i in nums:
	print(nums.index(i), i)

if ("one" not in nums):
	print("No se encuentra")

cities = collections.OrderedDict(sorted(cities.items()))
del cities[1719]
for city in cities:
	print(city)
print(dict(sorted(numDict.items()))[3])