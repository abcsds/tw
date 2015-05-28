from django.contrib import admin
from .models import SenTweet, WordScore

class SenTweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tweet',            {'fields': ['user_screen_name', 'text', 'lang']}),
        ('Date information', {'fields': [   'tweet_id',
                                            'truncated',
                                            'user_id',
                                            'user_name',
                                            'user_verified',
                                            'created_at',
                                            'user_utc_offset',
                                            'user_time_zone',
                                            'filter_level',
                                            'latitude',
                                            'longitude',
                                            'user_geo_enabled',
                                            'user_location',
                                            'favorite_count',
                                            'retweet_count',
                                            'user_followers_count',
                                            'user_friends_count',
                                            'in_reply_to_status_id',
                                            'retweeted_status_id',
                                            'sentiment'
                                        ],

                                        'classes': ['collapse']
                            }),
    ]
    list_display = ('user_screen_name', 'created_at', 'lang')
    list_filter = ['lang']
    search_fields = ['user_screen_name']
class WordScoreAdmin(admin.ModelAdmin):
    fields = ['word', 'score']

    list_display = ('word', 'score')
    search_fields = ['word']

admin.site.register(SenTweet, SenTweetAdmin)
admin.site.register(WordScore, WordScoreAdmin)
