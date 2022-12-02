import json
from operator import getitem
from rest_framework import serializers

from groups.serializers import GroupSerializer
from pets.models import Pet, Sex
from groups.models import Group
from traits.models import Trait
from traits.serializers import TraitSerializer

class PetSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=Sex.choices,
        default=Sex.DEFAULT,
    )
    group = GroupSerializer()
    traits = TraitSerializer(many=True)
    traits_count = serializers.SerializerMethodField(read_only=True, method_name='traits_count_get')  

    def traits_count_get(self, pet):
        return pet.traits.count()    
    
    def create(self, validated_data: dict) -> Pet:            
        group_data = validated_data.pop("group")     
        trait_data = validated_data.pop("traits")        

        grupo, created = Group.objects.get_or_create(**group_data) 
        print("O grupo {} foi {} com sucesso".format(grupo.scientific_name, 'criado' if created else 'resgatado'))
        pet = Pet.objects.create(**validated_data, group=grupo)         
                
        

        for trait in trait_data:
            traits, created = Trait.objects.get_or_create(**trait)                         
            pet.traits.add(traits)            
        
        pet.save()

        return pet

    def update(self, instance: Pet, validated_data: dict):
        group_data = validated_data.pop("group", None)     
        trait_data = validated_data.pop("traits", None) 

        if group_data is not None:
            grupo, created = Group.objects.get_or_create(**group_data) 
            instance.group = grupo

        if trait_data is not None:
            instance.traits.clear()
            for trait in trait_data:
                traits, created = Trait.objects.get_or_create(**trait)          
                instance.traits.add(traits)

        for key, value in validated_data.items():          
            setattr(instance, key, value)
           
        instance.save()

        return instance

    