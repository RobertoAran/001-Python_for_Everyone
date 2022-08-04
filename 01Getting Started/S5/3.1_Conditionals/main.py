hrs = input("Enter Hours:")
prc = input("Enter Price:")

if int(hrs) > 40 :
    prcExtr = float(prc) * 1.5
    hrsExtr = float(hrs) - 40
    hrs = 40
    payExtr = float(prcExtr) * float(hrsExtr)

pay = str(payExtr + (float(hrs) * float(prc)))

print(pay)
