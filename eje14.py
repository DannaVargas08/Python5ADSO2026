print("Ingrese el numero de la tabla de multiplicar: ")
multp = int(input())
print("Ingrese rango final: ")
rang = int(input())
print("Ingrese rango inicial: ")
i = int(input())
if i>=rang:
    print("El rango final no puede ser mayor que el rango inicial")
else:
     while i<=rang:
         res=multp*i
         print(multp,"x",i,"=",res)
         i=i+1