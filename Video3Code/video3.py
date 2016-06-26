def square(x):
	return x * x

def hello():
	return "Hello"

def greet(name):
	return hello() + " " + name

def sum_squares(x, y):
	return square(x) + square(y)

from math import sqrt

def find_distance(x1, y1, x2, y2):
	"""Returns the Euclidean distance between
	two points: (x1, y1) and (x2, y2)"""
	distance_x = x1 - x2
	distance_y = y1 - y2
	return sqrt(sum_squares(distance_x, distance_y))
