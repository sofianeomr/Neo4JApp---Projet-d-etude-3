import json

def get_intersections(geojson_file):
  # Chargement du fichier GeoJSON
  with open(geojson_file) as f:
    data = json.load(f)

  # Récupération des points dans le fichier GeoJSON
  points = []
  for feature in data['features']:
    if feature['geometry']['type'] == 'Point':
      points.append(feature['geometry']['coordinates'])

  # Calcul des intersections entre les points
  intersections = []
  for i in range(len(points)):
    for j in range(i+1, len(points)):
      if points[i] == points[j]:
        intersections.append(points[i])
    return intersections
