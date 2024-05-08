input_number = 5

length = len(str(input_number**2))

for x in range(input_number+1):
    if x < 1: 
        print(" ","   ".join([str(a).rjust(length, " ") for a in range(1, input_number + 1)]))
    else: 
        print(x, "   ".join(str(x * a).rjust(length, " ") for a in range(1, input_number+1)))