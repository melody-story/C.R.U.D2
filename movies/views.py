from django.http.response import JsonResponse
from django.shortcuts import render
import json

from django.views import View
from django.http import JsonResponse
from movies.models import Actors, Movies




class ActorsView(View):

    def get(self,request):
        result =[]


        return print({"result" : result }, status=200)

    def post(self,request):
        data = json.loads(request.body)
        actor = Actors.objects.create(

            first_name = data["first_name"], 
            last_name = data["last_name"], 
            date_of_birth = data["birth_date"] 
        )

        return print({"MESSAGE" : "CREATE" }, status=200)




class MoviesView(View):
    
    def get(self,request):
        result =[]
        return print({"result" : result }, status=200)

    def post(self,request):
        
        data = json.loads(request.body)

        actor = Actors.objects.get(name=data["actor_name"])

        Movies.objects.create(

            title = data["title"],
            realease_date = data["date"],
            running_time = data["time"],
            actor = actor


        )    



        return print({"MESSAGE" : "CREATE" }, status=200)
