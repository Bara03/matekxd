from fractions import Fraction
num = round(1.2133516482134197,2)
print(Fraction(str(num)).limit_denominator(1000))