"""
From 30 Days of Python tutorial, made by Coding Entrepreneurs.

Day 13 - Using a REST API Service

To run this code, you need an API Key from https://www.themoviedb.org
More info in https://developers.themoviedb.org

And install the next packages:

(python)$ pip install requests

Use of a Rest API service
"""
import os
import sys
import settings
import requests
# Better formating in printing a json structure
import pprint

# Movie DB api key
api_key = os.getenv('MOVIE_DB_API_KEY')
# Movie DB access token
access_token = os.getenv('MOVIE_DB_ACCESS_TOKEN')

# API base url
api_base_url = "https://api.themoviedb.org/{api_version}"

def get_query(endpoint_path, api_version, element_id=None, search_by=None):
    """
    Make a request to endpoint_path using a kwarg if needed

    @param endpoint_path string Is the endpoint path
    @param element_id integer Is the id of an element to get
    """
    extra_parameter = f"/{element_id}" if element_id else ''
    search_parameter = f"&query={search_by}" if search_by else ''
    headers = ''
    if api_version == '3':
        endpoint = f"{api_base_url}{endpoint_path}{extra_parameter}?api_key={api_key}{search_parameter}".format(api_version=api_version)
    elif api_version == '4':
        endpoint = f"{api_base_url}{endpoint_path}{extra_parameter}?{search_parameter}".format(api_version=api_version)
        headers = {
            'Authorization': f"Bearer {access_token}",
            'Content-Type': 'application/json;charset=utf-8'
        }
    else:
        return f"Write a valid version"
    print(f"Making a request to {endpoint}")
    r = requests.get(endpoint, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        # Encode the response tex to dict
        response = r.json()
        if response.get('status_message'):
            return response['status_message']
        else:
            return f"Error to make the request, {r.status_code}: {r.text}"

def get_key_name(data_movies, key_name):
    """
    Returns the detail specified by key_name

    @param data_movies Is the result of make a query to moviedb API
    @param key_name Is the detail that are looking for
    """
    if type(data_movies) != dict:
        return f"Data movies is not valid"
    if not key_name:
        return f"Data type is not valid"
    # Get the list of results in data_movies
    results = data_movies['results']
    result_set = set()
    for movie in results:
        result_set.add(movie[key_name])
    return result_set

if __name__ == "__main__":
    """
    Call methods that make request to themoviedb Rest API Service

    @param sys.argv[1] End point to request
    @param sys.argv[2] Id of element to search
    """
    try:
        endpoint_path = sys.argv[1]
        api_version = sys.argv[2]
    except:
        print("You must write a valid endpoint path and the api version to use.")
        print("List of possible pair of values, using the version 3 of the api:")
        print("Get all details of the 500 id movie: /movie/500 3")
        print("Search a movie by name: /search/movie 3 MovieName")
    search_by = ''
    try:
        # Fail if third argument is not an integer
        element_id = int(sys.argv[3])
    except:
        element_id = None
        if (len(sys.argv) > 3):
            search_by = sys.argv[3]

    if len(sys.argv) > 2:
        # Get a new guest id
        # endpoint = f"/authentication/guest_session/new"
        # response = get_query(endpoint_path=endpoint, api_version="3")
        # print(response)
        # if response.success:
        # session_id = response.guest_session_id
        response = get_query(endpoint_path=endpoint_path, api_version=api_version, 
            element_id=element_id, search_by=search_by)
        if type(response) == str:
            print(response)
        else:
            # Print the json in a good looking way
            pprint.pprint(response)
            # Return the ids of movies in response
            movies_item = get_key_name(response, 'id')
            print("Movies ids: ", movies_item)
            # Return the title of movies in response
            movies_item = get_key_name(response, 'original_title')
            print("Movies title: ", movies_item)