#!/usr/bin/env python



def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-3)


def fibonacci_v2(n):
	r = 0
	n_1,n_2 = 0,1
	if n == 0:
		return n_1
	if n == 1:
		return n_2
	for i in range(n-2):
		print n_1,n_2
		n_1,n_2 = n_2,n_1+n_2	
	return n_2

#print fibonacci(9)
print fibonacci_v2(10)




