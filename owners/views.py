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
        result = []
        owners = Owner.objects.all()

        print(owners)

        #for owner in owners:
            
        return JsonResponse({"MESSAGE" : "CREATE"}, status = 201)


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


    # def get(self, request):
    #     result =[]
        



        return JsonResponse({"MESSAGE" : "CREATE"}, status = 201)






# Create your views here.
