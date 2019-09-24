# CartolaBot é um BOT desenvolvido em Python que coleta e imprime traz algumas
# informações de times do game CartolaFC baseado no input do usuário.

# Importando as libs
# Instale bibliteca PIL manualmente (http://www.pythonware.com/products/pil/)
import requests
from PIL import Image
from io import BytesIO

# Definição da url da API e dos Paths para extração dos dados
url_base = 'https://api.cartolafc.globo.com/'

geral = 'times?q='

time = 'time/id/'

nome_time = input('Digite o nome do time: ')

api = requests.get(url_base + geral + nome_time)

# Obtendo os dados da api no formato JSON
tudo = api.json()

# Acessando os dados gerais do time digitado e capturando o ID do time
id_time = str(tudo[0]['time_id'])

# Acessando os dados completos do time através do seu ID e convertendo os dados em JSON
api = requests.get(url_base + time + id_time)

dados = api.json()

# Capturando os dados desejados
pat = dados['patrimonio']

pont = dados['pontos']

rdd = dados['rodada_atual']

dados_time = dados['time']

cartoleiro = dados_time['nome_cartola']

# Obtendo a imagem do escudo do time e redimensionando para 150x150
response = requests.get(dados_time['url_escudo_png'])
escudo = Image.open(BytesIO(response.content))
escudo = escudo.resize((150,150))

# Exibindo os dados
print(f'Time: {nome_time.upper()}')
print(f'Cartoleiro: {cartoleiro}')
print(f'Patrimônio: {pat}')
print(f'Ultima Pontuação: {pont}')
print(f'Ultima Rodada: {rdd}\n')

escudo