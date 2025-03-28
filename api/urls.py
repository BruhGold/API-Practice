from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path("questions/", views.questions_list.as_view(), name="questions_list"),
    path("questions/<int:pk>/", views.question_detail.as_view(), name="question_detail"),
    path("choices/", views.choice_list.as_view(), name="choice_list"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]