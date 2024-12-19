'''Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;'''

num = int(input('Digite um número: '))
fibo = [0, 1]
a = fibo[-1]
fibonacci = False

while a <= num:
  if a == num:
    fibonacci = True
    break
  a = a + fibo[-2]
  fibo.append(a)

if fibonacci:
  print(f'O número {num} pertence à sequência Fibonacci')
  print(f'Sequência até o número:{fibo}')
else:
  del(fibo[-1])
  print(f'O número {num} não pertence à sequência Fibonacci')
  print(f'Sequência até o número: {fibo}')
