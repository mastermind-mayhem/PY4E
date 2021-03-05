def computepay(hrs,rte):
    if hrs > 40:
    	total = hrs*rte
    	over = (hrs - 40.0) * (rte * 0.5)
    	gtotal = total + over
    else:
        gtotal = rte*hrs
    return gtotal

hrs = float(input("Enter Hours:"))
rte = float(input("Enter Rate:"))
p = computepay(hrs,rte)
print("Pay",p)
