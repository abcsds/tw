# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import twitter_stream.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SenTweet',
            fields=[
                ('id', twitter_stream.fields.PositiveBigAutoField(serialize=False, primary_key=True)),
                ('tweet_id', models.BigIntegerField()),
                ('text', models.CharField(max_length=250)),
                ('truncated', models.BooleanField(default=False)),
                ('lang', models.CharField(default=None, max_length=9, null=True, blank=True)),
                ('user_id', models.BigIntegerField()),
                ('user_screen_name', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=150)),
                ('user_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(db_index=True)),
                ('user_utc_offset', models.IntegerField(default=None, null=True, blank=True)),
                ('user_time_zone', models.CharField(default=None, max_length=150, null=True, blank=True)),
                ('filter_level', models.CharField(default=None, max_length=6, null=True, blank=True)),
                ('latitude', models.FloatField(default=None, null=True, blank=True)),
                ('longitude', models.FloatField(default=None, null=True, blank=True)),
                ('user_geo_enabled', models.BooleanField(default=False)),
                ('user_location', models.CharField(default=None, max_length=150, null=True, blank=True)),
                ('favorite_count', models.PositiveIntegerField(null=True, blank=True)),
                ('retweet_count', models.PositiveIntegerField(null=True, blank=True)),
                ('user_followers_count', models.PositiveIntegerField(null=True, blank=True)),
                ('user_friends_count', models.PositiveIntegerField(null=True, blank=True)),
                ('in_reply_to_status_id', models.BigIntegerField(default=None, null=True, blank=True)),
                ('retweeted_status_id', models.BigIntegerField(default=None, null=True, blank=True)),
                ('sentiment', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WordScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
