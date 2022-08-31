# for x in range(10):
#     for y in range(x):
#         print(y)

def votes(params):
	for vote in params:
	    print("Possible option:" + vote)
votes(['yes', 'no', 'maybe'])