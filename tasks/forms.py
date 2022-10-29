from django import forms
from . models import Project, Category ,EmailSubscribe


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
        
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




# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = EmailSubscribe
#         fields = ['email', ]



# class RegisterForm(forms.ModelForm):

#     email = forms.EmailField(label='البريد الإلكتروني')
  

#     class Meta:
#         model = EmailSubscribe
#         fields = ( 'email', )
