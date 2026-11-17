# Projeto de Analise Quantitativa - Cotilde Filipe
# Calcula lucro de Bitcoin

preco_ontem = 85000
preco_hoje = 90000
lucro = preco_hoje - preco_ontem

print(f"Preço ontem: {preco_ontem}")
print(f"Preço hoje: {preco_hoje}")
print(f"Lucro: {lucro} USD")

# Se lucro for positivo, foi um bom dia
if lucro > 0:
    print("Resultado positivo - bom para analise quantitativa")
