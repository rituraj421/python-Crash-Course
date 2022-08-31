#1 print numbers 1-7
number = 1
while number <= 7:
	print(number, end=" ")
	number += 1

#2 print letter in different line
def show_letters(word):
	for letter in word:
		print(letter)

show_letters("Hello")
# Should print one line per letter

#3
# import math
# def digits(n):
# 	count = 0
# 	if n == 0:
# 	  return 1
# 	while (n>0):
# 		count += 1
# 		n = math.floor(n/10)
# 	return count
	
# print(digits(25))   # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000)) # Should print 4
# print(digits(0))    # Should print 1

#4
def loop(start, stop, step):
	return_string = ""
	if step == 0:
		step = 1
	if start > stop:
		step = abs(step) * -1
	else:
		step = abs(step)
	for count in range(start,stop,step):
		return_string += str(count) + " "
	return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
print(loop(1,1,1)) # Should be empty