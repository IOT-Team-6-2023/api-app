from rest_framework import serializers

from api.models import Candidate, Constituency, Party, TallyItem

class TallySerializer(serializers.ModelSerializer):
    class Meta:
        model = TallyItem
        fields = ["candidate","constituency"]

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"
        
class PartySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"
        
class ConstituencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Constituency
        fields = "__all__"        