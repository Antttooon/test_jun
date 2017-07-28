from django import forms
from .models import Channel, Campaign

class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = ('__all__')

class CampaignForm(forms.Form):
    # name = models.CharField(max_length=80, verbose_name='Name')
    # channel = models.ForeignKey(Channel, verbose_name='Channel', blank=False, default=Channel)
    # bid = models.FloatField(verbose_name='Bid')
    # bid_type = models.CharField(max_length=3, verbose_name='bid t
    name = forms.CharField(max_length=80)
    channel = forms.ModelChoiceField(queryset=Channel.objects.all())



