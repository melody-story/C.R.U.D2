import movies
from django.http.response import JsonResponse
from django.shortcuts import render
import json

from django.views import View
from django.http import JsonResponse
from movies.models import Actors, Movies




class ActorsView(View):

    # 배우의 이름, 성, 그리고 출연한 영화 제목 목록
    def get(self,request):
        actors = Actors.objects.all()
        result =[]

        for actor in actors:
            movies_list = []
    
            actor_movies = actor.Movies.all()


            for movie in actor_movies:
            
                movies_list.append(
                    {
                        "movie_name": movie.title
                    }
                )
            
            result.append(
                {
                    "Actor_first_name" : actor.first_name,
                    "Actor_last_name"  : actor.last_name, 
                    "movies_list"      : movies_list
                }
            )


        return JsonResponse({"result" : result }, status=200)

    def post(self,request):
        data = json.loads(request.body)
        actor = Actors.objects.create(

            first_name = data["first_name"], 
            last_name = data["last_name"], 
            date_of_birth = data["birth_date"] 
        )
        return JsonResponse({"MESSAGE" : "CREATE" }, status=200)




class MoviesView(View):
    
    # 영화의 제목, 상영시간, 출연한 배우 목록 (이름만)
    def get(self,request):

        result =[]

        movies = Movies.objects.all()

        
        for movie in movies:
            
            Actor_list =[]
    
            #actors = movie.prefetch_related('actors_set').all()
            actors = movie.actors_set.all()
    
            for actor in actors:
    
                Actor_list.append(
                    {
                        "actor_name" : actor.first_name
                    }
                )

            result.append(
                {
                    "Movie_title" : movie.title,
                    "Movie_time"  : movie.running_time,
                    "Actors"       : Actor_list
                }
            )

        return JsonResponse({ "result" : result }, status=200)

    def post(self,request):
        
        data = json.loads(request.body)

        Movies.objects.create(

            title        = data["title"],
            release_date = data["date"],
            running_time = data["time"]
            
        )    
        return JsonResponse({"MESSAGE" : "CREATE" }, status=200)

