from rest_framework import serializers
from .models import *

##################################################### Скрипт 1 #####################################################
class Script_1_listserializer(serializers.ModelSerializer):
    #Scripts = ProgramLamps1listSerializer(read_only=True, many=True)
    class Meta:
        model = Temp1
        fields = '__all__'

class Script_1_DetailSerializer(serializers.ModelSerializer):
    #status = ProgramLamps1DetailSerializer(many=True)
    class Meta:
        model = Temp1
        fields = '__all__'
##################################################### Скрипт 2 #####################################################
class Script_2_listserializer(serializers.ModelSerializer):
    #Scripts = ProgramLamps1listSerializer(read_only=True, many=True)
    class Meta:
        model = Temp2
        fields = '__all__'

class Script_2_DetailSerializer(serializers.ModelSerializer):
    #status = ProgramLamps1DetailSerializer(many=True)
    class Meta:
        model = Temp2
        fields = '__all__'
##################################################### Скрипт 3 #####################################################
class Script_3_listserializer(serializers.ModelSerializer):
    #Scripts = ProgramLamps1listSerializer(read_only=True, many=True)
    class Meta:
        model = Temp3
        #exclude = ('Script_3s', )
        fields = '__all__'

        #fields = '__all__'

class Script_3_DetailSerializer(serializers.ModelSerializer):
    #status = ProgramLamps1DetailSerializer(many=True)
    class Meta:
        model = Temp3
        fields = '__all__'
#############################################  Родитель Скриптов  ##########################
class Scriptslistserializer(serializers.ModelSerializer):

    Temp1 = Script_1_listserializer(read_only=True, many=True)
    Temp2 = Script_2_listserializer(read_only=True, many=True)
    Temp3 = Script_3_listserializer(read_only=True, many=True)
    #Script_3 = Script_3_listserializer(read_only=True, many=True)
    #Script_2 = Script_2_listserializer(read_only=True, many=True)
    #Script_3 = Script_3_listserializer(read_only=True, many=True)

    class Meta:
        model = Scripts
        fields = '__all__'

class ScriptsDetailSerializer(serializers.ModelSerializer):
    #status = ProgramLamps1DetailSerializer(many=True)
    class Meta:
        model = Scripts
        fields = '__all__'
