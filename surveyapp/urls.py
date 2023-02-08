from django.urls import path
from . import views

urlpatterns = [
    path("", views.TestIndex.as_view(), name="test"),
    path("correspondent/register", views.SurveyCorrespondentView.as_view(), name="correspondent_register"),
    path("correspondent/data/dump", views.SurveyFromsView.as_view(), name="datadump"),

]
