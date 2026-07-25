import os
import osmnx as ox
import json

ARQUIVO = "DB/manaus_drive.graphml"

latitude = -3.1015524
longitude = -60.05476

latitudeDestino, longitudeDestino = -3.1200, -60.0210

cidade = "Manaus, Amazonas, Brazil"

if os.path.exists(ARQUIVO):
    print("Carregando grafo salvo...")
    G = ox.load_graphml(ARQUIVO)
else:
    print("Baixando grafo do OpenStreetMap...")
    G = ox.graph_from_place(
        cidade,
        network_type="drive"
    )

    print("Salvando grafo...")
    ox.save_graphml(G, ARQUIVO)



dados = {
    "origem": [latitude, longitude],
    "destino": [latitudeDestino, longitudeDestino],
    "caminho": []
}




# ==========================
# Encontra o nó mais próximo
# ==========================
no = ox.nearest_nodes(G, longitude, latitude)

print(f"Nó encontrado: {no}")

# ==========================
# Informações do nó
# ==========================
print("\nCoordenadas do nó:")

print(f"Latitude : {G.nodes[no]['y']}")
print(f"Longitude: {G.nodes[no]['x']}")

# ==========================
# Lista os vizinhos
# ==========================
print("\nVizinhos:\n")



dic = {
    "no_Pai": [G.nodes[no]['y'], G.nodes[no]['x']],
    "nos_Filhos": []
}

for vizinho in G.neighbors(no):

    dados_aresta = G.get_edge_data(no, vizinho)

    # Como o MultiDiGraph pode possuir várias ruas
    # entre dois nós, pegamos a primeira.

    atributos = dados_aresta[0]

    comprimento = atributos["length"]

    nome = atributos.get("name", "Rua sem nome")
    
    #dados["caminho"].append([G.nodes[vizinho]['y'], G.nodes[vizinho]['x']])

    print(f"Vizinho: {vizinho}")
    print(f"Rua: {nome}")
    print(f"Comprimento: {comprimento:.2f} metros")
    print(f"Latitude : {G.nodes[vizinho]['y']}")
    print(f"Longitude: {G.nodes[vizinho]['x']}")
    print("-" * 50)

    dic["nos_Filhos"].append([G.nodes[vizinho]['y'], G.nodes[vizinho]['x']])

dados["caminho"].append(dic)

with open("mapas/dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)