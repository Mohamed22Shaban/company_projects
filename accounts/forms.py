from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label=_('username'), max_length=30,  )
    email = forms.EmailField(label=_('email'))
    first_name = forms.CharField(label=_('firstname'))
    last_name = forms.CharField(label=_('lastname'))
    password1 = forms.CharField(
        label=_('password'), widget=forms.PasswordInput(), min_length=8)
    password2 = forms.CharField(
        label=_('repassword'), widget=forms.PasswordInput(), min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا الاسم.')
        return cd['username']


class LoginForm(forms.ModelForm):
    username = forms.CharField(label=_('username'))
    password = forms.CharField(
        label=_('passward'), widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label=_('firstname'))
    last_name = forms.CharField(label=_('lastname'))
    email = forms.EmailField(label=_('email'))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
