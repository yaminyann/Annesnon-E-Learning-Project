from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from django.utils.translation import gettext, gettext_lazy as _


# Contact form 
class Contact_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        widget_attrs = self.fields['name'].widget.attrs
        widget_attrs['class'] = 'form-control'
        widget_attrs = self.fields['email'].widget.attrs
        widget_attrs['class'] = 'form-control'
        widget_attrs = self.fields['subjects'].widget.attrs
        widget_attrs['class'] = 'form-control'
        widget_attrs = self.fields['textbox'].widget.attrs
        widget_attrs['style'] = 'height: 150px;'
            
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subjects = forms.CharField(max_length=100)
    textbox = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    
# Signup form
class SignUp(UserCreationForm):
    email = forms.CharField(
        required=True, widget=forms.EmailInput(attrs={'class':'form-control'})
        )
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'})
        )
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'})
        )
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'})
        }
        
# Login form
class Login(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'})
        )
    password = forms.CharField(
        label=_('Password'),strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current_password','class':'form-control'})
        )
    