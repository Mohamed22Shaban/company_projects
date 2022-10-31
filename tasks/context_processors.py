from . models import EmailSubscribe
from .forms import RegisterForm
def recive_email(request):
    if "email" in RegisterForm(request.POST):
        email = request.POST.get("email") 
        if not EmailSubscribe.objects.filter(email=email).exists():
            EmailSubscribe.objects.create(email=email) # 
    else:
        return {}

