from rest_framework import serializers

from api.models import Candidate, Constituency, Party, TallyItem

class TallySerializer(serializers.ModelSerializer):
    class Meta:
        model = TallyItem
        fields = "__all__"

class CandidateSerializer(serializers.ModelSerializer):
    party_name = serializers.ReadOnlyField(source='party.name', read_only=True)
    constituency_name = serializers.ReadOnlyField(source='constituency.name', read_only=True)
    class Meta:
        model = Candidate
        fields = "__all__"
        
class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"
        
class ConstituencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Constituency
        fields = "__all__"        