# Enunciado: Corrija o cálculo do total de vendas tratando possíveis erros de conversão.
 
vendas_dia = {"Notebook": 2500, "Mouse": 80, "Teclado": 150}
 
def total_vendas(vendas):
    total = 0
    for valor in vendas.values():
        try:
            total += int(valor)
        except:
            pass
    return total
 
print("Total de vendas:", total_vendas(vendas_dia))