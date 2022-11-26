from django.db import models
# from django.conf.global_settings import AUTH_USER_MODEL

# Create your models here.
from django.db import models

from django.utils.translation import gettext as _

class Category(models.Model):
    order = models.IntegerField(default=1)
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name


class Sales(models.Model):
    amount = models.FloatField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    active = models.BooleanField(default=True)
    



class Clients(models.Model):
    name = models.CharField(max_length= 50)
    photo_clients = models.ImageField(upload_to='photos_file', null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Project(models.Model):
 

    name = models.CharField(max_length= 250)
    engineer = models.CharField(max_length= 250, null=True, blank=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    place = models.CharField(max_length= 250, null=True, blank=True)
    manager = models.CharField(max_length= 250, null=True, blank=True)
    photo_project = models.ImageField(upload_to='photos_file', null=True, blank=True)
    photo_engineer = models.ImageField(upload_to='photos_file', null=True, blank=True)
    proid = models.IntegerField(null=True, blank=True)
    cost = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  
    created_at = models.DateTimeField(auto_now_add=True ,null=True, blank=True)

    datails = models.TextField(null=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    # user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE ,null=True)
    # sales = models.OneToOneField(Sales, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.name








class Order(models.Model):
    sales = models.OneToOneField(Sales, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')







## email settings

class EmailSubscribe(models.Model):
    email = models.EmailField(max_length=254, unique=True,null=True,blank=True)
   
    def __str__(self):
        return self.email



from django.conf import settings 
from django.core.mail import send_mail


class EmailSender(models.Model):
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs): # هذه الدالة تنفذ عندما يتم حفظ النموذج أو أنشاءه
        emails = list(EmailSubscribe.objects.values_list('email', flat=True))#جلب جميع الاميلات المسجلة
        subject = self.title
        message = self.content
        email_from = settings.EMAIL_HOST_USER
        recipient_list = emails
        send_mail( subject, message, email_from, recipient_list )
        super().save(*args, **kwargs)


class RecievMessages(models.Model):
    name = models.TextField(null=True)
    email = models.EmailField(max_length=254, unique=True,null=True,blank=True)
    message = models.TextField(null=True)
    phone = models.IntegerField(null=True)
   
    def __str__(self):
        return self.email