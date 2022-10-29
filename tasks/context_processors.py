from . models import EmailSubscribe

def recive_email(request):
    if "email" in request.POST:
        email = request.POST.get("email") 
        EmailSubscribe.objects.create(email=email) # 
    else:
        return {}
