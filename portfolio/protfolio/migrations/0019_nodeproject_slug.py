# Generated by Django 4.2 on 2024-03-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0018_nodeproject_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodeproject',
            name='slug',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
