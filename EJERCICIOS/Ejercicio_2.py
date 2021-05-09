"""
Escriba un programa que imprima todos los enteros positivos
impares menores que 100 omitiéndose aquellos que sean divisibles
por 7.
"""
lista=[]
for i in range(1,101):
  if(i%7!=0):
    lista.append(i)
print(lista) 