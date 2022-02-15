import json

from django.views import View
from django.http import JsonResponse

import owners
from .models import Owner, Dog

# http://localhost:8000/products Get

class OwnerView(View):
    def get(self, request):
        owners = Owner.objects.all()

        result = []

        for owner in owners:
            dog_list = []
            dogs     = owner.dog_set.all()
            for dog in dogs:
                dog_information = {
                    "name" : dog.name,
                    "age"  : dog.age,
                }
                dog_list.append(dog_information)
            
            owner_information = {
                "id"       : owner.id,
                "name"     : owner.name,
                "email"    : owner.email,
                "age"      : owner.age,
                "dog_list" : dog_list
            }
            result.append(owner_information)

        return JsonResponse( {"result" : result}, status = 200 )

    def post(self, request):
        try:
            data = json.loads(request.body) # json -> python
            Owner.objects.create(
                name  = data["name"], 
                email = data["email"], 
                age   = data["age"]
            )

            return JsonResponse( {"result": "Create!"}, status = 201)
        except KeyError:
            return JsonResponse( {"result": "Keyerror!😢"}, status = 404)

class DogView(View):        
    def get(self,request):
        dogs   = Dog.objects.all()

        result = []

        for dog in dogs:
            s = {
                "id"       : dog.id,
                "name"     : dog.name,
                "age"      : dog.age,
                "owner_id" : dog.owner_id
            }
            result.append(s)
        
        return JsonResponse( {"result" : result}, status = 200 )

    def post(self, request):
        data = json.loads(request.body) # json -> python
        Dog.objects.create(
            name = data["name"],
            age = data["age"], 
            owner_id = Owner.objects.get(id=data['owner_id']).id

        )

        return JsonResponse( {"result": "Create!"}, status = 201)