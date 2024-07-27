from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    id_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
