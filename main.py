from geometry.point import Point

# set two locations
location_1 = Point(345678, 456789)
location_2 = Point(445678, 556789)
print(f"\ninitial locations:\t\t{location_1}, {location_2}")

# calculate distance between them
distance = location_1.distance_to(location_2)
print(f"distance:\t\t\t{distance:.2f}m")

# calculate direction between them
direction = location_1.direction_to(location_2)
print(f"direction:\t\t\t{direction}°")

# calculate location 2 from location 1 and the distance and heading
print(f"location 2 (re-calculated):\t{location_1.offset_by(distance, direction)}")