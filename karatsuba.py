def ev_length(x_str, y_str):
	y_str = y_str.rjust(len(x_str), '0')
	return x_str, y_str


def karacuba(x, y):
	x_str = str(x)
	y_str = str(y)

	if len(x_str) <=1 or len(y_str) <=1:
		# print(x_str, y_str, 'mult =', int(x_str) * int(y_str))
		return int(x_str) * int(y_str)

	if len(x_str) > len(y_str):
		x_str, y_str = ev_length(x_str, y_str)
	elif len(y_str) > len(x_str):
		x_str, y_str = ev_length(y_str, x_str)

	a = x_str[ : len(x_str)//2]
	b = x_str[len(x_str)//2 : len(x_str)]

	c = y_str[ : len(y_str)//2]
	d = y_str[len(y_str)//2 : len(y_str)]
	# print('abcd: ',a,b,c,d)
	return (10**(len(x_str)-len(x_str)//2 + len(y_str) - len(y_str)//2))*karacuba(a,c) \
		    + (10**(len(x_str)-len(x_str)//2))*(karacuba(a,d) +karacuba(b,c)) + karacuba(b,d)

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print(karacuba(x,y))
print(x*y)
print(x*y - karacuba(x,y))