from rest_framework import serializers

from api.models import Candidates, Vote

class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidates
        fields = "__all__" 