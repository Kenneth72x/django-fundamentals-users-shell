from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def _str_(self):
    return f"First Name: {self.first_name} , Last Name: {self.last_name} , Age: {self.age}"
