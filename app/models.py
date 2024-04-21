from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    cource = models .CharField(max_length=100)
    id_number = models.IntegerField()
    

    def __str__(self) -> str:
        return self.name