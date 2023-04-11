from neo4j import GraphDatabase
import json

from intersection import get_intersections
from relation import create_relation

print("debug1")
# Connexion à la base de données Neo4j
driver = GraphDatabase.driver("bolt://localhost:7687/test", auth=("neo4j", "sofiane"))
session = driver.session()
print("debug2")

# Chargement des données GeoJSON à partir d'un
#  fichier
with open("C:/Users/33783/Desktop/geojson/inter.geojson") as f:
    data = json.load(f)
print("debug3")

# Boucle sur les caractéristiques dans les données GeoJSON
for feature in data["features"]:
    # Création des noeuds pour les caractéristiques 
    print(feature["properties"]["@id"])
    session.run("CREATE (:Feature {id: $id, name: $name, highway: $highway} )", id=feature["properties"]["@id"], name=feature["properties"]["name"], highway=feature["properties"]["highway"])
    node_names = []
    node_names.append(feature["properties"]["@id"])

intersection = get_intersections(data)
relation_type = "RELATION_TYPE"

# Exemple d'utilisation
for i in range(len(node_names) - 1):
    node1_name = node_names[i]
    node2_name = node_names[i + 1]
    create_relation, node1_name, node2_name, relation_type

session.close()