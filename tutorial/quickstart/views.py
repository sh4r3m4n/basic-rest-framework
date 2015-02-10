from django.contrib.auth.models import User, Group
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(methods=['GET'], url_path='show/encrypted_password')
    def display_password(self, request, pk):
        obj = self.get_object()
        return Response(obj.password)

    @list_route(methods=['GET'], url_path="show_12345")
    def test_list(self, request):
        return Response(12345)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
