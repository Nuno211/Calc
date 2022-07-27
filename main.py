
def add(x,y): return x+y
def subtract(x,y): return x-y
def mult(x,y): return x*y
def div(x,y): return x/y

nome=input('Seu nome: ')
op=0

while int(op)!=5:
  print()
  print("Menu")
  print("1 - soma")
  print("2 - subtração")
  print("3 - multiplicação")
  print("4 - divisão")
  print("5 - sair")
  print()
  op=input('Opção? ')
  print()
  if int(op)==5:
    break
  x=input('x? ')
  y=input('y? ')
  nome= f'Olá {nome.upper()}'
  print()
  print(nome)
  print('resposta: ', end='')
  if int(op)==1:
    print(add(int(x),int(y)))
  elif int(op)==2:
    print(subtract(int(x),int(y)))
  elif int(op)==3:
    print(mult(int(x),int(y)))
  elif int(op)==4:
    print(div(int(x),int(y)))
            

print('Fim')
print()