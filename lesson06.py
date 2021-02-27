import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

url_iban = "https://www.iban.com/currency-codes"
r_iban = requests.get(url_iban)

html_iban = r_iban.text

soup = BeautifulSoup(html_iban, 'html.parser')

tabela = soup.find("tbody")
linhas = tabela.find_all("tr")

todos_paises = []

for linha in linhas:
    itens = linha.find_all("td")
    nome = itens[0].text
    moeda_nome = itens[1].text
    moeda_codigo = itens[2].text

    if moeda_nome != "":
        pais = {
            "pais": nome,
            "código": moeda_codigo
        }
        todos_paises.append(pais)


def converter(pais_01, pais_02, amount):
    url_trans_wise = f"https://transferwise.com/gb/currency-converter/{pais_01}-to-{pais_02}-rate?amount={amount}"
    r_trans_wise = requests.get(url_trans_wise)
    if r_trans_wise.status_code != 200:
        print('Combinação não encontrada.')
    else:
        html_trans_wise = r_trans_wise.text
        soup = BeautifulSoup(html_trans_wise, 'html.parser')
        fee = soup.find('span', class_='text-success').string
        result = f'O valor convertido é {format_currency(float(fee) * float(amount), pais_02)}'
        return result


def menu():
    try:
        pais_1 = int(input("Escolha o número do país de origem:"))
        pais_2 = int(input("Escolha o número do país de destino:"))
        valor = float(input("Escolha o valor a ser negociado:"))

        if pais_1 > len(todos_paises):
            print("Número maior do que os existentes!")
            menu()
        elif pais_2 > len(todos_paises):
            print("Número maior do que os existentes!")
            menu()
        else:
            pais_code_01 = todos_paises[pais_1]['código']
            pais_01 = todos_paises[pais_1]['pais']
            print(f"(X){pais_01} com a moeda {pais_code_01}")

            pais_code_02 = todos_paises[pais_2]['código']
            pais_02 = todos_paises[pais_2]['pais']
            print(f"(X){pais_02} com a moeda {pais_code_02}")

            result = converter(pais_code_01, pais_code_02, valor) or 'Não foi possivel calcular.'

            print(result)
    except:
        print("Escolha inválida, escolher um número válido!")
        menu()


for index, pais in enumerate(todos_paises):
    print(f"## {index} - {pais['pais']}")

menu()