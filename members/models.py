from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from books.models import Book

# Create your models here.

class Member(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"),related_name='profile', on_delete=models.CASCADE, blank=True, null=True)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(_("Gender"),choices=(('male','Male'),('female','Female')), max_length=50)
    state = models.CharField( max_length=50)
    phone_no = models.CharField(_("phone no"), max_length=15)
    district = models.CharField( max_length=50)
    languages = models.CharField( max_length=50)
    occupation = models.CharField( max_length=50)       

    def __str__(self):
        return 's'
     
class Rented_Books(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name=_("book"), related_name="renter", on_delete=models.CASCADE)
    date = models.DateField(_("Rented on"), auto_now=False, auto_now_add=False)