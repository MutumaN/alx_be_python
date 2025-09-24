num1, num2 = int(input("Enter the first number: ")), int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
	case operation if operation == "+":
		print(f"The result is [{num1 + num2}].")
	case operation if operation ==  "-":
		print(f"The result is [{num1 - num2}].")
	case operation if operation == "*":
		print(f"The result is [{num1 * num2}].")
	case operation if operation == "/":
		try:
			num1 / num2
			print(f"The result is [{num1 / num2}].")
		except ZeroDivisionError:
			print("Cannot divide by zero.")

	case _:
		print("Something went haywire!")