from django.contrib.auth.models import User, Group
from rest_framework import serializers
from imobiliariaSA.models import Imovel, Fotos, Categoria, TipoImovel

# expor usuarios
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# expor grupos
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# expor fotos
class FotosImoveisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos
        fields = ['id', 'descricao', 'foto']

# expor imoveis
class ImoveisSerializer(serializers.ModelSerializer):
    fotos = FotosImoveisSerializer(many=True, read_only=False, required=False)

    class Meta:
        model = Imovel
        fields = ['id', 'nome', 'descricao', 'fotos', 'categoria', 'tipoImovel']

# expor tipo imoveis
class TipoImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoImovel
        fields = ['id', 'nome', 'status']

# expor categorias
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'status']