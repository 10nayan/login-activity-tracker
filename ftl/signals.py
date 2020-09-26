from django. contrib.auth.signals import user_logged_in,user_logged_out
from django.dispatch import receiver
from datetime import datetime
from tzlocal import get_localzone
from .models import Activity
local_tz=get_localzone()
query_time=datetime(2020,1,1,0,0,0)

#this function writes a new entry to Activity model when a user logged in
@receiver(user_logged_in)
def post_login(sender,user,request,**kwargs):
    time1=datetime.now()
    activity=Activity.objects.create(tz=local_tz,start_time=time1,end_time=time1,user_linked=request.user)
    activity.save()
    global query_time
    query_time=time1

#this function updates 'end_time' entry of Activity model when a user logged out 
@receiver(user_logged_out)
def post_logout(sender,user,request,**kwargs):
    a=Activity.objects.get(start_time=query_time,user_linked=request.user)
    a.end_time=datetime.now()
    a.save(update_fields=['end_time'])