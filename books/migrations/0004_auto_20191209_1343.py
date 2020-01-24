# Generated by Django 2.2.7 on 2019-12-09 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='Book'),
        ),
        migrations.AlterField(
            model_name='review',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Username'),
        ),
    ]