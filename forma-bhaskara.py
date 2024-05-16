#-b ± √(b²-4*a*c)/(2*a)

import math
def bhaskara(a,b,c):
    delta = b**2-4*a*c
    if delta <0:
        return f"Não possui raízes reais"
    elif delta ==0:
        x = -b /(2*a)
        return f"Apenas uma raiz real, X: {x}"
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return f"A raiz real do X1 é {x1}, e a raiz real do X2 {x2}"

a = float(input("Qual é o valor de a: "))
b = float(input("Qual é o valor de b: "))
c = float(input("Qual é o valor de c: "))

print(bhaskara(a,b,c))
print("0brigado :)")