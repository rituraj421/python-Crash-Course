#1
message = "A kong string witha a silly type"

# strings are immutable, we cant manipulate them
#message[2] = "l" #it will throw typeError
print(message)

new_message = message[0:2] + "l" + message[3:]
print(new_message)

#2
"""
firnd the index of x in "BJHVJHAVCJHASCxxHDxbwdbkjsjx"
"""
a = "BJHVJHAVCJHASCxxHDxbwdbkjsjx"
print(a.index("x"))

" ".join(["this", "is"])