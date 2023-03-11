# calculator
print('insira um valor:')
numero1 = int(input())

print('insira um operador:')
operador = input()

print('insira um valor:')
numero2 = int(input())

if operador == '+':
     resultado = numero1 + numero2
     print('O valor é = ' + str(resultado))

elif operador == '-':
     resultado = numero1 - numero2
     print('O valor é = ' + str(resultado))
elif operador == '*':
     resultado = numero1 * numero2
     print('O valor é = '+ str(resultado))
elif operador == '/':
     resultado = numero1 / numero2
     print('O valor é = ' + str(resultado))
else:
    print('Operador inválido!')



