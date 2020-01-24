# Generated by Django 2.2.7 on 2019-11-22 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_rented_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rented_books',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renter', to='books.Book', verbose_name='book'),
        ),
    ]
