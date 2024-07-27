from django.db import models
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    id_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.person.name} - {self.timestamp}'
