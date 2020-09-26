from django.db import models
from django.conf import settings

#Activity model to store users activity period and their timezone,and has a one to one relational mapping to Users model
class Activity(models.Model):
    tz=models.TextField(null=True,blank=True)
    start_time=models.DateTimeField(null=True,blank=True)
    end_time=models.DateTimeField(null=True,blank=True)
    user_linked=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='userliked')