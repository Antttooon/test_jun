from django.contrib import admin
from django.contrib.admin import StackedInline
from main.models import Channel, Campaign


# Register your models here.
class CampaignInline(admin.StackedInline):
    model = Campaign



class ChannelAdmin(admin.ModelAdmin):
    inlines = [ CampaignInline, ]
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['name', 'channel', 'bid', 'bid_type']


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Campaign, CampaignAdmin)
