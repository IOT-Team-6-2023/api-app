from django.urls import include, path
from api.views import CandidatesViewSet, VoteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'votes', VoteViewSet)
router.register(r'candidates', CandidatesViewSet)

urlpatterns = [
    path('', include(router.urls))
]