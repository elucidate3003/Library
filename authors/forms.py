from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ('name','about','dob','language','country','image','books_in_collection')
    def clean_about(self):
        content = self.cleaned_data.get('about')
        if len(content) > 100:
            raise forms.ValidationError('That is too long!')
        return content

    def clean(self,*args, **kwargs ):
        data = self.cleaned_data
        about = data.get('about')
        print(about)
        if about == '':
            about = None
        photo = data.get('image')

        if about is None and photo is None:
            raise forms.ValidationError('Error in About or No photo')
        super().clean(*args, **kwargs)
