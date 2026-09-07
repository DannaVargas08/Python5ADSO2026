estado_civil= input("Ingrese estado civil (S,C):")
edad= int(input("ingrese su edad: "))
buena_persona = input("¿Es buena persona?(S,C):")
linda= input("¿Es linda?(S,C):")
if estado_civil=="C":
    print ("No me caso! Ni me comprometo")
elif edad <= 30 and linda == "S" or buena_persona == "S":
    print ("Si me caso!")
else:
    print ("Solo me comprometo")