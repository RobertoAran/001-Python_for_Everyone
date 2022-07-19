largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    try:
        num = int(num)
    except:
        if num == "done":
            break
        else:
            print("Invalid input")

    try:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    except:
        if largest is None:
            largest = num
        elif smallest is None:
            smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
