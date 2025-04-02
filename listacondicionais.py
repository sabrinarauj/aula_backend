## 1 - Verificar par ou ímpar

num = int(input("Digite um número: "))

if num % 2 == 0:
    print("Esse número é par")
else:
    print("Esse número é ímpar") 

## 2 - Maior que 10

num = int(input("Digite um número: "))

if num > 10:
    print("Maior que 10")
else:
    print("Menor que 10")

## 3 - Maior de idade

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade") 

## 4 - Verificação de voto
idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não tem voto")

elif idade == 16:
    print("Voto opcional")

elif idade == 17:
    print("Voto opcional")

else:
    print("Voto obrigatório")

## 5 - Positivo, negativo ou zero

num = float(input("Digite um número: "))

if num > 0:
    print("O número é positivo")

elif num < 0:
    print("O número é negativo")

elif num == 0:
    print("O número digitado é igual a 0")

## 6 - Nota e menção

nota = int(input("Digite a nota: "))

if nota >= 10:
    print("A menção é A")

elif nota == 7 and nota <= 8:
    print("A menção é B")

elif nota == 6 and nota >= 5:
    print("A menção é C")

elif nota == 4 and nota <= 3:
    print("A menção é D")

elif nota < 2:
    print("A menção é E")

## 7 - Desconto por idade

idade = int(input("Digite sua idade para saber o desconto: "))

if idade <= 12:
    print("Tem direito ao desconto!")

elif idade > 60:
    print("Tem direito ao desconto")

else:
    print("Não tem direito ao desconto") 

## 8 - Triangulo
a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Os lados fornecidos formam um triângulo Equilátero.")
    elif a == b or a == c or b == c:
        print("Os lados fornecidos formam um triângulo Isósceles.")
    else:
        print("Os lados fornecidos formam um triângulo Escaleno.")
else:
    print("Os valores fornecidos não formam um triângulo.")


## 9 - Valor da compra
valor = float(input("Digite o valor total da compra: R$ "))

if valor < 100:
    desconto = 0.05 
elif 100 <= valor <= 500:
    desconto = 0.10  
else:
    desconto = 0.15  

valor_desconto = valor * desconto
valor_final = valor - valor_desconto

print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final da compra: R$ {valor_final:.2f}")


## 10 - Ano bissexto

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")


## 11 - IMC
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)  

print(f"Seu IMC é: {imc:.2f}")  

if imc < 18.5:
    print("Abaixo do peso")

elif 18.5 <= imc and imc <= 24.9:  
    print("Peso normal")

elif 25 <= imc and imc <= 29.9:  #
    print("Acima do peso")

else:  
    print("Obesidade")

## 12 -  Ordem dos numeros
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 < n2 < n3:
    print("Ordem crescente")

elif n1 > n2 > n3:
    print("Ordem decrescente")

else:
    print("Os números são iguais") 

## 13 - Temperatura

temperatura = int(input("Digite a temperatura em Celsius: "))

if temperatura < 10:
    print("A temperatura é fria")

elif temperatura <= 10 and temperatura < 25:
    print("A temperatura é aconchegante")

elif temperatura <= 25 and temperatura <= 40: 
    print("A temperatura está quente")

else: 
    print("A temperatura está muito quente")

## 14 - Converter a data 
data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = data.split("/")

data_formatada = f"{ano}/{mes}/{dia}"

print("Data convertida:", data_formatada)

## 15 - Validação de Senha 
import re

senha = input("Digite a senha: ")
if len(senha) < 8:
    print("A senha deve ter pelo menos 8 caracteres.")
if not re.search(r'[A-Z]', senha):
    print("A senha deve ter pelo menos uma letra maiúscula.")
if not re.search(r'[a-z]', senha):
    print("A senha deve ter pelo menos uma letra minúscula.")
if not re.search(r'\d', senha):
    print("A senha deve ter pelo menos um número.")
if not re.search(r'[@#$%&]', senha):
    print("A senha deve ter pelo menos um caractere especial (@, #, $, %, &).")
if (
    len(senha) >= 8
    and re.search(r'[A-Z]', senha)
    and re.search(r'[a-z]', senha)
    and re.search(r'\d', senha)
    and re.search(r'[@#$%&]', senha)
):
    print("Senha válida!")

## 16 - Raiz Quadrada
import math

num = float(input("Digite um número: "))
if num < 0:
    print("Não é possível calcular a raiz quadrada de um número negativo.")
elif num > 100:
    print("Número muito grande, reduza para um valor abaixo de 100.")
else:
    raiz = round(math.sqrt(num), 2)
    print(f"A raiz quadrada de {num} é {raiz}")

## 17 - Data Formatada
from datetime import datetime

data = input("Digite a data no formato (dd/mm/aaaa): ")
try:

    data_formatada = datetime.strptime(data, "%d/%m/%Y")
    
    data_convertida = data_formatada.strftime("%Y-%m-%d")
    
    print("Data válida: ", data_convertida)

except ValueError:
    print("Data inválida! Verifique o dia, mês e ano inseridos.")

## 18 - Expressões matemáticas 
def analise_expressao():
    try:
        expressao = input("Digite uma expressão matemática: ")  
        resultado = eval(expressao)  
        print("Resultado: ", resultado)
    except Exception as e:
        print("Erro na expressão:", e)

analise_expressao()

## 19 - Desafio CPF 

def calcular_digito(cpf_parcial, pesos):
    soma = sum(int(cpf_parcial[i]) * pesos[i] for i in range(len(cpf_parcial)))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "") 
    if cpf.isdigit() or len(cpf) != 11:
        print( "CPF inválido!")

        cpf_parcial = cpf[:9]
        digito1 = calcular_digito(cpf_parcial, [10, 9, 8, 7, 6, 5, 4, 3, 2])
        digito2 = calcular_digito(cpf_parcial + digito1, [11, 10, 9, 8, 7, 6, 5, 4, 3, 2])

        if cpf == cpf_parcial + digito1 + digito2:
            print("CPF válido") 
        else: 
            print("CPF inválido")

    cpf_usuario = input("Digite seu CPF: ")
    print(validar_cpf(cpf_usuario))













