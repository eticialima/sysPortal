# Generated by Django 3.2.9 on 2021-12-26 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('YOUTUBE', 'youtube'), ('WHATSAPP', 'whatsapp'), ('FACEBOOK', 'facebook'), ('INSTAGRAM', 'instagram'), ('TWITTER', 'twitter'), ('PINTEREST', 'pinterest'), ('SNAPCHAT', 'snapchat'), ('TIKTOK', 'tiktok'), ('DISCORD', 'discord'), ('GITHUB', 'Github')], max_length=10, null=True)),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name': 'Network',
                'verbose_name_plural': 'Networks',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', stdimage.models.StdImageField(blank=True, upload_to='profile', verbose_name='Image')),
                ('occupation', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('gender', models.CharField(blank=True, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('network', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='perfil.network', verbose_name='network')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
