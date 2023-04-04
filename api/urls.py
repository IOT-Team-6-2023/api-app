from django import urls
from django.urls import include, path
from api.views import CandidatesViewSet, ConstituencyViewSet, PartyViewSet, TallyViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tally', TallyViewSet)
router.register(r'candidates', CandidatesViewSet)
router.register(r'party', PartyViewSet)
router.register(r'constituency', ConstituencyViewSet)

vote_count = TallyViewSet.as_view({'get':'getVoteCount'})

urlpatterns = [
    path(r'voteCount', vote_count),
    path('', include(router.urls)),
]