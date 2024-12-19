'''Escreva um programa que inverta os caracteres de um string.
IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
Evite usar funções prontas, como, por exemplo, reverse;'''

string = str(input('Digite qualquer coisa, pois vamos inverter: '))
invertida = ""

for i in string:
  invertida = i + invertida

print(invertida)
