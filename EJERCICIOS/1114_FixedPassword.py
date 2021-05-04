Pass = int(input())
Cod = 2002

while (Pass != Cod):
  print("Senha Invalida")
  Pass = int(input())
  if (Pass == Cod):
    print("Acesso Permitido")