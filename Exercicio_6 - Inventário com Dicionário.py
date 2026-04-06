# Enunciado: Corrija a função para consultar um produto e mostrar quantidade e preço corretamente.

def consultar_produto(nome):
    inventario = {
    "Notebook": {"qtd": 10, "preco": 2500},
    "Mouse": {"qtd": 50, "preco": 80}}
    if nome in inventario:
        dados = inventario.get(nome)
        print(f"{nome} - Estoque: {dados['qtd']} | Preço: R${dados['preco']}")
    else:
        print("Produto não encontrado")
 
consultar_produto("Mouse")
consultar_produto("Headset")