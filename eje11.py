Not1 = float(input("Ingrese Nota1: "))
Not2 = float(input("Ingrese Nota2: "))

if (Not1 >= 2.5) and (Not2 >= 2.5):
    if (Not1 <= 5) and (Not2 <= 5):
        prom = (Not1 + Not2) / 2

        if prom >= 3.0:
            print("El aprendiz aprueba con: ", prom)
        else:
            print("El aprendiz NO aprueba sus notas: ", prom)
    else:
        print("Solo se admiten notas menores o iguales a 5.0")
else:
    print("Solo se admiten notas mayores o iguales a 2.5")