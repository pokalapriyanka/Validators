from django import forms
from app.models import *
from app.views import *



def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('Should not startswith a')

def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('Length should not be more than 5')
    
class TopicForm(forms.Form):
    topic_name=forms.CharField(validators=[validate_for_a,validate_for_len])

class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(validators=[validate_for_a,validate_for_len])
    url=forms.URLField()
    email=forms.EmailField()

class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    date=forms.DateField()
    author=forms.CharField(validators=[validate_for_a,validate_for_len])