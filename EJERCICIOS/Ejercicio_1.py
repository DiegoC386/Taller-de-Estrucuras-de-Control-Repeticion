"""
Sea N y K dos enteros positivos, con K < N. Se desea
escribir un programa que escriba el valor de N,N­1,N­2,...,
y así sucesivamente hasta llegar al valor de K.
"""
N=int(input("ingrese N: "))
K=int(input("Ingrese K: "))
Nnum=N+1
while (N>K):
  lista=[]
  for i in range (K,Nnum):
    lista.append(i)
  lista.sort(reverse=True)
  print(lista)
  break
else:
  print("K debe ser menor que N")