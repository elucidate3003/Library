# Generated by Django 2.2.7 on 2019-11-19 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50, verbose_name='Gender')),
                ('state', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=15, verbose_name='phone no')),
                ('district', models.CharField(max_length=50)),
                ('languages', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='profile')),
            ],
        ),
    ]
