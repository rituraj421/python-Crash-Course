# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller,bigger = order_numbers(100, 99)
print(smaller,bigger)

# What are the values passed into functions as input called?

# Parameters



def lucky_number(name):
  number = len(name) * 9
  print("Hello " + name + ". Your lucky number is " + str(number))
	    
(lucky_number("Kay"))
(lucky_number("Cameron"))


# Question 5
# What is the purpose of the def keyword?

# 1 point

# Used to define a new function


