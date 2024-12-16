import requests


def search(movie_name, access_token):
    movie = "%20".join(movie_name.lower().split(' '))
    url = f"https://api.themoviedb.org/3/search/movie?query={movie}&include_adult=true&page=1"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    movies = response.json()['results']
    dic = dict([(i['original_title'], i['id']) for i in movies])
    return dic



def recommendations(movie_id, access_token):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?page=1"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    rec = response.json()['results']
    dic = dict([(i['original_title'], 
                 "https://image.tmdb.org/t/p/original"+i['poster_path']) for i in rec])
    return dic

