nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o desconto (%): "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto
print("---------------------------------------------")
print(f"Nome do produto  | {nome_produto}")
print(f"Preço do produto | R${preco:.2f}")
print(f"Desconto         | {desconto}%")
print(f"Preço final      | R${preco_final:.2f}")
print("---------------------------------------------")