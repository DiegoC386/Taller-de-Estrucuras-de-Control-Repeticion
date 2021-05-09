"""
Calcule e imprima el número de términos necesarios para
que el valor de la siguiente sumatoria se aproxime los más
cercanamente a 1000 sin que lo exceda:
∑((k**2+1)/k), donde k=1,2,3,4,...
"""
k=int(input("Ingrese numero de terminos: "))
sum1=0
for i in range(1,k+1):
    sum1=sum1+((i**2+1)/i)
if(sum1>1000):
			print("No se puede sumar")
else:
	print("La suma es " ,round(sum1,2))