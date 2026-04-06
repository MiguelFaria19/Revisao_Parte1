# Enunciado: Corrija o código para adicionar um produto na lista apenas se ele ainda não existir.
# O programa deve mostrar o estoque atualizado após cada tentativa.

estoque = ["Notebook", "Mouse", "Teclado"]
 
def adicionar_produto(lista, produto):
    if produto in lista:
        print("Estoque 1:", lista)
    else:
        lista.append(produto)
        print("Estoque 2:", lista)
 
adicionar_produto(estoque, "Monitor")
adicionar_produto(estoque, "Mouse")