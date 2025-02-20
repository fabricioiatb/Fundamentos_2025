#ex1
altura = float(input("Informe sua altura: "))

pi = (72.7 * altura) - 58
print("Seu peso ideal é:", pi)

#ex2
km = int(input("Informe a distancia em Km rodados: "))
d = int(input("Informe a quantidade de dias utilizando o carro:"))
total = (km * 0.15) + (d * 60)
print("Total a pagar:", total)

#ex3
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos
print(f"O total em segundos é: {total}")

