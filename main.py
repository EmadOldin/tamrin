b = c = 0
while True:
    x = input("adad ya amalgar khod ra vared konid : ")
    if x in ["+", "-","*","/"]:
        amalgar = x
        break
    elif float(x) in range(10):
        b = (b * 10) + float(x)
    else:
        print("Please Run Again!")
        break

while True:
    x = input("adad khod ra vared konidn(baraye didane javab = ra vared konid) : ")
    if x == "=":
        break

    else:
        c = (c * 10) + float(x)
if amalgar == "+":
    print(f"{c} + {b} = {b+c}")
elif amalgar == "*":
    print(f"{c} * {b} = {b*c}")
elif amalgar == "/":
    print(f"{c} / {b} = {b/c}")
elif amalgar == "-":
    print(f"{c} - {b} = {b-c}")
