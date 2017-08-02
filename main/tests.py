from django.test import TestCase, RequestFactory, Client
from main.models import Channel, Campaign
from main.views import ChannelDetailView
from django.template.response import TemplateResponse


class ChannelViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        Channel.objects.create(name='Канал100', slug='kanal100', bid_types='CPC')
        Channel.objects.create(name='Канал200', slug='kanal200', bid_types='CPM')
        Channel.objects.create(name='Канал300', slug='kanal300', bid_types='CPA')

    def test_channel_view(self):
        qs = Channel.objects.all()
        response = self.client.get('/chnl/', {'context': qs})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Channel.objects.all()), len(qs))

    def test_channel_detail_view(self):

        qs = Channel.objects.filter(pk=100)

        response = self.client.post('/chnl/detail/100',{'context':qs})


        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, '/chnl/detail/100/')


    # def test_channel_create_view(self):
    #     response = self.client.post('chnl/create/')
    #
    #     self.assertEqual(response.status_code, 403)


class ChannelTests(TestCase):
    def test_str(self):
        channel = Channel(name='Канал 50', slug='kanal 50', bid_types='CPC')
        self.assertEqual(
            str(channel),
            'Канал 50'
        )


class CampaignTests(TestCase):
    def test_str(self):
        pk = 1
        channel_instance = Channel.objects.create(pk=pk, name='Канал 50', bid_types='CPC')

        campaign = Campaign(pk=pk, name='Компания 1', channel=channel_instance, bid=32, bid_type='CPC')
        self.assertEquals(
            str(campaign),
            'Компания 1 Канал 50 32 CPC',
        )
