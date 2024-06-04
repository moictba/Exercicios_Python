# Exercicio 2

# Calcular o IMC de uma pessoa, ao final exebir tópicos abaixo.
# -> Luiz Otávio tem 1.80 de altura, pesa 95 quilos e seu IMC é 29.3209876544320987
#... = Ellpsis -> não gera erro no código

# nome = "Luiz Otávio"
# altura = 1.80
# peso = 95
# imc = ... IMC = peso / (altura x altura)

nome = "Luiz Otávio"
altura = 1.80
peso = 95
imc = peso / (altura ** 2)
print(imc)

print(nome, "tem", altura, "de alura, pesa", peso, "quilos e seu imc é", imc)
