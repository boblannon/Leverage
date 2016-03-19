from django.shortcuts import render
from django.contrib.auth.models import User, Group
from app.models import CampaignFinance
from rest_framework import viewsets
from app.serializers import UserSerializer, GroupSerializer, CampaignFinanceSerializer


def index(request):
    return render(request, 'app/index.html')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CampaignFinanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows campaign finance data to be viewed.
    """
    queryset = CampaignFinance.objects.all()
    serializer_class = CampaignFinanceSerializer