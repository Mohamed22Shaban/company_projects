from django.shortcuts import render , redirect
from . models import *
from .forms import ProjectForm, CategoryForm
from django.utils.translation import gettext as _


from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.

def index(request):

    # add Project
    if request.method == 'POST':
        add_Project = ProjectForm(request.POST,request.FILES)
        if add_Project.is_valid():
            add_Project.save()
    # add category

        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
#add participate
        # add_participate = ParticipateForm(request.POST)
        # if add_participate.is_valid():
        #     add_participate.save()
        #     send_emails()

    context = {
        _('category'): Category.objects.all(),
        'Projectsss':Project.objects.all(),
        'form':ProjectForm(),
        'formcat':CategoryForm(),
        'allProjects':Project.objects.filter(active=True).count(),
        'Projectsold':Project.objects.filter(status='completed projects').count(),
        'Projectvaliable':Project.objects.filter(status='in progress projects').count(),
        'Projectretail':Project.objects.filter(status='joint projects').count(),
    }

    return render(request, 'pages/index.html', context)






def Projects(request):

    # deal with search 
    search = Project.objects.all()
    
    name = None
    if 'search_name' in request.GET:
        name = request.GET['search_name']
        if name:
            search = search.filter(title__icontains = name)



    context = {
        'category': Category.objects.all(),
        'Projectsss':search,
        'formcat':CategoryForm(),



        }


    return render(request, 'pages/project.html',context)


def update(request ,id):
    
    # get id
    Project_id = Project.objects.get(id = id)
    if request.method == 'POST':
        Project_save = ProjectForm(request.POST , request.FILES , instance=Project_id)
        if Project_save.is_valid():
            Project_save.save()
            return redirect('/')
    else:
        Project_save = ProjectForm(instance=Project_id)


    context = {
        'form':Project_save,
    }


    return render(request, 'pages/update.html',context)





def delete(request, id):

    Project_delete_id= Project.objects.get(id = id)
    if request.method == 'POST':
        Project_delete_id.delete()
        return redirect('/')
    
    

    return render(request, 'pages/delete.html')









def send(request):
    return render(request,'pages/register.html' )


# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from accounts.forms import UserRegisterForm
# from django.contrib.auth import login

# ## create registration
# class RegisterView(CreateView):
#     form_class = UserRegisterForm
#     # success_url = reverse_lazy('login')

    # def get_success_url(self):
    #     login(self.request, self.object)  #=> to automatic register
    #     return reverse_lazy('base')
#     template_name = 'pages/register.html'