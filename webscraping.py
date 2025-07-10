import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.stuttgart.com.br/padaria.html')

if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')
    lista_produto, lista_preco = [], []

    for card in soup.select('.type1 .product-item-details'):
        produto = card.select_one('.type1 .product-item-link')
        preco = card.select_one('.type1 .price')
        codigo = card.select_one('.sku')
        print(produto.text.strip(),'----', preco.text,'-----', codigo.text)

    # for nome_produto in soup.select('.type1 .product-item-link'):
    #     lista_produto.append(nome_produto.text.strip())
    #
    # for nome_preco in soup.select('.type1 .price'):
    #     lista_preco.append(nome_preco.text)
    #
    # for codigo_produto in soup.select('.sku'):
    #     lista_codigo_produto = codigo_produto.text.strip().split()
    #
    # dados = zip(lista_produto, lista_preco, codigo_produto)
    #
    # for item in dados:
    #     print(item[0],'-----', item[1], item[2])
    #
