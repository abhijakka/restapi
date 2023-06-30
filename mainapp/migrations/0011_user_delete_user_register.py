# Generated by Django 4.2.2 on 2023-06-28 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_user_register_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Name')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='user_Register',
        ),
    ]
