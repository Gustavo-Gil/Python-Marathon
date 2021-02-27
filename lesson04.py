import requests

http_list = [200, 201, 202, 204, 300, 301, 307, 308]

def menu():
  escolha = str(input("Verificar mais sites s/n ?")).lower()
  if escolha == "s":
    verificador()
  elif escolha == "n":
    print("Programa encerrado.")
  else:
    print("Opção inválida!")
    menu()

def verificador():
  print("Insira os sites que deseja verificar, separando por vírgulas:")
  urls = str(input()).lower().split(",")
  for url in urls:
    url = url.strip()
    if "." not in url:
      print(url, "Essa url está inváida")
    else:
      if "http" not in url:
        url = f"http://{url}"
      try:
        requisicao = requests.get(url)
        if requisicao.status_code in http_list:
          print(url, "Esse site está online.")
        else:
          print(url, "Esse site está offline.")
      except:
        print(url, "Erro na url")
  menu()

verificador()
