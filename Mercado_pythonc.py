'''
teste de sistema basico de caixa de supermercado em python
parte 1
'''
produtos = {}
precos_produtos = {
  "arroz 5kg": 27.50,
  "feijão 1kg": 7.50,
  "suco de laranja": 6.26,
  "leite 1lt": 4.25,
  "pão": 7.00,
  "refrigerante zero": 7.85,
  "papel toalha": 8.20,
  "molho de tomate": 3.20,
  "barra de chocolate": 6.00,
  "queijo parmesão": 26.50,
  "uva sem semente": 9.45,
  "vinho tinto": 63.60,
  "goiaba": 10.00,
}
descontos_produtos = {
  "vinho tinto": 0.15,
  "goiaba": 0.05
}
total = 0
#salva esse codigo
while True:
  item = input("Digite o nome do produto ou 'final' para finalizar a compra: ").lower()
  if item == "final" or len(item) == 0:
    break
  elif item in precos_produtos:
    if produtos.get(item) == None:
      produtos[item] = 1
    else:
      produtos[item] += 1
  else:
    print("Produto não encontrado. Tente novamente.")

print(f'Produtos do Cliente\n{"-"*30}\n QTD')
for item,quantidade in produtos.items():
  desconto = 0.0
  preco = precos_produtos[item]
  preco_total = preco * quantidade
  if quantidade >= 3 and descontos_produtos.get(item) != None:
    desconto = descontos_produtos[item]
    preco_total -= preco_total * desconto
  total += preco_total
  print(f'Você comprou x{quantidade} {item} R${preco:.2f}, totalizando R${preco_total:.2f}')
  if desconto > 0.0: # Desconto acasso um item com desconto seja selecionado mais de 3 vezes
    print(f'Você comprou mais de 3 {item}s! você ganhou um desconto de {desconto * 100}%')
print(f'Valor total: R${total:.2f}')
