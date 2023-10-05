number = int(input("Enter a five-digit integer: "))
ones = number % 10
tens = (number // 10) % 10
power = tens ** ones
result = (number // 100) * power
thousands = (number // 1000) % 10
tens_thousands = (number // 10000) % 10
difference = tens_thousands - thousands
if difference != 0:
    final_result = result / difference
    print("Result:", final_result)
else:
    print("Error: the difference between the number of tens of thousands and the number of thousands is zero")
