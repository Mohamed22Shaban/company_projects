from django.shortcuts import render , redirect
from . models import *
# from .forms import ProjectForm, CategoryForm
from django.utils.translation import gettext as _
from django.conf import settings



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

        'category': Category.objects.all(),
        'Projectsss':Project.objects.all(),
        'clients':Clients.objects.all(),
        'allprojects':Project.objects.filter(active=True).count(),
        'allclients':Clients.objects.filter(active=True).count(),
   
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
        # 'formcat':CategoryForm(),



        }


    return render(request, 'pages/project.html',context)

#update
# def update(request ,id):
    
#     # get id
#     Project_id = Project.objects.get(id = id)
#     if request.method == 'POST':
#         # Project_save = ProjectForm(request.POST , request.FILES , instance=Project_id)
#         if Project_save.is_valid():
#             Project_save.save()
#             return redirect('/')
#     else:
#         # Project_save = ProjectForm(instance=Project_id)


#     context = {
#         'form':Project_save,
#     }


#     return render(request, 'pages/update.html')


def show(request, id):
    
    # get id
    # model = Project.objects.filter(id = id).first()
    model = Project.objects.get(id = id)
    


    return render(request, 'pages/show.html',{
        'articles': model
    })


# from . forms import *
# def contact(request):
#     model = RecievMessages.objects.all
#     if request.method == 'POST':
#         email = request.POST.get("email")# جلب القيمة من الريكوست
#         if not RecievMessages.objects.filter(email=email).exists(): # نتأكد من أن الايميل غير مسجل عندنا لكي نتجنب التكرار
#             RecievMessages.objects.create(email=email) # انشاء كائن وحفظه في قاعدة البيانات
#             return redirect('/')
#     return render(request, 'pages/contact.html',{
#         'articles': model,
#         'formuser': ContactForm()
#     })

from . forms import *
def contact(request):
    # model = Project.objects.all()
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     phone = request.POST['phone']
    #     message = request.POST['message']

        
   
    
    #     send_mail(
    #     name,
    #     message,
    #     phone,
    #     ['settings.EMAIL_HOST_USER'],
    #     # ['mohamedtelb200@gmail.com'],
    #     email,
        
    # )
    if request.method == 'POST':
        add_book = ContactForm(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()

    context = {
        
        'form':ContactForm(),
     
    }


    return render(request, 'pages/contact.html', context
        
    )




# delete
# def delete(request, id):

#     Project_delete_id= Project.objects.get(id = id)
#     if request.method == 'POST':
#         Project_delete_id.delete()
#         return redirect('/')
    
    

    # return render(request, 'pages/delete.html')





## email settings


def send(request):
    if "email" in request.POST:
        email = request.POST.get("email")# جلب القيمة من الريكوست
        if not EmailSubscribe.objects.filter(email=email).exists(): # نتأكد من أن الايميل غير مسجل عندنا لكي نتجنب التكرار
            EmailSubscribe.objects.create(email=email) # انشاء كائن وحفظه في قاعدة البيانات
            return redirect('/')

    con = {
        'formuser': RegisterForm()
    }
    return render(request,'pages/register.html',con)





