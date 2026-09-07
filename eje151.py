inicio = int(input("Ingrese el número inicial: "))
final = int(input("Ingrese el número final: "))

for numero in range(inicio, final + 1):
    print("Tabla del", numero)

    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

    print()