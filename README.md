**   Project's Company django **



& Main features 

- Separated dev and projects settings

- User registration and logging 

- Procfile for easy deployments

- Separated requirements files

- SQLite by default and then use postgres instead

- sending an email to contact us

- participate in newsletter by email

- sending emails to paricipants py admin

- statistics page in admin for prjects

- publish a post control in projects from admin

- add comments for posts

- use language buttom to change language

- choose the category that you need 

- press on the project to show more details





& how can use the project 

- install python in your system and create virtual environment and activate it  
- activate => .\Scripts\activate
- use => pip install django
- Installation of packages via Requirements.txt file => pip install -r Requirements.txt
- create project  =>> django-admin startproject main_project .
- create apps  => python mange.py startapp task , accounts ,blog
- create datebase  in postgresql or sqlite3 =>python manage.py makemigrations ,, python manage.py migrate
- Run your developement server => python manage.py runserver
- make static settings =>> python manage.py collectstatic
- create locale file to trans and run => python manage.py makemessages -l ar  the  => python manage.py compilemessages


& to get in admin page use :
- python manage.py createsuperuser
- create your superuser, email and password





