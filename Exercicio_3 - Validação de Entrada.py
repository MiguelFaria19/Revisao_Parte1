# Enunciado: Corrija a função para ler uma quantidade do usuário.
# Deve tratar erros de entrada e repetir até receber um número válido.

def ler_quantidade():
    while True:
        try:
            qtd = int(input("Quantidade: "))
            return qtd  # retorna apenas quando for válido
        except ValueError:
            print("Erro! Digite apenas números.")
quantidade = ler_quantidade()
print("Quantidade válida:", quantidade)