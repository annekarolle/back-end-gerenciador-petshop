from django.db import models
from pets.models import Pet


# Create your models here.
class Trait(models.Model):
    name = models.CharField(max_length=20, unique=True)  
    created_at = models.DateTimeField(auto_now_add=True)    
 

    def __repr__(self) -> str:
        return f"[{self.id} - {self.name}]"