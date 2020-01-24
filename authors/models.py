from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

def upload_photo(instance,filename):
    return f'{instance.name}/{filename}'


class Author(models.Model):
      
    name = models.CharField(max_length=100)
    about = models.TextField(_("About"),null=True, blank=True)
    dob = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50, blank=True, null=True)
    books_in_collection = models.IntegerField(_("Books in Collection"), blank=True,null=True, default=0)
    image = models.ImageField(_("Photo"), upload_to=upload_photo,null=True, blank=True)


    def __str__(self):
        return self.name

    

