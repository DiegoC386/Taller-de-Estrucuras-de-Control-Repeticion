"""
Efectuar la división de dos números enteros, utilizando
el método de las restas sucesivas. Observe el siguiente ejemplo:
Dividir 8 entre 2
8 – 2 = 6
6 – 2 = 4	   número de restas efectuadas es igual al cociente =4
4 – 2 = 2
2 – 2 = 0    %resto de la división
Imprima el restante efectuado Ejemplos de prueba
"""
Cont=0
Dividendo=int(input("Ingresar Dividendo: "))
Divisor=int(input("Ingresar Divisor: "))
Dividendo=Dividendo-Divisor

while (Dividendo>=0):
	Cont=Cont+1
	Dividendo=Dividendo-Divisor
print("La Division es igual a: "+ str(Cont))