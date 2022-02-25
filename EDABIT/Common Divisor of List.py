'''
Write a function that returns the greatest common divisor of all list elements. If the greatest common divisor is 1, return 1.

Examples
GCD([10, 20, 40]) ➞ 10

GCD([1, 2, 3, 100]) ➞ 1

GCD([1024, 192, 2048, 512]) ➞ 64
Notes
List elements are always greater than 0.
There is a minimum of two list elements given.'''

import math
def GCD(lst):
	res=lst[0]
	for c in lst[1:]:
		res=gcd(res,c)
	return res
	
def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
		
