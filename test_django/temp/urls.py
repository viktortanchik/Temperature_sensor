from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'temp'
urlpatterns = [

######################################################### Scripts ######################################################
    path('Scripts/create/', ScriptsCreateView.as_view()),
    path('Scripts/detail/<int:pk>/', ScriptsDtailView.as_view()),
    path('Scripts/all', ScriptsListView.as_view()),
################################################################ Script 1  #############################################
    path('Script_1/create/', Script_1CreateView.as_view()),
    path('Script_1/detail/<int:pk>/', Script_1DtailView.as_view()),
    path('Script_1/all', Script_1ListView.as_view()),
######################################################### Script 2  ########################
    path('Script_2/create/', Script_2CreateView.as_view()),
    path('Script_2/detail/<int:pk>/', Script_2DtailView.as_view()),
    path('Script_2/all', Script_2ListView.as_view()),
######################################################### Script 3 ########################
    path('Script_3/create/', Script_3CreateView.as_view()),
    path('Script_3/detail/<int:pk>/', Script_3DtailView.as_view()),
    path('Script_3/all', Script_3ListView.as_view()),

    #########################################
]