def square(x):
	return x * x

def sum_squares(x, y):
	return square(x) + square(y)

from math import sqrt

def find_distance(x1, y1, x2, y2):
	"""Returns the Euclidean distance between
	two points: (x1, y1) and (x2, y2)"""
	distance_x = x1 - x2
	distance_y = y1 - y2
	return sqrt(sum_squares(distance_x, distance_y))

def create_point(x, y):
	return (x, y)

def get_x(point):
	return point[0]

def get_y(point):
	return point[1]

def difference(point1, point2):
	x_diff = get_x(point1) - get_x(point2)
	y_diff = get_y(point1) - get_y(point2)
	return x_diff, y_diff


def distance(point1, point2):
	distance_x, distance_y = difference(point1, point2)
	return sqrt(sum_squares(distance_x, distance_y))

def midpoint(point1, point2):
	"""
	x + y / 2
	"""
	x_coord = average(get_x(point1), get_x(point2))
	y_coord = average(get_y(point1), get_y(point2))
	return create_point(x_coord, y_coord)

def average(a, b):
	return (a + b) / 2

def print_items(lst):
	# i = 0
	# while i < len(lst):
	# 	print(lst[i])
	# 	i += 1

	for element in lst:
		print(element)

def divide_filter(lst, n):
	"""Filter out every element that are divisible by a number"""
	return [k for k in lst if k % n == 0]




