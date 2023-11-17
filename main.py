b = c = 0
while True:
    x = input("adad ya amalgar khod ra vared konid : ")
    if x == "+":
        amalgar = x
        break
    elif x == "*":
        amalgar = x
        break
    elif x == "/":
        amalgar = x
        break
    elif x == "-":
        amalgar = x
        break
    else:
        b = (b * 10) + float(x)

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
