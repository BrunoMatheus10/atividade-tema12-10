# Solicita ao usuário que insira um número de 1 a 10
numero = int(input("Digite um número de 1 a 10: "))

# Verifica se o valor inserido está fora do intervalo permitido
# Se o número estiver fora do intervalo, solicita novamente até que um valor válido seja inserido
while numero < 1 or numero > 10:
    print("Digite um valor entre 1 e 10.")
    numero = int(input("Digite um número de 1 a 10: "))

# Lista de números de 1 a 10
# Esta lista será usada para iterar e gerar a tabuada
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exibe a tabuada do número digitado usando o laço de repetição PARA (for)
print(f"Tabuada do {numero}:")
# Laço de repetição PARA (for) para iterar sobre cada número na lista 'numeros'
for vez in numeros:
    # Calcula o resultado da multiplicação do número digitado pelo usuário com o valor atual de 'vez'
    # Exibe o resultado da multiplicação no formato "numero x vez = resultado"
    print(f"{numero} x {vez} = {numero * vez}")
