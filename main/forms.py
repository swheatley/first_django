from django import forms 
from django.core.validators import RegexValidator

class CitySearchForm(forms.Form):  
    name = forms.CharField(required=True, initial=”Orem”)
    state = forms.CharField(required=True, initial=”Utah”)



class CitySearchForm(forms.Form):  
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    name = forms.CharField(required=True, initial='Orem', validators=[alphanumeric])
    state = forms.CharField(required=True, initial='Utah', validators=[alphanumeric])


class CreateCityForm(forms.ModelForm):  
    class Meta:
        model = City
