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
    reemail=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)


    def clean_botcatcher(self):
        cu=self.cleaned_data['botcatcher']
        if len(cu)>0:
            raise forms.ValidationError('bot is catched')

    def clean_url(self):
        cu=self.cleaned_data['url']
        if cu[-1]=='n':
            raise forms.ValidationError('Ended with in')

    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['reemail']
        if e!=re:
            raise forms.ValidationError('Data is invalid')


class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    date=forms.DateField()
    author=forms.CharField(validators=[validate_for_a,validate_for_len])
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=True)

    def clean_botcatcher(self):
        cu=self.cleaned_data['botcatcher']
        if len(cu)>0:
            raise forms.ValidationError('bot is catched')