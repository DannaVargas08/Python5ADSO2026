x = 100
for i in range(x):
    numero = float(input(f"Numero {i + 1}: "))
    if numero < 0:
        print(f"¡Número negativo detectado! ({numero})")
        print("Programa terminado.")
        break
    else:
         print (f"Numero ingresado: {numero}")
print ("Fin del programa.")        