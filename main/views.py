from django.shortcuts import render
from main.models import Campaign, Channel
from main.serializers import ChannelSerializer, CampaignSerializer
from rest_framework import viewsets, mixins, generics
from main.forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


# Create your views here.


def Main(request):
    pass
    # Campaigns = Campaign.objects.all()
    # Channels = Channel.objects.all()
    # return render(request, 'index.html', {'campaigns':Campaigns, 'channels':Channels})


# Channel CRUD operations with CBV
class ChannelListView(ListView):
    model = Channel
    template_name = 'list.html'


class ChannelCreateView(CreateView):
    model = Channel
    template_name = 'create_channel.html'
    success_url = '/chnl'
    fields = ('__all__')
    slug_url_kwarg = 'slug'


class ChannelUpdateView(UpdateView):
    model = Channel
    template_name = 'create_channel.html'
    success_url = '/chnl'
    fields = ('__all__')
    slug_url_kwarg = 'slug'


class ChannelDeleteView(DeleteView):
    model = Channel
    success_url = '/chnl/'
    template_name = 'confirm_delete.html'


class ChannelDetailView(DetailView):
    model = Channel
    success_url = '/chnl/'
    template_name = 'detail.html'

    # def get_queryset(self):
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     qs = Channel.objects.filter(pk=pk)
    #     return qs


#

# Campagn CRUD operations with CBV

class CampaignListView(ListView):
    model = Campaign
    template_name = 'camp_list.html'


class CampaignCreateView(CreateView):
    model = Campaign
    template_name = 'create_camp.html'
    success_url = '/camp/'
    fields = ('__all__')

    # slug_url_kwarg = 'slug'


class CampaignUpdateView(UpdateView):
    model = Campaign
    template_name = 'create_camp.html'
    success_url = '/camp/'
    fields = ('__all__')
    slug_url_kwarg = 'slug'


class CampaignDeleteView(DeleteView):
    model = Campaign
    success_url = '/camp/'
    template_name = 'confirm_delete.html'


class CampaignDetailView(DetailView):
    model = Campaign
    success_url = '/camp/'
    template_name = 'camp_detail.html'


# API REST

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
