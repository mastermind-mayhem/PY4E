import time
score = float(input("Enter Score: "))
if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.8:
    print("C")
elif score >= 0.8:
    print("D")
elif score < 0.6:
    print("F")
else:
    print("Luke, I am your father")
    time.sleep(2)
    print("NOOOOOO")
