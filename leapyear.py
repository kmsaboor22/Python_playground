'''For the learners: you should know that doing something 
like the setup for this challenge inclines you to do is a bad practice. 
Never do the following:
def f():
	if condition:
    	return True
    else:
    	return False

This is just dumb. You are returning a boolean, 
so why even use if blocks in the first place? 
The correct what of doing this would be:

def f():
    	return condition

'''

def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
