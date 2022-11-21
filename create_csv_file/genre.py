import requests
import json
import csv

url = requests.get("https://api.themoviedb.org/3//genre/movie/list?api_key=8513510776c862bf8d57bb36d072f05e&language=ko-KR")
text = url.text

# JSON 데이터에 액세스
data = json.loads(text)
data = data['genres']

with open('genrelist.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    for d in data:
        writer.writerow({'id': d['id'], 'name': d['name']})