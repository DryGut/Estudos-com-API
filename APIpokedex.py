import requests
import json

class Pokedex():
  """Agenda Pokemon onde serão buscada
      informações sobre o pokemon """

  def __init__(self, name):
    """ Inicializa a pokedex podendo ser usado tanto
        o nome quanto o id do pokemon """
    
    self.name = name

  def req_api(self):
    """ Requisição da API """

    #constroi a url com o parâmetro que será passado
    url = f'https://pokeapi.co/api/v2/pokemon/'
    resp = requests.get(url + self.name) 
    
    #verifica a resposta da url e retorna o arquivo json da API
    try:
      
      if resp.status_code == 200:
        return resp.json()
      else:
        return resp.status_code
        
    except:
      print("Erro na Conexao") #caso a resposta http seja diferente do code 200 retorna o erro
    
  def buscar_pokemon(self):
    """ Função que fará a busca no 
        arquivo JSON da API """
    
    bichos = {}               #estrutura de dados que será armazenado o pokemon
    tipos = []                #estrutura de dados que identificará seu tipo
    habilidades = []          #estrutura de dados com as habilidades do pokemon
    
    dados_api = self.req_api() #faz a requisição da API
    
    #coleta as habilidades
    for i in dados_api['abilities']:
      for key, value in i.items():
        if key == 'ability':
          habilidades.append(value['name'])
    
    #coleta o tipo
    for i in dados_api['types']:
      for key, value in i.items():
        if key == 'type':
          tipos.append(value['name'])
            
    #cria a estrutura de dados do pokemon que será utilizado
    bichos.update(
      {
        'name': dados_api['name'],
        'tipo': tipos,
        'habilidades': habilidades
      }
    )
    print(bichos)
            

pk = Pokedex('pikachu')
pk.buscar_pokemon()
pk = Pokedex('bulbasaur')
pk.buscar_pokemon()
pk = Pokedex('charmander')
pk.buscar_pokemon()
    