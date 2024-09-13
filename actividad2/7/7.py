
a = float(input("ingrese la nota del taller: "))
if a < 1:
    print("NOTA INVALIDA INGRESELA NUVAMENTE")
elif a > 5:
    print("NOTA INVALIDA INGRESELA NUEVAMENTE")

b = float(input("ingrese la nota del taller 2: "))
if b < 1:
    print("NOTA INVALIDA INGRESELA NUVAMENTE")
elif b > 5:
    print("NOTA INVALIDA INGRESELA NUEVAMENTE")

c = float(input("ingrese la nota del cuestionario 1: "))
if c < 1:
    print("NOTA INVALIDA INGRESELA NUVAMENTE")
elif c > 5:
    print("NOTA INVALIDA INGRESELA NUEVAMENTE")

d = float(input("ingrese la nota del cuestionario 2: "))
if d < 1:
    print("NOTA INVALIDA INGRESELA NUVAMENTE")
elif d > 5:
    print("NOTA INVALIDA INGRESELA NUEVAMENTE")
e = float(input("ingrese la nota del proyecto final: "))
if e < 1:
    print("NOTA INVALIDA INGRESELA NUVAMENTE")
elif e > 5:
    print("NOTA INVALIDA INGRESELA NUEVAMENTE")


promedio = (a*0.20) + (b*0.15) + (c*0.22) + (d*0.10) + (e*0.33)
promedio = round(promedio, 2)

if promedio > 4.5:
    print(f"tu desempeño fue excelente y tu nota definitiva es: {promedio}")
elif promedio > 3.5:
    print(f"tu desempeño fue bueno y tu nota definitiva es: {promedio}")
elif promedio > 3:
    print(f"tu desempeño fue regular y tu nota definitiva es: {promedio}")
else:
    print(f"tu desempeño fue insuficiente y tu nota definitiva es: {promedio}")
