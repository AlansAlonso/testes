# recebendo a quantidade de termos
quantidade_termos = int(input())

# recebendo os termos individuais corrompitos e realizando a soma
soma = 0

for _ in range(quantidade_termos):
  entrada = input()

  # uma resolução possível, manipulando a str antes de transformar o input em int:

  # expoente = int(entrada[-1])
  # base = int(entrada[0:-1])

  # outra resolução, manipulando numericamente
  entrada = int(entrada)
  expoente = entrada % 10
  base = entrada // 10

  # realizando a soma
  soma += base**expoente

# por algum motivo as vezes esse print é exibido, e as vezes não.
# acho que algum problema no replit no momento
# repetir o comando ajuda
print(soma)
print(soma)
