def computepay(h, r):
    if int(h) > 40:
        prcExtr = float(r) * 1.5
        hrsExtr = float(h) - 40
        h = 40
        payExtr = float(prcExtr) * float(hrsExtr)

    pay = str(payExtr + (float(h) * float(r)))
    return pay

hrs = input("Enter Hours:")
prc = input("Enter Price:")
p = computepay(hrs, prc)
print("Pay", p)

