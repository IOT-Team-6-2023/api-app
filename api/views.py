from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import Candidates, Vote
from api.serializer import CandidateSerializer, VoteSerializer

# Create your views here.
class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    
    
class CandidatesViewSet(viewsets.ModelViewSet):
    queryset = Candidates.objects.all()
    serializer_class = CandidateSerializer
    
    #get votes for candidate
    @action(detail=True, methods=['get'])
    def gwtVoteCount(self, request, pk=None):
        votes = Vote.objects.filter(candidate_id = pk)
        count = str(votes.count())
        return Response({'candidate_id': pk, 'vote count': count}) 
    
