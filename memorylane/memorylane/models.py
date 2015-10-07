from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    friends = models.CharField(max_length=5000)
    propic = models.CharField(max_length=1000)
    date_created = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    bio = models.TextField()
    memories = models.CharField(max_length=5000)

    def __str__(self):
    	return self.first_name + " " + self.last_name

class Memory(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    description = models.TextField()
    author = models.IntegerField()
    date_created = models.DateField()

    def __str__(self):
    	return self.name