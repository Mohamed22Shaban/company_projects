from django import forms
from . models import Project, Category ,EmailSubscribe, RecievMessages

from django.utils.translation import gettext as _

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]

        lebels ={
            'name':_('name')
        }
        
        widgets = {
            'name':forms.TextInput(attrs={ 'class':'form-control'}),
            }



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = [
            'name',
            'engineer',
            'photo_project',
            'photo_engineer',
            'proid',
            'cost',
            'category',
        ]


        lebels ={
            'name':_('name'),
            'engineer':_('engineer'),
            'photo_project':_('photo_project'),
            'photo_engineer':_('photo_engineer'),
            'proid':_('proid'),
            'cost':_('cost'),
            'category':_('category'),
        }


        widgets = {
            'name':forms.TextInput(attrs={ 'class':'form-control'}),
            'engineer':forms.TextInput(attrs={ 'class':'form-control'}),
            'photo_project':forms.FileInput(attrs={ 'class':'form-control'}),
            'photo_engineer':forms.FileInput(attrs={ 'class':'form-control'}),
            'proid':forms.NumberInput(attrs={ 'class':'form-control'}),
            'cost':forms.NumberInput(attrs={ 'class':'form-control'}),
       
            'category':forms.Select(attrs={ 'class':'form-control'}),

        }




## email settings
class RegisterForm(forms.ModelForm):

    class Meta:
        model = EmailSubscribe
        fields =[
            'email',

        ]

        lebels={
            'email':_('email'),
        }

        widgets={
            'email':forms.EmailInput(attrs={ 'class':'form-control'}),


        }
class ContactForm(forms.ModelForm):

    class Meta:
        model = RecievMessages
        fields =[
            'name',
            'email',
            'phone',
            'message',

        ]

        lebels={
            'name':_('name'),
            'email':_('email'),
            'phone':_('phone'),
            'message':_('message'),
        }

        widgets={
            'name':forms.TextInput(attrs={ 'class':'form-control'}),
            'email':forms.EmailInput(attrs={ 'class':'form-control'}),
            'phone':forms.NumberInput(attrs={ 'class':'form-control'}),
            'message':forms.TextInput(attrs={ 'class':'form-control'}),
        }



