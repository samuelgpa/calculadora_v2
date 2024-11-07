# Inicializando a variável de saída
saida = ''

# Função de adição
def adicao(a, b):
    return a + b

# Função de subtração
def subracao(a, b):
    return a - b

# Função de multiplicação
def multiplicacao(a, b):
    return a * b

# Função de divisão
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Função calculadora
def calculadora(num1, num2, operacao):
    resultado = None
    if operacao == '+' or operacao.lower() == 'adição':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtração':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicação':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisão':
        resultado = divisao(num1, num2)
    else:
        return "Operação inválida"
    
    return resultado

# Laço while para continuar executando o programa
while saida.lower() != 'n':
    # Entrada do usuário
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, / ou seu nome): ")

    # Chamando a função calculadora
    resultado = calculadora(primeiro_numero, segundo_numero, operacao)

    # Imprimindo o resultado
    print(f'Resultado da operação: {resultado}')

    # Perguntando se o usuário deseja continuar
    saida = input("Deseja continuar? (S/N): ")

print("Programa encerrado.")