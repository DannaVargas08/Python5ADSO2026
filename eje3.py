frutos_recolectados = int(input("Ingrese la cantidad de frutos recolectados: "))
frutos_producidos = int(input("Ingrese la cantidad de frutos producidos: "))

indice_cosecha = (frutos_recolectados / frutos_producidos) * 100

print("El índice de cosecha es:", indice_cosecha, "%")