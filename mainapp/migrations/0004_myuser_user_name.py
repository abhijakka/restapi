# Generated by Django 4.2.2 on 2023-06-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_name',
            field=models.CharField(help_text='user_name', max_length=255, null=True),
        ),
    ]