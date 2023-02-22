from django.contrib.auth.models import User, Group
from rest_framework import serializers
from imobiliariaSA.models import Imovel, Fotos

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class FotosImoveisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
        fields = ['id', 'descricao', 'foto']

class ImoveisSerializer(serializers.ModelSerializer):
    fotos = FotosImoveisSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Imovel
        fields = ['nome', 'descricao', 'categoria', 'fotos']