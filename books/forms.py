from django import forms
from .models import Review
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Field, ButtonHolder

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('username','stars','comment')
        exclude = ('book',)

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-group my-4'
        self.helper.label_class = 'col-md-6 col-form-label'
        self.helper.input_class = 'col-md-6 form-control'
        self.helper.layout = Layout(Div(Field('stars'), Field('comment'), ButtonHolder(Submit('submit', 'Post'))))



