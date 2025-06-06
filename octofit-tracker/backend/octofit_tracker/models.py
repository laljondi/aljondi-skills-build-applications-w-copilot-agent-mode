from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')

class Activity(models.Model):
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    timestamp = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboard')
    score = models.IntegerField(default=0)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    exercises = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
