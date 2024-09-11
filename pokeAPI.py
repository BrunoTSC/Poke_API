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


if __name__ == "__main__":
    try:
        pokemonID = int(input('Digite o ID do movimento que deseja consultar: '))
        id = pokemonID
    except ValueError:
        print("Por favor, insira um ID válido.")


def consulta():
    url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
    retorno = obter_json(url)
    
    if  isinstance(retorno, dict):
        nome = retorno.get("name", "nome não encontrado")
        tipos = retorno.get("types", [])
        moves = retorno.get("moves", [])
        tipos_lista = [tipo["type"]["name"] for tipo in tipos]
        movimentos = [move['move']['name'] for move in moves]

        print(f"Nome: {nome}")
        print(f"Tipos: {', '.join(tipos_lista)}")
        print(f"Movimentos: {', '.join(movimentos)}")
    
    else:
        print(retorno)

consulta()



'''def evolucoes(id):
    
    url = f'https://pokeapi.co/api/v2/evolution-chain/{id}/'
    retorno
    dici = retorno.json'''

def movimentos():
    url = f'https://pokeapi.co/api/v2/move/{id}/'
    retorno3 = obter_json(url)
    
    if  isinstance(retorno3, dict):
        nome = retorno3.get("name", "nome não encontrado")
        precisao = retorno3.get("accuracy", "não disponível")
        efeito_chance = retorno3.get("effect_chance", "não disponível")
        pp = retorno3.get("pp", "não disponível")
        prioridade = retorno3.get("priority", "não disponível")
        poder = retorno3.get("power", "não disponível")
        
        contest_combos = retorno3.get("contest_combos", {})
        normal = retorno3.get("normal", {})
        use_before = retorno3.get("use_before", [])

        # Exibindo os dados principais
        print(f"ID: {retorno3.get('id', 'não disponível')}")
        print(f"Nome: {nome}")
        print(f"Precisão: {precisao}")
        print(f"Efeito Chance: {efeito_chance}")
        print(f"PP: {pp}")
        print(f"Prioridade: {prioridade}")
        print(f"Poder: {poder}")

        
        print(f"Combos de Concurso: {contest_combos}")#dados dos combos de concurso

        
        print(f"Normal: {normal}") #dados normais

        # Exibindo os movimentos que devem ser usados antes
        if use_before:
            print("Movimentos para usar antes:")
            for item in use_before:
                nome_item = item.get('name', 'não disponível')
                url_item = item.get('url', 'não disponível')
                print(f"- Nome: {nome_item}, URL: {url_item}")
        else:
            print("Não há movimentos para usar antes.")


    else:
        print(retorno3)

movimentos()


'''def jogos():
    url = f'https://pokeapi.co/api/v2/generation/{id}/'''  "modificando"''