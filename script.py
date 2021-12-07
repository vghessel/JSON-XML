import requests
import xml.etree.cElementTree as ET

ceps = ["06764480", "04139000"]
retorno = []
for cep in ceps:
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    cep_body = request.json()
    retorno.append(cep_body)

root = ET.Element("root")

for data in retorno:
    info = ET.SubElement(root, "cep")
    ET.SubElement(info, "cep").text = data["cep"]
    ET.SubElement(info, "logradouro").text = data["logradouro"]
    ET.SubElement(info, "complemento").text = data["complemento"]
    ET.SubElement(info, "bairro").text = data["bairro"]
    ET.SubElement(info, "localidade").text = data["localidade"]
    ET.SubElement(info, "uf").text = data["uf"]
    ET.SubElement(info, "ibge").text = data["ibge"]
    ET.SubElement(info, "gia").text = data["gia"]
    ET.SubElement(info, "ddd").text = data["ddd"]
    ET.SubElement(info, "siafi").text = data["siafi"]


tree = ET.ElementTree(root)
tree.write("CEP.xml")