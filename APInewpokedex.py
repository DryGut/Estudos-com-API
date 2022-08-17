import requests
import json

"""
    Utilizando a API POKEDEX para criação de um arquivo JSON
    com dados sobre os pokemons
     
     dados a serem coletados:
          id = identificação do pokemon na API
          name = nome do pokemon
          types = o tipo do pokemon
          ability = habilidades que o pokemon possui
          stats = atributos do pokemon 
"""

def req_api():
  """ 
  Requisição da API 
  e estruturação dos Dados coletados 
  """
    
  total_pokemon = 151  #numero de pokemon que será salvo no arquivo
  bichos = [] 
  
  #constroi a url com o parâmetro que será passado
  url = 'https://pokeapi.co/api/v2/pokemon/'
     
    
  #verifica a resposta da url e retorna o arquivo json da API
  try:
    for i in range(total_pokemon): #laço dos pokemons que serão utilizados
      resp = requests.get(f'{url}{i+1}')
      if resp.status_code == 200:
        conteudo = resp.json()
       
        #estrutura de dados que será salvo no arquivo JSON
        a_bichos = {
          'id': conteudo['id'],
          'name': conteudo['name'],
          'types': [],
          'ability': [],
          'stats': []
        }
        #laços que farão a coleta dos dados a serem salvos
        for type in conteudo['types']:
          a_bichos['types'].append(type['type']['name'])
        for skill in conteudo['abilities']:
          a_bichos['ability'].append(skill['ability']['name'])
        for stats in conteudo['stats']:
          a_bichos['stats'].append({stats['stat']['name']: stats['base_stat']})
        
        bichos.append(a_bichos)
      else:
        return resp.status_code
        
  except:
    print("Erro na Conexao") #caso a resposta http seja diferente do code 200 retorna o erro
  
  return bichos

#função para salvar a estrutura de dados em arquivo JSON
def write_to_json(pokemon_lista):
  with open('listapokemon.json', 'w') as arq:
    json.dump(pokemon_lista, arq, indent=4, ensure_ascii=False)
    arq.close()

def main():
  pokemon = req_api()
  write_to_json(pokemon)

if __name__ == '__main__':
  main()