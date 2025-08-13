# 🛒 Cálculo de Desconto em Produto com Python

Este repositório contém um script simples em Python que permite ao usuário inserir informações sobre um produto, calcular o valor de desconto com base em uma porcentagem e exibir o preço final formatado.

## 📋 Descrição

O programa solicita que o usuário informe:

- O nome do produto
- O preço original do produto
- A porcentagem de desconto a ser aplicada

Em seguida, o programa:

1. Calcula o valor do desconto;
2. Subtrai o desconto do preço original;
3. Exibe as informações formatadas no terminal.

## 💻 Código

```python
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
