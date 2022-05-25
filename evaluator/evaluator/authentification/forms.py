from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, UserChangeForm

User = get_user_model()

import logging

logger = logging.getLogger(__name__)

class LoggingMixin(object):
    def add_error(self, field, error):
        if field:
            logger.info('Form error on field %s: %s', field, error)
        else:
            logger.info('Form error: %s', error)
        super().add_error(field, error)


class ProloginUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput, max_length=200)
    username = forms.CharField(max_length=64)
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    birthdate = forms.DateField(widget=forms.DateInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']
    
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email 

    def save(self, commit=True):  
        user = User.objects.create_user(  
            self.cleaned_data['email'],
            self.cleaned_data['username'],  
            self.cleaned_data['first_name'],
            self.cleaned_data['last_name'],
            self.cleaned_data['birthdate'],  
            self.cleaned_data['password1'],
        ) 
        if commit:
            user.save()
        return user 
    
    def save_m2m(self):
        # chetor
        pass


class AdminProloginUserCreationForm(ProloginUserCreationForm):
    def save(self, commit=True):  
        user = User.objects.create_superuser(  
            self.cleaned_data['email'],
            self.cleaned_data['username'],  
            self.cleaned_data['first_name'],
            self.cleaned_data['last_name'],
            self.cleaned_data['birthdate'],  
            self.cleaned_data['password1'],
        )
        if commit:
            user.save()
        return user 


class AdminProloginUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_password(self):
        return self.initial["password"]