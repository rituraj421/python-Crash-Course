# here we will solve some practice questions

#  Q1)In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number.

# ANS
from turtle import screensize


bill = 47.28
tip = 7.092
total = 47.28 + 7.092
share = 27.186 
print("Each person needs to pay:" + str(share))

# Q2)Combine the variables to display the sentence "How do you like Python so far?" 
# ANS:

word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print((word1) + " " + str(word2) + " " + str(word3) + " " + str(word4) + " " + str(word5) + " " + str(word6) + " " + str(word7))

# Q3) display 2+2 = 4 on screen 

a = 2
b = a+a
print("2 + 2 = " + str(b) )