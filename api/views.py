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
            candidates = Candidate.objects.all()
            votes = TallyItem.objects.all()
            print(candidates)
            print(votes)
            temp = []
            for c in candidates:
                if votes.filter(candidate = c.candidate_id).exists() == False:
                    k=0
                else:
                    k = votes.filter(candidate = c.candidate_id).count()
                temp.append({'candidate_id': c.candidate_id, 'candidate_name': c.__str__(), 'count': str(k)})
            print(temp)
            return Response(temp)
        
        # elif candidate_id ==  None:  #http://localhost:8000/votingAPI/voteCount?constituency_id=x
        #     print('2')
        #     print(temp)
        #     return Response(temp)
        
        elif constituency_id == None: #http://localhost:8000/votingAPI/voteCount?candidate_id=x
            count= 0
            if Candidate.objects.filter(candidate_id = candidate_id).exists() == False:
                return Response({'Error': 'Candidate doesn\'t exist'})
            c = Candidate.objects.get(candidate_id = candidate_id)
            print(c)
            if TallyItem.objects.filter(candidate = candidate_id).exists():
                count = TallyItem.objects.filter(candidate = candidate_id).count()
                result = {'candidate_id': candidate_id, 'candidate': c.__str__(),'count': str(count)}
            else:
                result = {'candidate': candidate_id, 'count': '0'}
            return Response(result)
        
        else:
            return Response({'Error': 'Invalid Request'})
    
class CandidatesViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        firstName = request.data.get('firstName')
        middleName = request.data.get('middleName')
        lastName = request.data.get('lastName')
        print(firstName, middleName, lastName)
        if self.queryset.filter(firstName = firstName).filter(middleName = middleName).filter(lastName = lastName).exists():
            return Response({'Error':'Candidate already exists'})
        
        return super().create(request, *args, **kwargs)
    
class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        name = request.data.get('name')
        print(name)
        if self.queryset.filter(name = name).exists():
            return Response({'Error':'Party already exists'})
        
        return super().create(request, *args, **kwargs)
    
class ConstituencyViewSet(viewsets.ModelViewSet):
    queryset = Constituency.objects.all()
    serializer_class = ConstituencySerializer
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        name = request.data.get('name')
        print(name)
        if self.queryset.filter(name = name).exists():
            return Response({'Error':'Constituency already exists'})
        
        return super().create(request, *args, **kwargs)