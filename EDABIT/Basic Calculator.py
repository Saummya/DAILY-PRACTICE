'''
Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.

Examples
calculator(2, "+", 2) ➞ 4

calculator(2, "*", 2) ➞ 4

calculator(4, "/", 2) ➞ 2
Notes
If the input tries to divide by 0, return: "Can't divide by 0!"
'''
def calculator(num1, operator, num2):
	op=["+","-","*","/"]	
	if operator in op:
		if operator=="+":
			return num1+num2
		if operator=="-":
			return num1-num2
		if operator=="*":
			return num1*num2
		if operator=="/":
			if num2==0:
				return ("Can't divide by 0!")
			else:
				return num1/num2
		
	
