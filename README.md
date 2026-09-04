# Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Projeto-black?logo=github)

## Sobre o projeto:
Este projeto é uma **Calculadora de Consumo de Energia**, desenvolvida em **Python** 🐍.
O programa pede o **nome do aparelho, sua potência em watts e o tempo de uso médio diário**, para calcular o consumo mensal em kWh e em R$.

## Objetivo:
Esse projeto é um trabalho que fiz para meu curso, como forma de aprendizado da linguagem Python e do uso do Git e do GitHub.

## Fórmulas utilizadas nos cálculos:
```text
Consumo mensal = (Potência × Horas por dia × 30) ÷ 1000
```
### Onde:
- **Potência** = potência do aparelho em watts (W).
- **Horas por dia** = tempo médio de uso diário.
- **30** = quantidade considerada de dias no mês.
- **1000** = conversão de Wh para kWh.
- 
```text
tarifa = 0.96
custo = consumo_mensal * tarifa
```
### Onde:
- **Tarifa** = valor cobrado por 1 kWh.
- **Custo** = valor estimado a ser pago pelo consumo do aparelho.
- **Consumo Mensal** = consumo estimado do aparelho em kWh.

### Exemplo:
Considere um aparelho com potência de 8000 W utilizado durante 3 horas por dia:

```text
Consumo mensal = (8000 × 3 × 30) ÷ 1000
Consumo mensal = 720 kWh
```
## Como executar:
### 1. Instale o Python
É necessário ter o **Python 3** instalado em seu computador para executar o programa.
### 2. Abra a pasta do projeto
Abra o terminal na pasta "Consumo-Energia", onde estão os arquivos "app.py" e "README.md".
### 3. Execute o programa
No terminal, utilize o comando: "python app.py".
Após executar o comando, o programa solicitará o nome do aparelho, a potência em watts e o tempo médio de uso diário.

## Autor(a)
### Giovana Brizaco Reimberg