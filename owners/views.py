import json
from typing import AsyncGenerator
#from django.shortcuts import render
from django.http import JsonResponse
from django.views import View 

from owners.models import Owner, Dog


# class OwnersView(View):
#     def post(self, request):
#         data = json.loads(request.body) 
#         owner = Owner.objects.create(
#             name = data["owner"],
#             email = data["email"],
#             age = data["owner_age"]
            
#         )
#         print(owner)
#         Dog.objects.create(
#             name = data["dog"],
#             age = data["dog_age"],
#             owner = owner
#         )
#         print(Dog.objects.all())  
#         return JsonResponse({"MESSAGE" : "CREATE"}, status = 201)

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body) 
        owner = Owner.objects.create(
            name = data["owner"],
            email = data["email"],
            age = data["owner_age"]
        )
        return JsonResponse({"MESSAGE" : "CREATE"}, status = 201)
 
    def get(self, request):
        results = []
        owners = Owner.objects.all()
        
        for owner in owners:
            dogs = owner.dog_set.all()
            dogs_list = []
            
            for dog in dogs:
                dogs_list.append(
                    {   
                        "dog_name"    : dog.name, 
                        "dog_age"     : dog.age 
                    }
                )

            results.append(
                {
                    "owner"       : owner.name, 
                    "owner_age"   : owner.age,
                    "email"       : owner.email,
                    "dogs_list"   : dogs_list
                }
            )


           
        return JsonResponse({"results" : results}, status = 200)


class DogsView(View):


    def post(self, request):
        data = json.loads(request.body) 
        
        owner = Owner.objects.get(
            name = data["owner_name"]          
        )

        Dog.objects.create(
            name = data["dog"],
            age = data["dog_age"],
            owner = owner
        )
        return JsonResponse({"MESSAGE" : "CREATE"}, status = 201)


    def get(self, request):
        results = []
        dogs = Dog.objects.all()

        for dog in dogs:
            results.append(
                {
                    "dog_name" :  dog.name,
                    "dog_age" : dog.age,
                    "owner" : dog.owner.name

                }
            ) 
        return JsonResponse({"results" : results}, status = 200)
        










# Create your views here.
