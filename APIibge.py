import requests
import json

class ListaDeEstados():

  def __init__(self, estado):
    self.estado = estado

  def req_api(self):

    url = f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/'
    resp = requests.get(url + self.estado)
    
    if resp.status_code == 200:
      return resp.json()
    else:
      return resp.status_code

  def imprime_estado(self):
    
    dados_api = self.req_api()
    if type(dados_api) is not int:
      print(dados_api['sigla'] + " - " + dados_api['nome'])
    else:
      print(dados_api)

class ListaDeNomes():

  def __init__(self, nome):
    self.nome = nome

  def req_api(self):

    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/'
    resp = requests.get(url + self.nome)
    
    if resp.status_code == 200:
      return resp.json()
    else:
      return resp.status_code

  def imprime_nomes(self):

    dados_api = self.req_api()
    for i in dados_api:
      for key, value in i.items():
        if key == 'nome':
          print(value)




ibge = ListaDeNomes("marley")
ibge.imprime_nomes()
repo = ListaDeEstados("pe")
repo.imprime_estado()