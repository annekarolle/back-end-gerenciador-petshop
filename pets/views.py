from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView, Response, Request, status
from .models import Pet
from .serializers import PetSerializer

# Create your views here.

class PetView(APIView):
    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:  
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class PetDetailView(APIView):
    def get(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        serializer = PetSerializer(pet)

        return Response(serializer.data, status.HTTP_200_OK)
    
    def delete(self,request, pet_id:int):
        pet = get_object_or_404(Pet, id=pet_id)

        pet.delete()
        
        return Response(status.HTTP_204_NO_CONTENT)

    def patch(self, request, pet_id: int) -> Response:       
        pet = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(pet, request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)   
    
    
