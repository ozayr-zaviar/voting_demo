import datetime
from unicodedata import name
from django.db import models

# Create your models here.
class Voter(models.Model):
  name = models.CharField(max_length=32)
  voter_id = models.IntegerField(default=0)

class Candidate(models.Model):
  name = models.CharField(max_length=32)
  party = models.CharField(max_length=32)

class Vote(models.Model):
  voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
  candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
  time = models.DateTimeField(default=datetime.datetime.now)