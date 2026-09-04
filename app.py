print("Calculadora de Consumo de Energia")

nome_aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (w): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))
dias_por_mes = float(input("Digite quantos dias esse aparelho é usado no mês: "))

consumo_mensal = (potencia * horas_dia * 30) / 1000
tarifa = 0.96
custo = consumo_mensal * tarifa

print("Resultado")
print(f"Aparelho: {nome_aparelho}")
print(f"Potência: {potencia} W")
print(f"Uso diário: {horas_dia} horas")
print(f"Consumo mensal estimado: {consumo_mensal:.2f} kWh")
print(f"Custo mensal estimado: R$ {custo:.2f}")