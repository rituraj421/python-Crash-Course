# Data types in python

# In Python, text in between quotes -- either single or double quotes -- is a string data type. An integer is a whole number, without a fraction, while a float is a real number that can contain a fractional part. For example, 1, 7, 342 are all integers, while 5.3, 3.14159 and 6.0 are all floats.

# When attempting to mix incompatible data types, you may encounter a TypeError. You can always check the data type of something using the type() function.

#example 1
a = 4
b = "5"
#print(a+b) #it eill throw typeError , as a integer and an string cannot be added

c = 4
d = "5"
print(a + int(b)) #this is the explicit conversion , here we converted string to int and then added both the integers

#VARIABLES

# python variables are case sensitive
# basicalle "variables = value"
# variables can't start wiith a number , it must be alphabet aur underscore
# it can't have white spaces
base = 5
height = 3
area = (base*height)/2

print(area)

print("cat" > "Cat") #try it with replacing ">" with +, -, < operators