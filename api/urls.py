from . import views
from django.urls import path

urlpatterns = [
    path("questions/", views.questions_list.as_view(), name="questions_list"),
    path("questions/<int:pk>/", views.question_detail.as_view(), name="question_detail"),
    path("choices/", views.choice_list.as_view(), name="choice_list"),
]