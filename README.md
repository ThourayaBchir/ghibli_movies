
### Steps to install the app

```

git clone git@github.com:ThourayaBchir/ghibli_movies.git

cd ghibli_movies

python3 -m venv ghibli_venv

source ghibli_venv/bin/activate

pip install -r requirements.txt

```

### To launch the app
Then there is two options to run the app:

1/ 

````
flask run -h localhost -p 8000
````

2/

````
<complete the path here>/ghibli/ghibli_venv/bin/python   <complete the path here>/ghibli/films_app.py
````

### To run tests

````
nosetests
````

### To test pep8 requirements

```
flake8
```

### What can be improved

- We can refactor the method <code>merge_films_and_peoples(films_list, peoples_list)</code> into 2 parts: one for 
cleaning peoples data and another method for merging people and films data.

- we can test more special cases, for example if the api returns inconsistent data: movies and 
peoples doesn't match or for duplicate cases.

- to handle better bad responses from the api

