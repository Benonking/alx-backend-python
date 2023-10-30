from functools import wraps
def a_decorator(func):
	@wraps(func)
	def wrapper(*args,** kw):
		'''wrapper fun'''
		func()
	return wrapper
@a_decorator
def first_function():
	'''docstring fot first function'''
	print("first function")
@a_decorator
def second_func(a):
	'''doc 4 2'''
	print("second function")


print(first_function.__name__)
print("First function")
print(first_function.__doc__)
print(second_func.__name__)
print(second_func.__doc__) 