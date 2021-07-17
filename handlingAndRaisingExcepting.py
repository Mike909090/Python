#using exceptions
try:
    print(ourVariable)
except Exception as e:
	print('ourVariable is not defined',"""
	""", e)
finally:
	print('Output is printed successfully')

#rasining an error

def print_five_items(data):
#if number I want iusnt five, I raise an error
    if len(data) != 5:
        raise ValueError("The argument must have five elements")
    for item in data:
        print (item)
print_five_items([5,2,3,4,5])
