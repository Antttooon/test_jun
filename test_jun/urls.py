"""test_jun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from main.views import Main

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from main import views
from main.views import *

router = routers.DefaultRouter()
router.register(r'channels',views.ChannelViewSet)
router.register(r'campaign',views.CampaignViewSet)
router.register(r'campaign/(\d+)/$',views.CampaignViewSet)




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Channel CBV urls http://127.0.0.1:8000/chnl/

    url(r'^chnl/$', ChannelListView.as_view()),
    url(r'^chnl/detail/(?P<pk>\d+)/$', ChannelDetailView.as_view(),name='channel_detail'),
    url(r'^chnl/delete/(?P<pk>\d+)/$', ChannelDeleteView.as_view(),name='channel_delete'),
    url(r'^chnl/update/(?P<pk>\d+)/$', ChannelUpdateView.as_view(),name='channel_update'),
    url(r'^chnl/create/$', ChannelCreateView.as_view(),name='chanel_create'),

    # Campaign CBV urls http://127.0.0.1:8000/camp/

    url(r'^camp/$', CampaignListView.as_view()),
    url(r'^camp/detail/(?P<pk>\d+)/$', CampaignDetailView.as_view(),name='camp_detail'),
    url(r'^camp/delete/(?P<pk>\d+)/$', CampaignDeleteView.as_view(),name='camp_delete'),
    url(r'^camp/update/(?P<pk>\d+)/$', CampaignUpdateView.as_view(),name='camp_update'),
    url(r'^camp/create/$', CampaignCreateView.as_view(),name='camp_create'),




]