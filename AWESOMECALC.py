#import libraies
import wml
#main code

def awesomecalc():
  print("Welcome to wyatts AWESOME calculator using wyatts math library!")

  print("Please select an option from the list below:")
  #output text to screen and get operation
  print("1. Fraction to mixed number.")
  print("2. Mixed number to fraction.")
  print("3. Power calculator.")
  print("4. Addition")
  print("5. Subtraction")
  print("6. Multiplication")
  print("7. Division")
  print("8. Floor division")
  print("9. Modulus")
  print("10 Exit")
  op = input("Enter operation: ")
  #run logic
  if op == "2":
    whole = int(input("Whole Number: "))
    num1 = int(input("Numerator: "))
    den1 = int(input("Denominator: "))
    wml.mixed2frac(whole, num1, den1)
  if op == "1":
    num2 = int(input("Numerator: "))
    den2 = int(input("Denominator: "))
    wml.frac2mixed(num2, den2)
  if op == "3":
    base = int(input("Base: "))
    exp = int(input("Exponent: "))
    wml.powercalc(base, exp)
  if op == "4":
    num3 = int(input("First Number: "))
    num4 = int(input("Second Number: "))
    print(num3 + num4)
  if op == "5":
    num5 = int(input("First Number: "))
    num6 = int(input("Second Number: "))
    print(num5 - num6)
  if op == "6":
    num7 = int(input("First Number: "))
    num8 = int(input("Second Number: "))
    print(num7 * num8)
  if op == "7":
    num9 = int(input("First Number: "))
    num10 = int(input("Second Number: "))
    print(num9 / num10)
  if op == "8":
    num11 = int(input("First Number: "))
    num12 = int(input("Second Number: "))
    print(num11 // num12)
  if op == "9":
    num13 = int(input("First Number: "))
    num14 = int(input("Second Number: "))
    print(num13 % num14)
  if op == "10":
    print("")
  else:
    print("")