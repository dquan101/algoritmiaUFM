from fractions import Fraction
from math import ceil
'''Este algoritmo es codicioso debido a que en cada iteración elige la opción optima. Puede ser que no alcanze una solución óptima global, pero si alcanza una cercana a esta'''
def codicioso(a):
  results = []

  while a > 0:
    if a.numerator == 1:
      results.append(a)
      break
    x = Fraction(1, ceil(a.denominator/a.numerator))
    a = a - x
    results.append(x)
  return tuple(results)

if __name__ == "__main__":
  a = (int(input("Denominador: ")))
  b = (int(input("Numerador: ")))
  print(greedy(Fraction(a,b)))
