# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

# Create your models here.
class Goal(models.Model):
    start = models.DateField(default=datetime.today().date())
    deadline = models.DateField()
    goal = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    user = models.ForeignKey('User')
    
    def __str__(self):
        return self.goal
    
    def as_json(self):
        return dict(
            start = self.start.strftime('%d. %m. %Y'),
            deadline = self.deadline.strftime('%d. %m. %Y'),
            goal = self.goal,
            description = self.description,
            user = self.user.name
        )
    
class User(models.Model):
    name = models.CharField(max_length=254, default='Anona Anonymous')
    email = models.EmailField(max_length=254)
    fbid = models.CharField(max_length=254, default=0)
    
    def __str__(self):
        return self.name
    
    def as_json(self):
        return dict(
            name = self.name,
            email = self.email
        )

class Reminder(models.Model):
    goal = models.ForeignKey('Goal')
    date = models.DateField()
    text = models.TextField()
    
    def __str__(self):
        return self.date.strftime('%d. %m. %Y')


