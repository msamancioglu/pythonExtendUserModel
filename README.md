# Extending base User Model of Django 

Example Python/Django application for extending default User model of Django with additional fields by inheriting AbstractUser base model.

P.S.:
  Preferably, this must be done before any reference to User model in your app to prevent conflicts 

--------------

# So, let's do it!


First of all, import AbstractUser model in models.py (customuserapp/models.py):

         from django.contrib.auth.models import AbstractUser

Then, extend AbstractUser with new fields (bio, location, birth_date, second_mail, etc.)

          class User(AbstractUser):
                  bio = models.TextField(max_length=500, blank=True)
                  location = models.CharField(max_length=30, blank=True)
                  birth_date = models.DateField(null=True, blank=True)
                  second_email  = models.EmailField(null=True, blank=True)


Add following line to settings.py (customuser/settings.py)

          AUTH_USER_MODEL = 'customuserapp.User'


Finally, migrate database

         python manage.py migrate


