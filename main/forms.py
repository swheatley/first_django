from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from main.models import City, CustomUser
from django import forms 

#from django.core.validators import RegexValidator
from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True) 
    phone = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea) 

    # args are variables,  kwargs (key-word ) argument are variables and a value
    # val, val2="something"
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/contact_view/'
        self.helper.layout = Layout(
                Div('name', 'email', 'phone', css_class = 'col-md-6'),
                Div('message' , css_class = 'col-md-6')
            )

        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Submit', css_class="btn-primary")
                )
            )


class CityEditForm(forms.ModelForm):

    class Meta:
        model = City
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CityEditForm, self). __init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/city_edit/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', "Save Changes", css_class="btn-primary"),
                )
            ) 
 

# #class StateCapitalEditForm(forms.ModelForm):

#     class Meta:
#         model = StateCapital
#         fields = '__all__'
        
#     def __init__ (self, *args, **kwargs):
#         super(StateCapitalEditForm, self). __init__(*args, **kwargs

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        class Meta:
            model = CustomUser
            fields = ['email']
            exclude = ['username']


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserhangeForm, self).__init(*args, **kwargs)
        #del self.fields['username']

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
        exlcude = ['username']


class UserSignUp(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class UserLogin(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
