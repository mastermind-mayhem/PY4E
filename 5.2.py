largest = None
smallest = None
while True:
    var = input("Enter a Number: ")
    if var == "done":
        break
    try:
        var = int(var)
        if largest is None or var > largest:
            largest = var
        if smallest is None or var < smallest:
            smallest = var
    except:
        print("Invalid input")
        continue
largest = str(largest)
smallest = str(smallest)
print("Maximum is "+largest)
print("Minimum is "+smallest)
