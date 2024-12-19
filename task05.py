'''Escreva um programa em pseudocódigo ou em uma linguagem de programação de sua escolha que faça o seguinte:
Receba um número inteiro positivo como entrada
Imprima todos os números pares de 0 até esse número (inclusive)
Se o número for ímpar, imprima também uma mensagem indicando isso
Exemplo de saída para entrada = 7:
0 2 4 6
O número 7 é ímpar'''

numero = int(input('Digite um número inteiro positivo: '))
print()

for i in range(0, numero, 2):
  print(i, end=' ')

print()
if numero % 2 != 0:
  print(f'O número {numero} é ímpar.')
else:
  print(f'O número {numero} é par.')
