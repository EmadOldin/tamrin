from math import sqrt
a = float(input("Zarib x^2 : "))
b = float(input("Zarib x : "))
c = float(input("Adade sabet : "))

delta = (b**2)-(4*a*c)

if delta == 0:
	print(-b/(2*a))
	
elif delta <0:
	print("Hich meghdari nadarad!")
	
else :
	# using math library
	# print(f"Rishe 1 : {(-b+sqrt(delta))/(2*a)}")
	# print(f"Rishe 2 : {(-b-sqrt(delta))/(2*a)}")
	# ----------------------------------------------------	
	# with out math library
	print(f"Rishe 1 : {(-b + (delta ** 0.5)) / (2*a)}")
	print(f"Rishe 2 : {(-b - (delta ** 0.5)) / (2*a)}")
