# Generated by Django 2.2.7 on 2019-11-22 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20191122_1753'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0002_auto_20191122_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rented_Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Rented on')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
