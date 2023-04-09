from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models import Candidate, Constituency, Party, TallyItem
from api.serializer import CandidateSerializer, ConstituencySerializer, PartySerializer, TallySerializer
from django.db.models import Count
from django.core.serializers import serialize
import json

#Create your views here.
class TallyViewSet(viewsets.ModelViewSet):
    queryset = TallyItem.objects.all()
    serializer_class = TallySerializer
    
    #get votes for candidate
    @action(detail=True, methods=['get'])
    def getVoteCount(self, request):
        candidate_id = request.query_params.get('candidate_id',None)
        constituency_id = request.query_params.get('constituency_id', None)
        if candidate_id == None and constituency_id == None:   #http://localhost:8000/votingAPI/voteCount
            print('1')
            serializer = TallySerializer(self.get_queryset(), many = True)
            return Response(serializer.data)
        elif candidate_id ==  None:  #http://localhost:8000/votingAPI/voteCount?constituency_id=x
            print('2')
            tally = TallyItem.objects.filter(constituency = constituency_id).values('candidate').annotate(count = Count('candidate'))
            print(tally)
            temp = []
            for k in tally:
                temp.append({'candidate': k['candidate'], 'count': k['count']})
            print(temp)
            return Response(temp)
        elif constituency_id == None: #http://localhost:8000/votingAPI/voteCount?candidate_id=x
            print('3')
            tally = TallyItem.objects.filter(candidate = candidate_id).values('constituency').annotate(count = Count('constituency'))
            temp = []
            for k in tally:
                temp.append({'constituency': k['constituency'], 'count': k['count']})
            return Response(temp)
        else:     #http://localhost:8000/votingAPI/voteCount?candidate_id=x&constituency_id=y
            print('4')
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