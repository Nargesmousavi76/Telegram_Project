import requests
import random

def get_movie_info_by_name(movie_name):
    url = f'https://moviesapi.ir/api/v1/movies'
    params_dict = {
        'q': movie_name
    }

    try :
        response = requests.get(url, params=params_dict)
        if response.status_code != 200:
            return 'ERROR'
        else:
            response = response.json()
            result = response['data']

            unique_movies = []

            titles = []

            for movie in result:

                if movie['title'] not in titles:

                    titles.append(movie['title'])
                    unique_movies.append(movie)


            return unique_movies



            # result = response['data']
            # print("SEARCH RESULTS:", result)

            # return result
        
            # title = result['title']
            # year = result['year']
            # country =  result['country']
            # imdb_rate = result['imdb_rating']
            # return (title, country , year, imdb_rate)

    except :
        return "ERROR"
#################################################################
def get_movie_info_by_id(movie_id):
    url = f'https://moviesapi.ir/api/v1/movies/{movie_id}'

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return 'ERROR'
        else:
            response = response.json()
            title = response['title']
            country = response['country']
            director = response['director']
            year = response['year']
            imdb_rate = response['imdb_rating']
            genres = response.get('genres',[])
            poster = response.get('poster', '')

            return (title, country , director, year, imdb_rate, genres,poster)
    except: 
        return 'ERROR'

##########################################################

def get_movies():

    url = 'https://moviesapi.ir/api/v1/movies'

    try:
        response = requests.get(url)

        if response.status_code != 200:
            return 'ERROR'

        else:
            response = response.json()

            result = response['data']

            return result

    except:
        return 'ERROR'
#############################################################

def get_random_movie():
    movies = get_movies()

    if movies == 'ERROR':
        return 'ERROR'

    else:
        movie = random.choice(movies)

        movie_id = movie['id'] 

        return get_movie_info_by_id(movie_id)    



#if __name__ == '__main__':



