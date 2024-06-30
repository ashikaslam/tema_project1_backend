# Generated by Django 5.0.6 on 2024-06-29 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reaction', '0002_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_reactions', to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='owner_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reactions', to='user_profile.userprofile'),
        ),
    ]