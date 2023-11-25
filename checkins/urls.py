from django.urls import path
from checkins.views import CheckinView


urlpatterns = [
    path('checkins', CheckinView.as_view()),
]