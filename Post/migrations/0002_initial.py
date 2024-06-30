# Generated by Django 5.0.6 on 2024-06-29 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Post', '0001_initial'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owner_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='user_profile.userprofile'),
        ),
    ]