from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import Candidate, Constituency, Party, TallyItem
from api.serializer import CandidateSerializer, ConstituencySerializer, PartySerializer, TallySerializer

#Create your views here.
class TallyViewSet(viewsets.ModelViewSet):
    queryset = TallyItem.objects.all()
    serializer_class = TallySerializer
    
    #get votes for candidate
    @action(detail=True, methods=['get'])
    def getVoteCount(self, request):
        candidate_id = request.query_params.get('candidate_id')
        constituency_id = request.query_params.get('constituency_id')
        tally = TallyItem.objects.filter(candidate_id = candidate_id).filter(constituency_id=constituency_id)
        count = str(tally.count())
        return Response({'candidate_id': candidate_id, 'vote count': count})
    
class CandidatesViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    
class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    
class ConstituencyViewSet(viewsets.ModelViewSet):
    queryset = Constituency.objects.all()
    serializer_class = ConstituencySerializer