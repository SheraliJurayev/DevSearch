# Generated by Django 4.1.7 on 2023-04-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
