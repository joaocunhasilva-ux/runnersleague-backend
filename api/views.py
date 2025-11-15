from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Athlete, Race, Result
from .serializers import AthleteSerializer, RaceSerializer, ResultSerializer
from .ranking_engine import ranking_geral

class RankingView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(ranking_geral())

class SubmitResult(generics.CreateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        athlete = getattr(self.request.user, "athlete", None)
        serializer.save(athlete=athlete, is_approved=False)

