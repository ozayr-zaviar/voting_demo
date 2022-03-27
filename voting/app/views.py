from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Candidate, Voter, Vote
from django.shortcuts import render

# Create your views here.
def index(request):
  candidates = Candidate.objects.all()
  return render(request, 'index.html', {'candidates': candidates})

def vote(request, candidate_id):
  voter = Voter.objects.create(name='abc', voter_id='1')
  Vote.objects.create(voter_id=voter.id, candidate_id=candidate_id)

  return index(request)

def result(request):
  candidates = Candidate.objects.all()
  all_votes = {}

  for candidate in candidates:
    votes = Vote.objects.filter(candidate_id=candidate.id)
    all_votes[candidate.id] = {
      'name': candidate.name,
      'votes': len(votes)
    }

  return render(request, 'results.html', {'candidates': all_votes})
    