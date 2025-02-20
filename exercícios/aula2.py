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

#ex4
salarioh = float(input("Quanto você ganha por hora? R$ "))
horastb = float(input("Quantas horas você trabalha no mês? "))
salario_bruto = salarioh * horastb
descontoir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - descontoir - desconto_inss - desconto_sindicato

print(f"\nSalário bruto: R$ {salario_bruto:.2f}")
print(f"Desconto imposto de renda (11%): R$ {descontoir:.2f}")
print(f"Desconto INSS (8%): R$ {desconto_inss:.2f}")
print(f"Desconto sindicato (5%): R$ {desconto_sindicato:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
