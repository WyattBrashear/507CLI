def mixed2frac(whole, numerator, denominator):
  n1 = whole * denominator
  n2 = n1 + numerator
  print("The improper fraction is:", n2, "over", denominator)

def frac2mixed(numerator, denominator):
  n1 = numerator // denominator
  n2 = numerator % denominator
  print("the mixed number is:", n1, "and", n2, "over",         denominator)

def powercalc(base, exponent):
  for i in range(exponent):
    base = base * base
  print(base)