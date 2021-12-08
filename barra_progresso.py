from tqdm import tqdm
import time
import requests

# # PEGAR OS DADOS DESSE CEP
# link = 'https://cep.awesomeapi.com.br/json/51020000'
#
# requisicao = requests.get(link)
# print(requisicao.json())



# quero entregar pra cidade do Recife
import requests


# passo 1: pegar a lista de ceps
with open("ceps.txt", "r") as arquivo:
    ceps = arquivo.read()
ceps = ceps.split("\n")
# passo 2: pegar as informações de cada cep
enderecos_entrega = []
for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/{cep}'
    # passo 3: verificar se a cidade é Recife
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']
    # passo 4: printar o cep e o bairro
    if cidade == "Recife":
        enderecos_entrega.append((cep, bairro))
print(enderecos_entrega)

