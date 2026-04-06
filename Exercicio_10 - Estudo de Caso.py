# Enunciado:
# A TechZone precisa de um sistema de estoque. O código abaixo contém vários bugs.
# Corrija todos os problemas para que o sistema funcione corretamente com as seguintes funcionalidades:
# - Cadastrar novo produto
# - Buscar produto (busca sequencial)
# - Atualizar quantidade em estoque
# - Encontrar o produto mais barato acima de um determinado preço (usando busca binária)
# - Gerar relatório completo do estoque
# Trate todos os erros de entrada do usuário de forma amigável.
 
estoque = [
    {"nome": "notebook dell", "quantidade": 8, "preco": 2899.90},
    {"nome": "mouse logitech", "quantidade": 45, "preco": 89.90},
    {"nome": "teclado mecânico", "quantidade": 12, "preco": 249.90},
    {"nome": "monitor 24", "quantidade": 15, "preco": 899.90}
]
 
def cadastrar_produto():
    nome = input("Nome do produto: ").lower()
    try:
        quantidade = int(input("Quantidade inicial: "))
        preco = float(input("Preço unitário: "))
    except:
        print("Erro: quantidade e preço devem ser números!")
        return
    estoque.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    print(f"Produto {nome} cadastrado com sucesso!")


def buscar_produto(nome_busca):
    for produto in estoque:
        if produto["nome"] == nome_busca:
            return produto
    return None


def atualizar_quantidade(nome, quantidade_alterada):
    produto = buscar_produto(nome)
    if produto:
        produto["quantidade"] += quantidade_alterada
        print(f"Estoque atualizado! {nome} agora tem {produto['quantidade']} unidades.")
    else:
        print("Produto não encontrado!")


def produto_mais_barato_acima_de(preco_minimo):
    precos = []
    for p in estoque:
        precos.append(p["preco"])
    precos.sort()
    baixo = 0
    alto = len(precos) - 1
    resultado = None
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if precos[meio] >= preco_minimo:
            resultado = precos[meio]
            alto = meio - 1
        else:
            baixo = meio + 1
    if resultado is None:
        return "Nenhum produto encontrado acima desse preço."
    return f"Produto mais barato acima de R${preco_minimo}: R${resultado}"
 
 
def gerar_relatorio():
    if not estoque:
        print("Estoque vazio!")
        return
    total_estoque = 0
    print("\n--- Relatório de Estoque ---")
    for produto in estoque:
        valor_total = produto["quantidade"] * produto["preco"]
        total_estoque += valor_total
        print(f"{produto['nome']:25} | Qtd: {produto['quantidade']:3} | Preço: R${produto['preco']:.2f} | Total: R${valor_total:.2f}")
    print(f"\nValor total em estoque: R${total_estoque}")
 
 
def menu():
    while True:
        print("\n=== TechZone - Controle de Estoque ===")
        print("1. Cadastrar novo produto")
        print("2. Buscar produto")
        print("3. Atualizar quantidade")
        print("4. Produto mais barato acima de um preço")
        print("5. Gerar relatório completo")
        print("6. Sair")
 
        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número.")
            continue
 
        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            nome = input("Digite o nome do produto: ").lower()
            prod = buscar_produto(nome)
            if prod:
                print(f"Encontrado: {prod['nome']} - Qtd: {prod['quantidade']} - R${prod['preco']:.2f}")
            else:
                print("Produto não encontrado.")
        elif opcao == 3:
            nome = input("Nome do produto: ").lower()
            try:
                qtd = int(input("Quantidade a adicionar/subtrair (use negativo para saída): "))
                atualizar_quantidade(nome, qtd)
            except:
                print("Quantidade inválida!")
        elif opcao == 4:
            try:
                preco = float(input("Preço mínimo: R$"))
                print(produto_mais_barato_acima_de(preco))
            except:
                print("Preço inválido!")
        elif opcao == 5:
            gerar_relatorio()
        elif opcao == 6:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
menu()