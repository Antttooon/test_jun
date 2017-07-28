from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
CPC = 'cpc'
CPM = 'cpm'
CPA = 'cpa'
CPV = 'cpv'
CPI = 'cpi'

BID_TYPES = {
    (CPC, 'CPC'),
    (CPM, 'CPM'),
    (CPA, 'CPA'),
    (CPV, 'CPV'),
    (CPI, 'CPI'),
}


class Channel(models.Model):
    name = models.CharField(verbose_name='Name', max_length=80, blank=False, db_index=True)
    slug = models.SlugField(max_length=80, db_index=True)
    bid_types = models.CharField(max_length=3, choices=BID_TYPES, default=CPC)

    def __str__(self):
        return "{} {}".format(self.name, self.bid_types)

    def get_campaign(self):
        Campaign.objects.filter(channel=self)


class Campaign(models.Model):
    name = models.CharField(max_length=80, verbose_name='Name')
    channel = models.ForeignKey(Channel, verbose_name='Channel', blank=False, default=Channel)
    bid = models.FloatField(verbose_name='Bid')
    bid_type = models.CharField(max_length=3, verbose_name='bid type', choices=BID_TYPES, blank=False, default=CPC)

    def __str__(self):
        return "{} {} {} {}".format(self.name, self.channel, self.bid, self.bid_type)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        channel = self.channel
        print(channel.bid_types)
        print(self.bid_type)
        if channel.bid_types == self.bid_type:
            super(Campaign, self).save()
        else:
            pass

