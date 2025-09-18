from distance import Distance

distance_1 = Distance(2, "km")
distance_2 = Distance(100, "m")
distance_3 = distance_1 + distance_2
distance_4 = distance_2 - distance_3
distance_5 = distance_3 - distance_2
distance_6 = distance_5 != distance_3

print(distance_1)
print(distance_2)
print(distance_3)
print(distance_4)
print(distance_5)
print(distance_6)