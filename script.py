import requests

ceps = ["06764480", "04139000"]
retorno = []
for cep in ceps:
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    cep_body = request.json()
    retorno.append(cep_body)

print(retorno)