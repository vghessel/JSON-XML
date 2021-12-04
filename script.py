import requests
import xml.etree.cElementTree as ET

ceps = ["06764480", "04139000"]
retorno = []
for cep in ceps:
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    cep_body = request.json()
    retorno.append(cep_body)


for data in retorno:
    root = ET.Element("root")

    ET.SubElement(root, "cep").text = data["cep"]
    ET.SubElement(root, "logradouro").text = data["logradouro"]
    ET.SubElement(root, "complemento").text = data["complemento"]
    ET.SubElement(root, "bairro").text = data["bairro"]
    ET.SubElement(root, "localidade").text = data["localidade"]
    ET.SubElement(root, "uf").text = data["uf"]
    ET.SubElement(root, "ibge").text = data["ibge"]
    ET.SubElement(root, "gia").text = data["gia"]
    ET.SubElement(root, "ddd").text = data["ddd"]
    ET.SubElement(root, "siafi").text = data["siafi"]

tree = ET.ElementTree(root)
tree.write("CEP.xml")