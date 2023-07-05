from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self) -> str:
        return self.name