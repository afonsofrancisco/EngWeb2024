import json
import os
import pathlib

def delete_folder(pth):
    for sub in pth.iterdir():
        if sub.is_dir():
            delete_folder(sub)
        else:
            sub.unlink()
    pth.rmdir()

delete_folder(pathlib.Path("Cities"))
os.mkdir("Cities")

file = open("mapa-virtual.json", "r", encoding="utf-8").read()
dicionario = json.loads(file)

city_list = dicionario["cidades"]
links_list = dicionario["ligações"]



cityHtml = """
<!DOCTYPE html>
<html lang="pt PT">
<head>
"""

for city in city_list:
    id = city["id"]
    name = city["nome"]
    population = city["população"]
    description = city["descrição"]
    distrito = city["distrito"]


    cityHtml = cityHtml
    cityHtml += f"""
    <title>Cidade n{id[1:]}</title>
    <meta charset="utf-8">
    </head>

    <body>
    """

    cityHtml += f"<h1>{name}</h1>"
    cityHtml += f"<h3>Número: {id}</h3>"
    cityHtml += "<hr>"
    cityHtml += f"<p><b>Distrito: </b>{distrito}</p>"
    cityHtml += f"<p><b>População: </b>{population}</h3>"
    cityHtml += f"<p><b>Descrição: </b>{description}</h3>"
    cityHtml += "<hr>"
    cityHtml += "<h3>Ligações:</h3>\n<ul>\n"

    for ligacao in links_list:
        if ligacao["origem"] == id:
            idViagem = ligacao["id"]
            destino = ligacao["destino"]
            distancia = ligacao["distância"]
            
            for city in city_list:
                if city["id"] == destino:
                    cityHtml += f"<li><a href = 'http://localhost:2602/{destino}'>{city['nome']}</a></li>"
                    break
                
            
            
            cityHtml += f"<ul>\n<li><b>Distância: </b>{distancia}</li>"
            cityHtml += f"<li><b>Id: </b>{idViagem}</li>\n</ul>"
    cityHtml += "</ul>\n\n\n"
    cityHtml += "<a href = 'http://localhost:2602/'>Voltar ao Menu</a>"
    cityHtml += "</body>"

    with open(f"./Cities/{id}.html", "w", encoding="utf-8") as ficheiroHTML:
        ficheiroHTML.write(cityHtml)