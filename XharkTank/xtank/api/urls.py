from django.urls import path
#from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_details
from xtank.api.views import (pitch_list, pitch_detail,counteroffer)



urlpatterns = [
    path('pitches/', pitch_list, name='pitch-list'),
    path('pitches/<int:pk>/', pitch_detail, name='pitch-detail'),
    path('pitches/<int:pk>/makeOffer', counteroffer, name='counteroffer'),

    

]