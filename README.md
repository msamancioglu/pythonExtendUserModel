# Extending base User Model of Django 

Example Python/Django application for extending default User model of Django with additional fields by inheriting AbstractUser base model.


First, import AbstractUser model in models.py (customuserapp/models.py):

         from django.contrib.auth.models import AbstractUser

Then, extend AbstractUser

          class User(AbstractUser):
         

Finally, add following line to settings.py (customuser/settings.py)

          AUTH_USER_MODEL = 'customuserapp.User'


P.S.:
  Preferably, this must be done before any reference to User model in your app to prevent conflicts 
