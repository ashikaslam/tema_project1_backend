# Generated by Django 5.0.6 on 2024-06-30 05:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reaction', '0004_alter_reaction_content_type'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]