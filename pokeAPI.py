import requests


def obter_json(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.json()
        else:
            return f"ERRO:{resposta.status_code}"
    except requests.exceptions.RequestException as e:
      return f"Erro na requisição: {e}"
    
pokemonID = int(input('Digite o Id do pokemon que deseja consultar: '))
id = pokemonID 

def consulta():
    url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
    retorno = obter_json(url)
    
    if  isinstance(retorno, dict):
        nome = retorno.get("name", "nome não encontrado")
        tipos = retorno.get("types", [])

        tipos_lista = [tipo["type"]["name"] for tipo in tipos]
        print(f"Nome: {nome}")
        print(f"Tipos: {', '.join(tipos_lista)}")
    
    else:
        print(retorno)

consulta()




'''
def evolucoes(id):
    
    url = f'https://pokeapi.co/api/v2/evolution-chain/{id}/'
    retorno
    dici = retorno.json
def movimentos():
    url = f'https://pokeapi.co/api/v2/evolution-chain/{id}/'
def jogos():
    url = f'https://pokeapi.co/api/v2/generation/{id}/'''