from django.test import TestCase, Client

# Create your tests here.
from movie.models import Movie, Actor


class TestMovieViewSet(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(name='Murod', birthdate='2022-11-14', gender='Erkak')
        self.movie = Movie.objects.create(name='Delfin bola', genre='Komik', year='2022-11-14', imdb=1)
        self.movie = Movie.objects.create(name='Bolakay', genre='Komik', year='2022-11-14', imdb=0)
        self.client = Client()

    # def test_get_all_movies(self):
    #     response = self.client.get("/movie/")
    #     data = response.data
    #
    #     self.assertEquals(response.status_code, 200)
    #     self.assertEquals(data[0]['name'], "Delfin bola")

    # def test_search(self):
    #     response = self.client.get("/movie/?search=Komik")
    #     data = response.data
    #     print(data)
    #     self.assertEquals(response.status_code, 200)

    def test_order(self):
        response = self.client.get("/movie/?ordering=imdb")
        data = response.data
        print(data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(data[0]['name'], 'Bolakay')
        self.assertEquals(data[1]['name'], 'Delfin bola')
        self.assertEquals(data[1]['genre'], 'Komik')
