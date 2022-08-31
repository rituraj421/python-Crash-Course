friends = ['rituraj', 'ritu']
for friend in friends:
    print("hi "+ friend)

for i in range(10):
    print("Hello ritu")

for i in range(10):
    print(i)

for i in range(4):
    print("i =", i)


#seconds in a week program
secondsPerDay = 86400;

daysInAWeek = 7;

secondsInAWeek = daysInAWeek * secondsPerDay;

print(secondsInAWeek)


#password generator
alphabet = 26

letters_in_word = int(input("Enter the number of letters should be in the password : "))

no_of_possibilities = alphabet**letters_in_word

print("No.of possible passwords formed with 6 letters are : ",no_of_possibilities)