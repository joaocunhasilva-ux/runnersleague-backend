from django.urls import path
from .views import RankingView, SubmitResult

urlpatterns = [
    path("ranking/", RankingView.as_view()),
    path("submeter-resultado/", SubmitResult.as_view()),
]
