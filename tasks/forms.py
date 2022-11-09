from django import forms
from . models import Project, Category ,EmailSubscribe
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
            'retal_cost_day',
            'retal_priod',
            'total_retal',
            'status',
            'category',
        ]


        lebels ={
            'name':_('name'),
            'engineer':_('engineer'),
            'photo_project':_('photo_project'),
            'photo_engineer':_('photo_engineer'),
            'proid':_('proid'),
            'cost':_('cost'),
            'retal_cost_day':_('retal_cost_day'),
            'retal_priod':_('retal_priod'),
            'total_retal':_('total_retal'),
            'status':_('status'),
            'category':_('category'),
        }


        widgets = {
            'name':forms.TextInput(attrs={ 'class':'form-control'}),
            'engineer':forms.TextInput(attrs={ 'class':'form-control'}),
            'photo_project':forms.FileInput(attrs={ 'class':'form-control'}),
            'photo_engineer':forms.FileInput(attrs={ 'class':'form-control'}),
            'proid':forms.NumberInput(attrs={ 'class':'form-control'}),
            'cost':forms.NumberInput(attrs={ 'class':'form-control'}),
            'retal_cost_day':forms.NumberInput(attrs={ 'class':'form-control', 'id':'retailprice'}),
            'retal_priod':forms.NumberInput(attrs={ 'class':'form-control', 'id':'retailpriod'}),
            'total_retal':forms.NumberInput(attrs={ 'class':'form-control', 'id':'totalretail'}),
            'status':forms.Select(attrs={ 'class':'form-control'}),
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



