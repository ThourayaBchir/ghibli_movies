from flask import render_template, redirect
import pandas as pd
import numpy as np
import requests
from app import app, cache

API_URL = 'https://ghibliapi.herokuapp.com/'


@app.route('/')
def index():
    return redirect('/movies/')


@app.route('/movies/')
@cache.cached(timeout=60)
def movies():
    films_list = get_from_api(API_URL, 'films')
    peoples_list = get_from_api(API_URL, 'people')
    films_and_peoples_list = merge_films_and_peoples(films_list, peoples_list)

    return render_template('index.html', films_list=films_and_peoples_list)


def get_from_api(url, field: str):
    field_list = requests.get(url + field).json()
    return field_list


def merge_films_and_peoples(films_list, peoples_list):
    df_peoples = pd.DataFrame(peoples_list, columns=['name', 'films'])
    df_peoples = pd.DataFrame({'names': np.repeat(df_peoples.name.values, df_peoples.films.str.len()),
                               'films': np.concatenate(df_peoples.films.values)})
    df_peoples['film_id'] = df_peoples['films'].apply(lambda x: x.split('/')[-1])

    df_films = pd.DataFrame(films_list, columns=['id', 'title'])
    df = pd.merge(df_films, df_peoples, left_on='id', right_on='film_id', how='outer').fillna('').groupby(['title'])\
        .agg({'names': lambda x: list(x)}).reset_index()

    return df.to_dict('records')
