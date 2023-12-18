# bounce.py
#
# Exercise 1.5

initial_height_meters = 100
depreciation_factor = 0.60
n_bounces = 10

height = initial_height_meters
for i in range(n_bounces):
    height = height * depreciation_factor
    print(round(height, 4))
