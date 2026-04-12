a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n1.Sub 2.Add 3.Mul 4.Div 5.Mod 6.Pow 7.Floor")
ch = int(input("Choice: "))

if ch == 1: print("Result:", a - b)
elif ch == 2: print("Result:", a + b)
elif ch == 3: print("Result:", a * b)
elif ch == 4: print("Result:", a / b if b != 0 else "Error")
elif ch == 5: print("Result:", b % a if a != 0 else "Error")
elif ch == 6: print("Result:", a ** b)
elif ch == 7: print("Result:", a // b if b != 0 else "Error")
else: print("Invalid choice")