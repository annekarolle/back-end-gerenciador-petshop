from django.db import models

# Create your models here.


class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f"[{self.id}] - {self.scientific_name}"
