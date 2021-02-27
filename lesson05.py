import requests
from bs4 import BeautifulSoup

#url + request
url_iban = "https://www.iban.com/currency-codes"
r_iban = requests.get(url_iban)

#salva o html no html_"nome"
html_iban = r_iban.text

#faz a sopa
soup = BeautifulSoup(html_iban, 'html.parser')

#filtragem de tabela
tabela = soup.find("tbody")
linhas = tabela.find_all("tr")

#lista dos paises
todos_paises = []

#loop em cada linha
for linha in linhas:
  #cria lista de TDs dentro de cada TR
  itens = linha.find_all("td")
  #pega valores
  nome = itens[0].text
  moeda_nome = itens[1].text
  moeda_codigo = itens[2].text
  #verifica se tem moeda universal
  if moeda_nome != "":
    #monta Dict
    pais = {
      "pais": nome,
      "código": moeda_codigo
    }
    #adiciona Dict montada na lista
    todos_paises.append(pais)

def menu():
  #tenta pegar e converter para int
  try:
    escolha = int(input("Escolha o país baseado no número:"))
    #verifica se não é maior que a lista
    if escolha > len(todos_paises):
      print("Número maior do que os existentes!")
      menu()
    else:
      resultado = todos_paises[escolha]
      print(f"O país {resultado['pais']} possui a moeda {resultado['código']}")
  except:
    print("Escolha inválida, escolher um número válido!")
    menu()
#inicia programa
print("BEM VINDO AO IDENTIFICADOR DE MOEDAS INTERNACIONAIS.")
print("ESCOLHA UM PAIS BASEADO NO NÚMERO:")
#print dos paises enumerados
for index, pais in enumerate(todos_paises):
  print(f"## {index} - {pais['pais']}")
#chama o menu
menu()
