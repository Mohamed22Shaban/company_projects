from django.shortcuts import render, redirect
from .forms import UserCreationForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from blog.models import Post

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



from django.views.generic import CreateView
from django.urls import reverse_lazy




class RegisterView(CreateView):
    form_class = UserCreationForm
    # if form_class.is_valid():
    #     form_class.save()
    # success_url = reverse_lazy('login')
    template_name = 'user/register.html'

    def get_success_url(self):
        login(self.request, self.object) 
        return reverse_lazy('profile')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.warning(
                request, 'هناك خطأ في اسم المستخدم أو كلمة المرور.')

    return render(request, 'user/login.html', {
        'title': 'تسجيل الدخول',
    })


def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {
        'title': 'تسجيل الخروج'
    })


@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user)
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)
    return render(request, 'user/profile.html', {
        'title': 'الملف الشخصي',
        'posts': posts,
        'page': page,
        'post_list': post_list,
    })


@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'تم تحديث الملف الشخصي.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'تعديل الملف الشخصي',
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'user/profile_update.html', context)
