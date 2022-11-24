import requests
import json
import csv

# 관측소번호, 시작날짜, 종료날짜 입력 필수
# print(data)

# df = pd.json_normalize(data['response']['resultData'])

# csv 저장
# data.to_csv("sample.csv")

with open('movielist.csv', 'w', newline='', encoding='utf-8') as csvfile:
    movie_genre = []
    pk = 0
    fieldnames = ['id', 'title', 'poster_path', 'backdrop_path', 'actors','overview','popularity','vote_average','vote_count','release_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for page in range(1, 51):
        page = str(page)
        url = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key=8513510776c862bf8d57bb36d072f05e&language=ko-KR&page={page}')
        text = url.text

        # JSON 데이터에 액세스
        data = json.loads(text)
        data = data['results']

        for d in data:
            if d['adult'] == False:
                url2 = requests.get(f"https://api.themoviedb.org/3/movie/{d['id']}/credits?api_key=8513510776c862bf8d57bb36d072f05e&language=ko-KR")
                text2 = url2.text
                casts = json.loads(text2)
                casts = casts['cast']
                actors = []
                for gen in d['genre_ids']:
                    pk += 1
                    movie_genre.append([pk, d['id'], gen])
                for cast in casts:
                    actors.append([cast['id'], cast['name'], cast['profile_path']])
                writer.writerow(
                        {
                            'id': d['id'],
                            'title': d['title'],
                            'poster_path': d['poster_path'],
                            'backdrop_path': d['backdrop_path'],
                            'actors':actors, 
                            'overview':d['overview'],
                            'popularity':d['popularity'],
                            'vote_average':d['vote_average'],
                            'vote_count':d['vote_count'],
                            'release_date':d['release_date'],
                        }
                    )


with open('movie_genres.csv', 'w', newline='') as csvfile:
    # fwriter = csv.writer(csvfile, delimiter=',')
    fieldnames = ['id', 'movie_id', 'genre_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for pair in movie_genre:
        writer.writerow({'id':pair[0],'movie_id': pair[1], 'genre_id': pair[2]})