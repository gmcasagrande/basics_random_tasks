'''Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53
Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.'''

fat_SP = float(67836.43)
fat_RJ = float(36678.66)
fat_MG = float(29229.88)
fat_ES = float(27165.48)
fat_OU = float(19849.53)
fat_total = float(fat_SP + fat_RJ + fat_MG + fat_ES + fat_OU)

p_SP = int((fat_SP * 100) / fat_total)
p_RJ = int((fat_RJ * 100) / fat_total)
p_MG = int((fat_MG * 100) / fat_total)
p_ES = int((fat_ES * 100) / fat_total)
p_OU = int((fat_OU * 100) / fat_total)

print(f'O faturamento do estado de SP corresponde a {p_SP}% do total.')
print(f'O faturamento do estado do RJ corresponde a {p_RJ}% do total.')
print(f'O faturamento do estado de MG corresponde a {p_MG}% do total.')
print(f'O faturamento do estado do ES corresponde a {p_ES}% do total.')
print(f'O faturamento dos outros estados corresponde a {p_OU}% do total.')
