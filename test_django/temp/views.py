from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import*
# Create your views here.

######################################################### Scripts View #######################################################
class ScriptsCreateView(generics.CreateAPIView):
    serializer_class = ScriptsDetailSerializer
class ScriptsListView(generics.ListAPIView):
    serializer_class = Scriptslistserializer
    queryset = Scripts.objects.all()

class ScriptsDtailView(generics.RetrieveUpdateDestroyAPIView):   #############
    serializer_class = Scriptslistserializer
    queryset = Scripts.objects.all()

#################################################################### Script 1 View ############################################
class Script_1CreateView(generics.CreateAPIView):
    serializer_class = Script_1_DetailSerializer
class Script_1ListView(generics.ListAPIView):
    serializer_class = Script_1_listserializer
    queryset = Temp1.objects.all()

class Script_1DtailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Script_1_listserializer
    queryset = Temp1.objects.all()
#################################################################### Script 2 View ############################################
class Script_2CreateView(generics.CreateAPIView):
    serializer_class = Script_2_DetailSerializer
class Script_2ListView(generics.ListAPIView):
    serializer_class = Script_2_listserializer
    queryset = Temp2.objects.all()

class Script_2DtailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Script_2_listserializer
    queryset = Temp2.objects.all()
###################################################################### Script 3 View ##########################################
class Script_3CreateView(generics.CreateAPIView):
    serializer_class = Script_3_DetailSerializer
class Script_3ListView(generics.ListAPIView):
    serializer_class = Script_3_listserializer
    queryset = Temp3.objects.all()

class Script_3DtailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Script_3_listserializer
    queryset = Temp3.objects.all()


