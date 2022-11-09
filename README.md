**   Project's Company django 
project show my company's project with profit datails  and every project with its engineer and cost and period 


**  Libraries and framework used:
Python 3.10.7
Django 2.2
Django==4.1.2
django-crispy-forms==1.14.0
gunicorn==20.1.0
heroku==0.1.4
Jinja2==3.1.2
lazy-object-proxy==1.7.1
Pillow==9.2.0
psycopg2==2.9.5
pylint==2.15.3
virtualenv==20.16.5
whitenoise==6.2.0

** Steps to download project:
1- Download the full project from this link:
https://github.com/Mohamed22Shaban/company_projects

1- Create your virtual environment:
-  virtualenv .

2- Activate your virtual enviroment:
-  .\Scripts\activate

3-create project  =>> django-admin startproject main_project .
- make settings for the project and url

4- Run your developement server:
python manage.py runserver

5-create apps  => python mange.py startapp task , accounts ,blog
-make settings for apps in INSTALLED_APPS and creat its url 
6-create its model in model.py   
- create datebase  in postgresql or sqlite3
-python manage.py createsuperuser
and tied your model in admin.py to sho in database
use cod => python manage.py makemigrations ,, python manage.py migrate

 and function in views.py and tied them with urls .py for each app 
- crate template folder in virtual and creat file for each function

7-make static settins  py creat static folder in the main_project and put ccs folder and js folder and img folder in it 
- and settings of media
and then call it py   =>> python manage.py collectstatic

8- Installation of packages via Requirements.txt file:
pip install -r Requirements.txt

9- Change directory using this code:
cd src

8- create ropestry in github 
- make setting in .gitignore file

$ git init
$ git add .
$ git commit -m "your commit"
$ git remote add origin URL
$ git push -u origin main or master








-- Deploy to Heroku
Run the following commands to deploy the app to Heroku:
- notice " should create Procfile in the virtual and make whitenoise settings  "


$ heroku open
$ heroku login
$ heroku create projectname
$ heroku git:remote -a projectname
$ git push heroku master or master
$ heroku open
- if there are any blogs use:
$ heroku logs --tail
