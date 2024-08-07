# Generated by Django 5.0.6 on 2024-06-29 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('friendship', '0001_initial'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='friend_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendships_initiated', to='user_profile.userprofile'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='friend_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendships_received', to='user_profile.userprofile'),
        ),
    ]
