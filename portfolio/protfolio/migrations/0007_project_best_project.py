# Generated by Django 4.2 on 2024-03-17 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0006_rename_auther_project_collaborators'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='best_project',
            field=models.BooleanField(default=False),
        ),
    ]
