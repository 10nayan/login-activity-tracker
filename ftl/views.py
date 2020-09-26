from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Activity
User = get_user_model()
from .forms import UserForm
# Create your views here.

#this function registers new user
def register(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully, signin now')
            return redirect('/signin')
    else:
        form=UserForm()
    return render(request,'ftl/register.html',{'form':form})

#this function is for signin new user to application and redirects to home page
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            messages.warning(request,"Invalid username or password")
            return redirect('/signin')
    return render (request,'ftl/signin.html')

#this function signout already logged in user,if no user is curently logged in it will throw warning message
def signout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have succesfully logged out")
        return redirect('/signin')
    messages.warning(request,"You are already logged out")
    return redirect('/signin')

#this function returns json response of activity status of users 
def home(request):
    response_data = {"ok": False,"members":[]}
    response_data['ok']=True
    queryset=Activity.objects.all()
    query=User.objects.all()
    for user in query:
        newdict={}
        newdict['id']=user.username
        newdict['real_name']=user.get_full_name()
        try:
            objects=Activity.objects.filter(user_linked=user)
            newdict['tz']=objects[0].tz
            newdict['activity_periods']=[{'start_time':obj.start_time.strftime("%b %d %Y, %H:%M:%S %p"),'end_time':obj.end_time.strftime("%b %d %Y, %H:%M:%S %p")} for obj in objects]
        except:
            newdict['tz']="N/A"
            newdict['activity_periods']=[{'start_time':"",'end_time':""}]
        response_data['members'].append(newdict)

    return JsonResponse(response_data)
