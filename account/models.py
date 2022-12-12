from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils import timezone
class CustomUser(AbstractUser):
    user_type_data = (('Member','Member'),('Director','Director'),('Executive Council','Executive Council'),('Assistant Director','Assistant Director'),('Sponsor','Sponsor'),('Patron','Patron'))
    user_type=models.CharField(default='Member',choices=user_type_data,max_length=20)
