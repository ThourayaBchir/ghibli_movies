import unittest
from app import app, cache
from app.routes import get_from_api, merge_films_and_peoples


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.app_client = app.test_client()
        self.api_url = 'https://ghibliapi.herokuapp.com/'

    def tearDown(self):
        cache.clear()

    def test_server_response(self):
        self.r = self.app_client.get('/movies/')
        self.assertEqual(self.r.status_code, 200)

    def test_get_from_api(self):
        # for movies
        self.films_list = get_from_api(self.api_url, 'films')
        self.assertGreater(len(self.films_list), 0)
        self.assertTrue(all(['id' in film.keys() for film in self.films_list]))
        self.assertTrue(all(['title' in film.keys() for film in self.films_list]))

        # for peoples
        self.peoples_list = get_from_api(self.api_url, 'people')
        self.assertGreater(len(self.peoples_list), 0)
        self.assertTrue(all(['name' in people.keys() for people in self.peoples_list]))
        self.assertTrue(all(['films' in people.keys() for people in self.peoples_list]))

    def test_merge_films_and_peoples(self):
        self.peoples_list = [
            {'name': 'Pazu', 'films': ['https://app.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe']},
            {'name': "Renaldo Moon aka Moon aka Muta",
             'films': ["https://app.com/films/90b72513-afd4-4570-84de-a56c312fdf81",
                       "https://app.com/films/ff24da26-a969-4f0e-ba1e-a122ead6c6e3"]}]

        self.films_list = [{'url': 'https://app.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe', 'title': 'Castle in the Sky'},
                           {'url': 'https://app.com/films/90b72513-afd4-4570-84de-a56c312fdf81', 'title': 'The Cat Returns'},
                           {'url': 'https://app.com/films/ff24da26-a969-4f0e-ba1e-a122ead6c6e3', 'title': 'Whisper of the Heart'}]

        self.expected_result = [{'title': 'Castle in the Sky', 'names': ['Pazu']},
                                {'title': 'The Cat Returns', 'names': ['Renaldo Moon aka Moon aka Muta']},
                                {'title': 'Whisper of the Heart', 'names': ['Renaldo Moon aka Moon aka Muta']}]

        self.list_films_and_people = merge_films_and_peoples(self.films_list, self.peoples_list)

        self.assertListEqual(self.list_films_and_people, self.expected_result)


if __name__ == '__main__':
    unittest.main()
