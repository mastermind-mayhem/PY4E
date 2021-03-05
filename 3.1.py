hrs = float(input("Hours:"))
rte = float(input("Rate:"))
if hrs > 40:
    total = hrs*rte
    over = (hrs - 40.0) * (rte * 0.5)
    gtotal = total + over
else:
    gtotal = rte*hrs
print(gtotal)
