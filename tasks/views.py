from django.shortcuts import render , redirect
from . models import *
from .forms import ProjectForm, CategoryForm
from django.utils.translation import gettext as _



def index(request):

    # add Project
    # if request.method == 'POST':
    #     add_Project = ProjectForm(request.POST,request.FILES)
    #     if add_Project.is_valid():
    #         add_Project.save()
    # add category

        # add_category = CategoryForm(request.POST)
        # if add_category.is_valid():
        #     add_category.save()

    context = {
        _('category'): Category.objects.all(),
        'Projectsss':Project.objects.all(),
        # 'form':ProjectForm(),
        # 'formcat':CategoryForm(),
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

#update
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


    return render(request, 'pages/update.html')




# delete
def delete(request, id):

    Project_delete_id= Project.objects.get(id = id)
    if request.method == 'POST':
        Project_delete_id.delete()
        return redirect('/')
    
    

    return render(request, 'pages/delete.html')







from . forms import RegisterForm

def send(request):
    if "email" in request.POST:
        email = request.POST.get("email")# جلب القيمة من الريكوست
        if not EmailSubscribe.objects.filter(email=email).exists(): # نتأكد من أن الايميل غير مسجل عندنا لكي نتجنب التكرار
            EmailSubscribe.objects.create(email=email) # انشاء كائن وحفظه في قاعدة البيانات
            return redirect('/')

        # elif EmailSubscribe.objects.filter(email__iexact=email).exists():
            # print('this is already register')

    con = {
        'formuser': RegisterForm()
    }
    return render(request,'pages/register.html',con)





