from imobiliariaSA.serializers import UserSerializer, GroupSerializer, ImoveisSerializer, TipoImovelSerializer, CategoriaSerializer
from imobiliariaSA.models import Imovel, TipoImovel, Categoria

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token






@csrf_exempt
def login(request):
    body_unicode = request.body.decode('utf-8')
    # print("unicode" + " " + body_unicode)
    body = json.loads(body_unicode)
    # print("body" + " " + body.get('username'))
    # print("body" + " " + body.get('password'))

    if body['username']:
        user = authenticate(username=body['username'], password=body['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            response_data = {
                'token': token.key,
                'id': user.id,
                'usuario': user.username,
                'email': user.email,
                'nome': user.first_name
            }
            return JsonResponse(response_data)


# @csrf_exempt
# def login(request):
#     print(request)
#     body_unicode = request.body.decode('utf-8')
#     print("unicode" + " " + body_unicode)
#     body = json.loads(body_unicode)
#     print("body" + " " + body)

#     username = body.get('username')
#     password = body.get('password')
#     print("nome" + username)
#     print("senha" + password)

#     if username and password:
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             token, created = Token.objects.get_or_create(user=user)
#             response_data = {
#                 'token': token.key,
#                 'id': user.id,
#                 'usuario': user.username,
#                 'email': user.email,
#                 'nome': user.first_name
#             }
#             return JsonResponse(response_data)
#         else:
#             return HttpResponse('Invalid login credentials.')
#     else:
#         return HttpResponse('Username and password are required.')
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class ImoveisViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImoveisSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class ImoveisViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImoveisSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class TipoImovelViewSet(viewsets.ModelViewSet):
    queryset = TipoImovel.objects.all()
    serializer_class = TipoImovelSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
