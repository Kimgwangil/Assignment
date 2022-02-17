from ast import expr_context
import json
from .models import Movie, Actor, ActorMovie
from django.http import JsonResponse
from django.views import View


class ActorView(View):
    def get(self,request):
        actors = Actor.objects.all()
        result = [] 
        for actor in actors: 
            movie_list = []
            movies = actor.movies.all()
            for movie in movies:
                movie_list.append(movie.title)

            actor_information = {
                "first_name"     : actor.first_name,
                "last_name"      : actor.last_name,
                "date_of_birth"  : actor.date_of_birth,
                "movies"    : movie_list
            }
            result.append(actor_information)
        return JsonResponse( {"Actor_information" : result}, status = 200)

    def post(self,request):
        try:
            data = json.loads(request.body)
            Actor.objects.create(
                first_name    = data["first_name"],
                last_name     = data["last_name"],
                date_of_birth = data["date_of_birth"]
            )
            return JsonResponse( {"result" : "Actor Create!👏🏻"}, status = 201)
        except KeyError:
            return JsonResponse( {"result" : "Keyerror 🙀"}, status = 400)



class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        result = []

        for movie in movies:
            actors = movie.actors.all()
            actor_list = []
            for actor in actors:
                actor_list.append(actor.last_name + actor.first_name)

            movie_information = {
                "title"        : movie.title,
                "release_date" : movie.release_date,
                "running_time" : movie.running_time,
                "actor_list"   : actor_list
            }
            result.append(movie_information)
 
        return JsonResponse( {"movie_information" : result}, status = 200)

    def post(self, request):
        try:
            data = json.loads(request.body)
            Movie.objects.create(
                title        = data["title"],
                release_date = data["release_date"],
                running_time = data["running_time"],
            )
            return JsonResponse( {"result" : "Movie Create!👏🏻"}, status = 201)
        except KeyError:
            return JsonResponse( {"result" : "Keyerror 🙀"}, status = 400)

class ActorMovieView(View):
    def post(self,request):
        data = json.loads(request.body)
        if not Actor.objects.filter(id=data['actor_id']).exists():
            return JsonResponse( {"Message" : "Actor Does Not Exist"}, status = 400)
        elif not Movie.objects.filter(id=data['movie_id']).exists():
            return JsonResponse( {"Message" : "Movie Does Not Exist"}, status = 400)

        ActorMovie.objects.create(
            actor_id = data["actor_id"],
            movie_id = data["movie_id"]
        )
        return JsonResponse( {"result" : data }, status = 201)


# class ActorMovieView(View):
#     def post(self,request):
#         try:
#             data = json.loads(request.body)

#             ActorMovie.objects.create(
#                 actor_id = data["actor_id"],
#                 movie_id = data["movie_id"]
#             )
#             return JsonResponse( {"result" : data }, status = 201)
#         except Exception as e:
#             return JsonResponse( {"Message" : "error"}, status = 404)
