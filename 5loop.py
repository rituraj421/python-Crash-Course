# 1WHILE LOOP

#1
x = int(input("Enter the number: "))
while x < 5:
    print("Not there yer, x=" + str(x))
    x = x+1
    print("x="+str(x))

# 2
def attempts(n):
    y = 2
    while y <= n:
        print("Attempt " + str(y))
        y += 1
    print("Done")

attempts(10)

#3
def count_down(start_number):
    current = start_number
    while (current > 0):
        print(current)
        current -= 1
    print("Zero!")

count_down(3)

#4
# while x%2 == 0:
#     x = x/2
# print(x)

#5
# def print_range(start, end):
# 	# Loop through the numbers from start to end
# 	m = start
# 	while m <= end:
# 		# m =+ 1
# 		print(m)

# print_range(1, 5)


#6 print_prime_factors function print all the prime factors of a number. A prime factor is a number that is prime and divides another without a remainder.
def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)

#7 multiplication table
def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result =  number*multiplier
		# What is the additional condition to exit out of the loop?
		if result>25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	


#FOR LOOP 
#1
def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(1,10):
    print(n, factorial(n))


# NESTED LOOPS
#1
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()

def greet_friends(friends):
    for friend in friends:
        print("Hey " + friend)
greet_friends(["ritu", "rituraj", "nita"]) #don't forget "[]"

#3
# def validate_users(users):
#   for user in users:
#     if is_valid(user):
#       print(user + " is valid")
#     else:
#       print(user + " is invalid")

# validate_users(["purplecat"])

# QUIZ
#1
def factorial(n):
    result = 1
    for x in range(1, n):
        result *= x
    return result

for n in range(0, 10):
    print(n, factorial(n+1))

#2
for x in range(1,11):
  print(x**3)

#3
# def retry(operation, attempts):
#   for n in range(attempts):
#     if operation():
#       print("Attempt " + str(n) + " succeeded")
#       break
#     else:
#       print("Attempt " + str(n) + " failed")

# retry(create_user, 3)